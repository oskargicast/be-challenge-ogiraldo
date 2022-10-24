from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Creates a dummy superuser'

    def handle(self, *args, **options):
        try:
            super_user = User.objects.create_user(
                username='admin',
                email='oscar.gi.cast@gmail.com',
                password='admin'
            )
        except IntegrityError:
            raise CommandError('Superuser is already created. Check the README file.')
        super_user.is_superuser = True
        super_user.is_staff = True
        super_user.save()
        self.stdout.write(
            self.style.SUCCESS(
                f'====Superuser created====\n'
                f'Username: admin\n'
                f'Password: admin\n'
            )
        )