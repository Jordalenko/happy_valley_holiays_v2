import os
from django.conf import settings
from django.core.management.base import BaseCommand
from cottages.models import Cottage, CottageImage

class Command(BaseCommand):
    help = "Import cottage images from media/cottages/<cottage_slug>/ folders"

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Run the import without saving any changes',
        )
        parser.add_argument(
            '--undo',
            action='store_true',
            help='Undo the last import by deleting imported CottageImage entries'
        )

    def handle(self, *args, **options):
        media_path = os.path.join(settings.MEDIA_ROOT, 'cottages')
        dry_run = options['dry_run']
        undo = options['undo']
        import_log = 'last_imported_images.txt'

        if undo:
            if not os.path.exists(import_log):
                self.stdout.write(self.style.WARNING("No import log found. Cannot undo."))
                return
            with open(import_log, 'r') as f:
                ids = [int(line.strip()) for line in f if line.strip().isdigit()]
            deleted, _ = CottageImage.objects.filter(id__in=ids).delete()
            os.remove(import_log)
            self.stdout.write(self.style.SUCCESS(f"Undo complete. Deleted {deleted} CottageImage entries."))
            return

        if not os.path.exists(media_path):
            self.stdout.write(self.style.ERROR(f"Directory not found: {media_path}"))
            return

        if dry_run:
            self.stdout.write(self.style.WARNING("Running in dry-run mode: no changes will be saved."))

        created_images = []

        for folder_name in os.listdir(media_path):
            folder_path = os.path.join(media_path, folder_name)
            if not os.path.isdir(folder_path):
                continue

            try:
                cottage = Cottage.objects.get(slug=folder_name)
            except Cottage.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"No cottage with slug '{folder_name}' found. Skipping."))
                continue

            self.stdout.write(f"Processing images for cottage '{cottage.slug}'...")

            for filename in os.listdir(folder_path):
                if not filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    continue

                relative_path = f"cottages/{folder_name}/{filename}"
                exists = CottageImage.objects.filter(cottage=cottage, image=relative_path).exists()
                if exists:
                    self.stdout.write(f"Image '{filename}' already linked. Skipping.")
                    continue

                if not dry_run:
                    ci = CottageImage(cottage=cottage, image=relative_path)
                    ci.save()
                    created_images.append(ci)
                    self.stdout.write(self.style.SUCCESS(f"Added image '{filename}'."))
                else:
                    self.stdout.write(f"[Dry Run] Would add image '{filename}'.")

        self.stdout.write(self.style.SUCCESS(f"{'Simulated' if dry_run else 'Imported'} {len(created_images)} images."))

        if not dry_run:
            with open(import_log, 'w') as f:
                for ci in created_images:
                    f.write(str(ci.id) + '\n')
            self.stdout.write("You can undo this import by running:\n  python manage.py import_cottage_images --undo")
