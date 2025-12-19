from django.core.management import BaseCommand

from user.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email='admin@examle.com')
        user.set_password('123qwe')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

