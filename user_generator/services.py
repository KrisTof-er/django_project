from faker import Faker

fake = Faker()


def generate_user() -> str:
    user = fake.first_name(), fake.unique.ascii_email()
    return ' '.join(user)


def generator_of_users(users: int) -> str:
    for user_number in range(users):
        yield f"{user_number + 1}. {generate_user()}"
