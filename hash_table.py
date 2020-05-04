# create
my_dict ={}
grades = {'Ana': 'B', 'John': 'A+', 'Denise': 'A', 'Katy': 'A', 'test': None}

# avoid KeyError by adding default value F
grades.get('John', 'F')
# add
grades['Jack'] = 'C'
print(grades)

# look up
if 'Ana' in grades:
    print('can only look up key')
if 'A' in grades.values():  # time: O(n)
    print('or look up values in values')

# update
grades['Ana'] = 'A'

# delete a specific key
grades.pop('Ana')   # O(1)
del grades['John']  # O(n)
print(grades.pop("food", None))     # could delete even if food is not in
# del grades.values("A")

# time complexity O(1) space complexity O(n)

# convert
print(list(grades))
print(list(grades.values()))
# get keys and values
print(grades.items())
# get all keys as a list !! keys() and values() are in random order which is different from a list
print(list(grades.keys()))

for key in grades.keys():
    print(key)
# values
#  any type: immutable and mutable
#  can be duplicates
#  dictionary value can be a list or another dictionary
# keys
#  must be unique
#  immutable type
#  cannot be a list

