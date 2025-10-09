# ===========================================================
# Basic List
# 
# A list comprehension consists of "brackets containing"
# ===========================================================

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits.count('apple'))        #2
print(fruits.count('tangerine'))    #0

print(fruits.index('banana'))       #3
print(fruits.index('banana', 4))    #6

fruits.reverse()
print(fruits)   # ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

fruits.append('grape')
print(fruits)   # ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

fruits.sort()
print(fruits)   # ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

fruits.pop()
print(fruits)   # ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']

## remark
# For instance, [None, 'hello', 10] doesn’t sort 
# because integers can’t be compared to strings 
# and None can’t be compared to other types.

# ===========================================================
# 5.1.1 Using Lists as Stacks
# ===========================================================
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)       #[3, 4, 5, 6, 7]
stack.pop() #7
print(stack)        #[3, 4, 5, 6]
stack.pop() #6
stack.pop() #5
print(stack)        #[3, 4]


# ===========================================================
# 5.1.2 Using Lists as Queues
# ===========================================================
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves 'Eric'
queue.popleft()                 # The second to arrive now leaves'John'
print(queue)                    # Remaining queue in order of arrival deque(['Michael', 'Terry', 'Graham'])



# ===========================================================
# 5.1.3 List Comprehensions
# ===========================================================
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)  #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares2 = [x**2 for x in range(10)]
print(squares2) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print(combs)    # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combs)    # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]


vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]  #[-8, -4, 0, 4, 8]
# filter the list to exclude negative numbers
[x for x in vec if x >= 0]  #[0, 2, 4]
# apply a function to all the elements
[abs(x) for x in vec]   #[4, 2, 0, 2, 4]


# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]   #['banana', 'loganberry', 'passion fruit']


# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]   #[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]


# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]   #[1, 2, 3, 4, 5, 6, 7, 8, 9]


from math import pi
[str(round(pi, i)) for i in range(1, 6)]    #['3.1', '3.14', '3.142', '3.1416', '3.14159']


# ===========================================================
# 5.1.4 Nested List Comprehensions
# ===========================================================
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)   #[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

[[row[i] for row in matrix] for i in range(4)]  #[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

x = list(zip(*matrix))
print(x)    #[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]



# ===========================================================
# 5.2 The del statement
# ===========================================================

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a   # [1, 66.25, 333, 333, 1234.5]
del a[2:4]
a   # [1, 66.25, 1234.5]
del a[:]
a   # []


# ===========================================================
# 5.3 Tuples and Sequences
#
# A tuple consists of a number of values separated by commas, for instance:
# Tuples are immutable
# ===========================================================

t = 12345, 54321, 'hello!'
t[0]    # 12345
t       # (12345, 54321, 'hello!')
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u       # ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Tuples are immutable: 
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!
# t[0] = 88888
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment


# but ......  __"they can contain mutable objects"__:
v = ([1, 2, 3], [3, 2, 1])
v   # ([1, 2, 3], [3, 2, 1])
v[0][1] = 4
print(v)    # ([1, 4, 3], [3, 2, 1])

# A special problem is the construction of tuples containing 0 or 1 items: 
# the syntax has some extra quirks to accommodate these.
empty = ()
singleton1 = 'hello',    # <-- note trailing comma
singleton2 = ('hello',)
t = 12345, 54321, 'hello!' # is an example of tuple packing:
x, y, z = t
print(x)    # 12345
print(z)    # hello!


# ===========================================================
# 5.4 Sets
#
# A set is an unordered collection with no duplicate elements. unordered
# Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
# Curly braces or the set() function can be used to create sets. 
# Note: to create an empty set you have to use set(), not {};
# ===========================================================

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed {'orange', 'banana', 'pear', 'apple'}
'orange' in basket                 # fast membership testing > True
'crabgrass' in basket              # False

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a > {'a', 'r', 'b', 'c', 'd'}
a - b                              # letters in a but not in b > {'r', 'd', 'b'}
a | b                              # letters in a or b or both > {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
a & b                              # letters in both a and b > {'a', 'c'}
a ^ b                              # letters in a or b but not both > {'r', 'd', 'b', 'm', 'z', 'l'}

a = {x for x in 'abracadabra' if x not in 'abc'}
a   # {'r', 'd'}


# ===========================================================
# 5.5 Dictionaries
#
# It is best to think of a dictionary as a set of key: value pairs, with the requirement that the keys are unique.
# A pair of braces creates an empty dictionary: {}
# use the get() method instead, to prevent get KeyError 
# ===========================================================

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel             # {'jack': 4098, 'sape': 4139, 'guido': 4127}
tel['jack']     # 4098

# KeyError
# tel['irv']      
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'irv'

print(tel.get('irv'))   # None
del tel['sape']
tel['irv'] = 4127
tel                 # {'jack': 4098, 'guido': 4127, 'irv': 4127}
list(tel)           # ['jack', 'guido', 'irv']
sorted(tel)         # ['guido', 'irv', 'jack']
'guido' in tel      # True
'jack' not in tel   # False

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]) # {'sape': 4139, 'guido': 4127, 'jack': 4098}

{x: x**2 for x in (2, 4, 6)}    # {2: 4, 4: 16, 6: 36}

dict(sape=4139, guido=4127, jack=4098)  # {'sape': 4139, 'guido': 4127, 'jack': 4098}


# ===========================================================
# 5.6 Looping Techniques
#
# ===========================================================

# loop dictionary
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
# gallahad the pure
# robin the brave

# loop with index
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
# 0 tic
# 1 tac
# 2 toe

# loop with key value from 2 lists
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
# What is your name?  It is lancelot.
# What is your quest?  It is the holy grail.
# What is your favorite color?  It is blue.

# loop with sorted
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
# apple
# apple
# banana
# orange
# orange
# pear

# loop with unique and sorted
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
# apple
# banana
# orange
# pear

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
filtered_data   # [56.2, 51.7, 55.3, 52.5, 47.8]


# ===========================================================
# 5.7 More on Conditions
# Python treats 0, None, '', [], {}, set() → False
# ตัวอื่น ๆ → True
# ===========================================================

if []:
    print("This won't print")   # donot print this
if [1, 2]:
    print("This will print")    # print this

#ternary expression
x = 5
y = 10 if x > 0 else -10    # y = 10
print(y)