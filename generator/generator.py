import random
import string
from pathlib import Path


def generated_file():
    base_path = Path('.')
    path = rf'{base_path}\test_file{random.randint(0,999)}.txt'
    file = open(path, 'w+')
    file.write('Test string for file ')
    file.close()
    return file.name, path


def generated_string():
    test_string = (''.join(random.choices(string.ascii_lowercase, k=5)))
    return test_string


