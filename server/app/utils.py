

from faker import Faker
def generate_random_user():
    fake = Faker()
    random_name = fake.name()
    random_email = fake.email()
    # password = fake.password()

    user_data = {
        "username": random_name,
        "email": random_email,
        "password": "123"
    }
    return user_data
