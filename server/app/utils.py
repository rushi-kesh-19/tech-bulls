

from faker import Faker
def generate_random_user():
    fake = Faker()
    random_name = fake.name()
    random_email = fake.email()

    user_data = {
        "username": random_name,
        "email": random_email,
        "health_data": [],
        "created_at": datetime.utcnow()
    }
    return user_data
