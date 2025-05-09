import os
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates a superuser."

    def handle(self, *args, **options):
        # Fetch the password from an environment variable.
        password = os.environ.get("SUPERUSER_PASSWORD")
        if not password:
            self.stderr.write("Error: SUPERUSER_PASSWORD environment variable not set.")
            return

        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(username="admin", password=password)
            self.stdout.write("Superuser 'admin' has been created.")
        else:
            self.stdout.write("Superuser 'admin' already exists.")
