import random
import string
from pathlib import Path
from faker import Faker

from data.data import Person

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_file():
    base_path = Path('.')
    path = rf'{base_path}\test_file{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write('Test string for file ')
    file.close()
    return file.name, path


def generated_string():
    test_string = (''.join(random.choices(string.ascii_lowercase, k=5)))
    return test_string


def generated_person():
    yield Person(
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        job_title=faker_ru.company()
    )
