import random
from pathlib import Path


def generated_file():
    base_path = Path('.')
    path = rf'{base_path}\test_file{random.randint(0,999)}.txt'
    file = open(path, 'w+')
    file.write('Test string for file ')
    file.close()
    return file.name, path


