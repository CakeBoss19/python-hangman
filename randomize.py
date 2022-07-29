from posixpath import split
from random import randint
from dictionary import dictionary
def randomize():
    dictionary_list = dictionary.split()
    return dictionary_list[randint(0, 50000)]
