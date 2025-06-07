import os
from django.core.management.base import BaseCommand
from django.conf import settings
from cottages.models import Cottage, CottageImage
from django.core.files import File

class Command(BaseCommand):
    help = 'Populate CottageImage from media/cottages/**/<slug>/image.jpg'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Simulate what would happen without making changes.'
        )
        parser.add_argument(
            '--undo',
            action='store_true',
            help='Remove all CottageImage objects created via this script.'
        )

    def handle(self, *args, **options):
        dry_run = options['dry_run']
        undo = options['undo']
        base_dir = os.path.join(settings.MEDIA_ROOT, 'cottages')

        if undo:
            deleted, _ = CottageImage.objects.all().delete()
            self.stdout.write(self.style.WARNING(f"Deleted {deleted} CottageImage entries."))
            return

        count = 0

        for root, dirs, files in os.walk(base_dir):
            slug = os.path.basename(root)
            try:
                cottage = Cottage.objects.get(slug=slug)
            except Cottage.DoesNotExist:
                continue  # Skip non-matching folders

            for filename in files:
                if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    filepath = os.path.join(root, filename)
                    relative_path = f"cottages/{slug}/{filename}"

                    if CottageImage.objects.filter(cottage=cottage, image=relative_path).exists():
                        continue  # Skip duplicates

                    if dry_run:
                        self.stdout.write(f"[DRY RUN] Would add image: {relative_path} → {slug}")
                    else:
                        with open(filepath, 'rb') as f:
                            image = CottageImage(
                                cottage=cottage,
                                caption=filename
                            )
                            image.image.save(relative_path, File(f), save=True)
                            self.stdout.write(f"Added image {filename} to cottage '{slug}'")
                            count += 1

        if dry_run:
            self.stdout.write(self.style.WARNING("Dry run complete. No changes made."))
        else:
            self.stdout.write(self.style.SUCCESS(f"Imported {count} images."))