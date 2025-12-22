from collections import Counter

text = """Python is a powerful programming language.
Python is easy to learn, and Python is widely used in data science, web development, and automation.

Many developers like Python because it is readable and flexible.
However, Python is not perfect: Python can be slower than some other languages, but in most cases, Python is fast enough.

Learning Python helps developers think clearly and solve problems efficiently."""

def get_count_chars(text):
    count_dict = {}
    for i in text:
        num = count_dict.get(i)
        if num:
            count_dict[i] = num + 1
        else:
            count_dict[i] = 1

    print(count_dict)


# get_count_chars(text)

counter = Counter(text)
print(sorted(counter))


