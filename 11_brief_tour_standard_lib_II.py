# ===========================================================
# 11. Brief Tour of the Standard Library — Part II
#
# ===========================================================


# ===========================================================
# 11.1. Output Formatting
#
# The reprlib module provides a version of repr() customized for abbreviated displays
# The pprint module offers more sophisticated control over printing both built-in and user defined objects
# The textwrap module formats paragraphs of text to fit a given screen width:
# The locale module accesses a database of culture specific data formats. 
# ===========================================================
import reprlib
print(set('supercalifragilisticexpialidocious'))
print(reprlib.repr(set('supercalifragilisticexpialidocious')))

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta','yellow'], 'blue']]]
pprint.pprint(t, width=30)
# [[[['black', 'cyan'],
#    'white',
#    ['green', 'red']],
#   [['magenta', 'yellow'],
#    'blue']]]

import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print(textwrap.fill(doc, width=40))
# The wrap() method is just like fill()
# except that it returns a list of strings
# instead of one big string with newlines
# to separate the wrapped lines.

import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')   # 'English_United States.1252'
conv = locale.localeconv()          # get a mapping of conventions
x = 1234567.8
locale.format_string("%d", x, grouping=True)    # '1,234,567'
locale.format_string("%s%.*f", (conv['currency_symbol'],conv['frac_digits'], x), grouping=True)    # '$1,234,567.80'


# ===========================================================
# 11.2. Templating
#
# ===========================================================

from string import Template
t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')  # 'Nottinghamfolk send $10 to the ditch fund.'

import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'
fmt = 'Ashley_%n%f'
t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))
# img_1074.jpg --> Ashley_0.jpg
# img_1076.jpg --> Ashley_1.jpg
# img_1077.jpg --> Ashley_2.jpg


# ===========================================================
# 11.3. Working with Binary Data Record Layouts
#
# ===========================================================

# import struct

# with open('myfile.zip', 'rb') as f:
#     data = f.read()

# start = 0
# for i in range(3):                      # show the first 3 file headers
#     start += 14
#     fields = struct.unpack('<IIIHH', data[start:start+16])
#     crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

#     start += 16
#     filename = data[start:start+filenamesize]
#     start += filenamesize
#     extra = data[start:start+extra_size]
#     print(filename, hex(crc32), comp_size, uncomp_size)

#     start += extra_size + comp_size     # skip to the next header


# ===========================================================
# 11.4. Multi-threading
#
# ===========================================================

import threading, zipfile, time

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        time.sleep(2)
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('workfile.txt', 'workflie.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')


# ===========================================================
# 11.5. Logging
#
# The logging module offers a full featured and flexible logging system.
# ===========================================================

import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')


# ===========================================================
# 11.6. Weak References
#
# Python does automatic memory management (reference counting for most objects and garbage collection to eliminate cycles). 
# The memory is freed shortly after the last reference to it has been eliminated.
# ===========================================================

# import weakref, gc
# class A:
#     def __init__(self, value):
#         self.value = value
#     def __repr__(self):
#         return str(self.value)
# a = A(10)                   # create a reference
# d = weakref.WeakValueDictionary()
# d['primary'] = a            # does not create a reference
# d['primary']                # fetch the object if it is still alive > 10
# del a                       # remove the one reference
# gc.collect()                # run garbage collection right away > 0
# d['primary']                # entry was automatically removed
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# #     d['primary']                # entry was automatically removed
# #   File "C:/python314/lib/weakref.py", line 46, in __getitem__
# #     o = self.data[key]()
# # KeyError: 'primary'


# ===========================================================
# 11.7. Tools for Working with Lists
#
# The array module provides an array object that is like a list that stores only homogeneous data and stores it more compactly.
#       typecode "H" > array of numbers stored as two byte unsigned binary numbers
# 
# The 'collections' module provides a 'deque' object that is like a list with faster appends and pops from the left side but slower lookups in the middle.
# 
# the bisect module with functions for manipulating sorted lists:
# 
# The heapq module provides functions for implementing heaps based on regular lists.
# ===========================================================

from array import array
a = array('H', [4000, 10, 700, 22222])
print(sum(a))   # 26932
print(a[1:3])  # array('H', [10, 700])

from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print(d)
print("Handling", d.popleft())  # Handling task1

import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores) # [(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]

from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                               # rearrange the list into heap order
heappush(data, -5)                          # add a new entry
print([heappop(data) for i in range(3)])    # fetch the three smallest entries   > [-5, 0, 1]


# ===========================================================
# 11.8. Decimal Floating-Point Arithmetic
#
# The decimal module offers a Decimal datatype for decimal floating-point arithmetic. 
# helpful for financial applications and other uses which require exact decimal representation,
# ===========================================================

from decimal import *
round(Decimal('0.70') * Decimal('1.05'), 2) # Decimal('0.74')
round(.70 * 1.05, 2)                        # 0.73 < float

Decimal('1.00') % Decimal('.10')    # Decimal('0.00')
1.00 % 0.10                         # 0.09999999999999995 < float

sum([Decimal('0.1')]*10) == Decimal('1.0')                          # True
0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0    # False

getcontext().prec = 5
print(Decimal(1) / Decimal(7))  # Decimal('0.14286')