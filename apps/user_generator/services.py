import logging
from typing import NamedTuple, Iterator

from faker import Faker

fake = Faker()


class User(NamedTuple):
    name: str
    email: str


def generate_user() -> User:
    user_name = fake.first_name()
    user_email = fake.unique.ascii_email()
    logging.info(f"User {user_name} generated")
    return User(name=user_name, email=user_email)


def generator_of_users(users: int) -> Iterator[User]:
    for _ in range(users):
        yield generate_user()
