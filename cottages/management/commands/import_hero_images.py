import os
from django.core.management.base import BaseCommand
from cottages.models import HeroImage

class Command(BaseCommand):
    help = "Import hero images from media/hero/ folder"

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Simulate import without saving'
        )
        parser.add_argument(
            '--undo',
            action='store_true',
            help='Delete previously imported HeroImage entries'
        )

    def handle(self, *args, **options):
        folder_path = 'media/hero'
        dry_run = options['dry_run']
        undo = options['undo']

        if undo:
            count, _ = HeroImage.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f"Deleted {count} HeroImage entries."))
            return

        if not os.path.exists(folder_path):
            self.stdout.write(self.style.ERROR(f"Folder '{folder_path}' does not exist."))
            return

        created = []
        for filename in os.listdir(folder_path):
            if not filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                continue

            image_path = f'hero/{filename}'
            exists = HeroImage.objects.filter(image=image_path).exists()
            if exists:
                self.stdout.write(f"Image '{filename}' already exists. Skipping.")
                continue

            if dry_run:
                self.stdout.write(f"[DRY RUN] Would import: {filename}")
            else:
                hi = HeroImage(image=image_path, caption=filename)
                hi.save()
                created.append(hi)
                self.stdout.write(f"Imported: {filename}")

        if dry_run:
            self.stdout.write(self.style.WARNING("Dry run complete. No changes saved."))
        else:
            self.stdout.write(self.style.SUCCESS(f"Successfully imported {len(created)} images."))
