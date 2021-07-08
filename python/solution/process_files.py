from os import listdir
from os.path import isfile, join
import re

BOOK_DIR = "../books"


def process_string(string):
    return re.sub(r"[^A-Za-z]", " ", string).lower().split(" ")


def read_books():
    files = [f for f in listdir(BOOK_DIR) if isfile(join(BOOK_DIR, f))]
    books = {}
    for file in files:
        with open(join(BOOK_DIR, file), "r") as f:
            books[file] = process_string(f.read())

    return books
