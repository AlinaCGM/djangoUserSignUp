# populate_users.py
import os
import django
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoUser.settings")
django.setup()

from userlogin.models import User

fake = Faker()

def populate_users(num_users=10):
    for _ in range(num_users):
        User.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email()
        )

if __name__ == "__main__":
    populate_users()
