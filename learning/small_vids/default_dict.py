
from collections import defaultdict


text = """Python is a powerful programming language.
Python is easy to learn, and Python is widely used in data science, web development, and automation.

Many developers like Python because it is readable and flexible.
However, Python is not perfect: Python can be slower than some other languages, but in most cases, Python is fast enough.

Learning Python helps developers think clearly and solve problems efficiently."""


def get_word_list(text):
    word_list = text.split(' ')
    word_dict = {}
    for i in word_list:
        word = word_dict.get(i[0])
        if word:
            word.append(i)
        else:
            word_dict[i[0]] = [i]
    print(word_dict)

get_word_list(text)

def get_word_list_dd(text):
    word_list = text.split(' ')
    word_dict = defaultdict(list)
    for i in word_list:
        word_dict[i[0]] = i
    print(word_dict)

get_word_list_dd(text)