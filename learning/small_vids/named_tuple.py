from collections import namedtuple

person_1 = ('Bob', 30, 'Kyiv')

print(f'Simple tuple: Name {person_1[0]} Age {person_1[1]}, City {person_1[2]}')

Person = namedtuple('Person', ['name', 'age', 'city'])

person_2 = Person('Nike', 40, 'Kyiv')
person_3 = Person('Alena', 32, 'Odessa')

print(f'Named tuple: Name {person_2.name} Age {person_2[1]} City {person_2.city}')