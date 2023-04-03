from django.core.management.base import BaseCommand, CommandError

from silverstrike.lib import import_firefly


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'file',
            type=str,
            help='File to import')

    def handle(self, *args, **options):
        try:
            import_firefly(options['file'])
        except FileNotFoundError:
            raise CommandError(f"Could not open {options['file']} for writing")
        else:
            print(f"Imported transactions from {options['file']}")
