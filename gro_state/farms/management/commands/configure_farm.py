from django.core.management.base import BaseCommand
from gro_state.farms.models import Farm

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '-n', '--name', dest='name',
            help=Farm._meta.get_field_by_name('name')[0].help_text
        )
        parser.add_argument(
            '-s', '--slug', dest='slug',
            help=Farm._meta.get_field_by_name('slug')[0].help_text
        )
        parser.add_argument(
            '-l', '--layout', dest='layout',
            help=Farm._meta.get_field_by_name('layout')[0].help_text
        )

    def handle(self, *args, **options):
        farm = Farm.get_solo()
        for k, v in options.items():
            setattr(farm, k, v)
        farm.save()
