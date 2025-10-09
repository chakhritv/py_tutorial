# ===========================================================
# 7. Input and Output
#
# ===========================================================


# ===========================================================
# 7.1 Fancier Output Formatting
# ===========================================================

# To use formatted string literals, begin a string with f or F before the opening quotation
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}') # 'Results of the 2016 Referendum'

# The str.format() method of strings requires more manual effort.
yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
print(yes_votes)    # 42572654
print(total_votes)  # 85705149
print(percentage)   # 0.496733912684756
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))

# When you don’t need fancy output but 
# just want a quick display of some variables for debugging purposes, 
# you can convert any value to a string with the repr() or str() functions.
s = 'Hello, world.'
str(s)      # 'Hello, world.'
repr(s)     # "'Hello, world.'"
str(1/7)    # '0.14285714285714285'
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)    # The value of x is 32.5, and y is 40000...

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)   # 'hello, world\n'

# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"


# ===========================================================
# 7.1.1 Formatted String Literals
# ===========================================================
import math
print(f'The value of pi is approximately {math.pi:.3f}.')   # The value of pi is approximately 3.142.

# Passing an integer after the ':' will cause that field to be a minimum number of characters wide.
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')     # name:min lenght = 10,  phone
# Sjoerd     ==>       4127
# Jack       ==>       4098
# Dcab       ==>       7678

# Other modifiers can be used to convert the value before it is formatted.
#  '!a' applies ascii(),
#  '!s' applies str(),
#  '!r' applies repr():
animals = 'eels'
print(f'My hovercraft is full of {animals}.')       # My hovercraft is full of eels.
print(f'My hovercraft is full of {animals!r}.')     # My hovercraft is full of 'eels'.

# The = specifier can be used to expand an expression to the text of the expression
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')        # Debugging bugs='roaches' count=13 area='living room'


# ===========================================================
# 7.1.2 The String format() Method
# ===========================================================
print('We are the {} who say "{}!"'.format('knights', 'Ni'))    # We are the knights who say "Ni!"

print('{0} and {1}'.format('spam', 'eggs'))     # spam and eggs
print('{1} and {0}'.format('spam', 'eggs'))     # eggs and spam

print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))
# This spam is absolutely horrible.

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))
# The story of Bill, Manfred, and Georg.

# This can be done by simply passing the dict and using square brackets '[]' to access the keys.
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678

# with the ** notation.
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678

for x in range(1, 11):
    print('{0:2d} {1:5d} {2:8d}'.format(x, x*x, x*x*x))
#  1     1        1
#  2     4        8
#  3     9       27
#  4    16       64
#  5    25      125
#  6    36      216
#  7    49      343
#  8    64      512
#  9    81      729
# 10   100     1000


# ===========================================================
# 7.1.3 Manual String Formatting
# ===========================================================

# There are similar methods str.ljust(), str.rjust(), str.center().
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))
#  1   1    1
#  2   4    8
#  3   9   27
#  4  16   64
#  5  25  125
#  6  36  216
#  7  49  343
#  8  64  512
#  9  81  729
# 10 100 1000

# str.zfill(), which pads a numeric string on the left with zeros.
'12'.zfill(5)               # '00012'
'-3.14'.zfill(7)            # '-003.14'
'3.14159265359'.zfill(5)    # '3.14159265359'


# ===========================================================
# 7.1.4 Old string formatting
# ===========================================================

# The % operator (modulo) can also be used for string formatting. 
print('The value of pi is approximately %5.3f.' % math.pi)  # The value of pi is approximately 3.142.


# ===========================================================
# 7.2 Reading and Writing Files
#
# Normally, files are opened in 'text mode' > read and write as string
#
# Mode can be 
#   'r' read only (default)
#   'w' write (delete existing file if exist)
#   'a' append
#   'r+' read and write
#   !!! '*b' append 'b' if need binary mode > read and write as bytes object
#
# It is good practice to use the with keyword when dealing with file objects. 
# The advantage is that the file is properly closed after its suite finishes
# ===========================================================

# f = open('test.txt', 'r')   # อ่านไฟล์
# f = open('test.txt', 'w')   # เขียนไฟล์ (ล้างทิ้งก่อน)
# f = open('test.txt', 'a')   # append ต่อท้าย
# f.close()   # เปิดไฟล์เสร็จ ควรปิดเสมอ:

# !!!! Warning !!!!
# Calling f.write() without using the 'with' keyword or calling f.close() 
# might result in the arguments of f.write() not being completely written to the disk, 
# even if the program exits successfully.

# open() returns a file object
i = 1
with open('workfile.txt', encoding="utf-8") as f:
    read_data = f.read()
    print(i, read_data)
    i +=1
    # no need to close manually

# We can check that the file has been automatically closed.
print(f.closed)     # True


# ===========================================================
# 7.2.1 Methods of File Objects
#
# data = f.read()          # อ่านทั้งหมด
# line = f.readline()      # อ่านทีละบรรทัด
# lines = f.readlines()    # อ่านทั้งหมดเป็น list
# list(f)                  # อ่านทั้งหมดเป็น list
# หากจบไฟล์แล้วสั่ง read() จะ return empty string ''
#
# f.write(string|bytes)           # returning the number of characters written.
# ===========================================================

with open('workfile.txt', encoding="utf-8") as f:
    for line in f:
        print(line, end='')
print()


# ===========================================================
# 7.2.2 Saving structured data with JSON
#
# The standard module called json can take Python data hierarchies, 
# and convert them to string representations; this process is called 'serializing'. 
# Reconstructing the data from the string representation is called 'deserializing'.
# ===========================================================

import json
data = {'name': 'John', 'age': 30, 'languages': ['Python', 'Java']}
print(type(data), data)
s = json.dumps(data)    # serializing แปลงเป็น string 
print(type(s), s)
j = json.loads(s)       # load string และ deserializing
print(type(j), j)

# เขียนไฟล์ JSON
with open('data.json', 'w') as f:
    json.dump(data, f)  # serializing แปลงเป็น string และ write ลง f

# อ่านไฟล์ JSON
with open('data.json', 'r') as f:
    obj = json.load(f)  # load string และ deserializing

print(type(obj), obj)