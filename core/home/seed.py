from django.contrib.auth.models import User
from faker import Faker
from home.models import Contribution
from random import randint

fake = Faker()


def seed_db(n):
    num_users = User.objects.count()
    for _ in range(n):
        user_index = randint(0, num_users - 1)
        user = User.objects.all()[user_index]
        donor_name = fake.name()
        phone = fake.phone_number()
        email = fake.email()
        address = fake.address()
        people = randint(20, 100)
        requests = 0
        contrib = Contribution(user=user, donor_name=donor_name, phone=phone, email=email, address=address, people=people, requests=requests)
        contrib.save()

seed_db(10)

