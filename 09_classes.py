# ===========================================================
# 9. Classes
#
# class
#   - attribute
#   - method
# ===========================================================


# ===========================================================
# 9.1 A Word About Names and Objects
#
# ทุกอย่างใน Python คือ object เช่น ตัวเลข, list, ฟังก์ชัน, คลาส
# ตัวแปร (variable) คือ ชื่อ (name) ที่อ้างอิงถึง object
# ตัวแปรหลายตัวสามารถอ้างถึง object เดียวกันได้ เช่น
# ===========================================================

a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4]


# ===========================================================
# 9.2 Python Scopes and Namespaces
#
# Namespace คือการจับคู่ชื่อ (Name) กับวัตถุ (Object) เป็นเหมือน พจนานุกรม (Dictionary)
# เช่น คุณสามารถมีฟังก์ชันชื่อ maximize ใน Module A และ Module B ได้พร้อมกัน 
#       แต่เมื่อเรียกใช้ต้องระบุชื่อ Module ด้วย (เช่น ModuleA.maximize และ ModuleB.maximize)
# 
# Scope คือ ขอบเขตข้อความ (Textual Region) ของโปรแกรม Python 
#       คือ "บริเวณที่คุณสามารถใช้ชื่อตัวแปรได้โดยไม่ต้องระบุที่มา"
#   Local (ในสุด): ชื่อที่กำหนดในฟังก์ชันปัจจุบัน
#   Enclosing (ของฟังก์ชันที่ครอบ): ชื่อที่กำหนดในฟังก์ชันที่อยู่ด้านนอก (สำหรับฟังก์ชันที่ซ้อนกัน)
#   Global (ถัดไป): ชื่อส่วนกลางของโมดูลปัจจุบัน
#   Built-in (นอกสุด): ชื่อมาตรฐานที่มาพร้อมกับ Python
#
# ลำดับการค้นหาชื่อใน Python เรียกว่า LEGB rule:
#   Local → Enclosing → Global → Built-in
# ===========================================================


# ===========================================================
# 9.2.1 Scopes and Namespaces Example
#
# คำสั่ง global: ใช้เพื่อระบุว่าการอ้างอิงและการกำหนดค่าทั้งหมดควรทำกับ Global Scope ของโมดูล
# คำสั่ง nonlocal: ใช้เพื่อระบุว่าตัวแปรอยู่ใน Enclosing Scope (ของฟังก์ชันที่ครอบอยู่)
# ===========================================================
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)
scope_test()
print("In global scope:", spam)
# After local assignment: test spam
# After nonlocal assignment: nonlocal spam
# After global assignment: nonlocal spam
# In global scope: global spam


# ===========================================================
# 9.3 A First Look at Classes
#
# คลาสคือแม่แบบ (blueprint) สำหรับสร้าง object (instance)
# ===========================================================


# ===========================================================
# 9.3.1 Class Definition Syntax
#
# class ClassName:
    # <statement-1>
    # .
    # .
    # .
    # <statement-N>
# ===========================================================


# ===========================================================
# 9.3.2 Class Objects
#
# ===========================================================
print()
print()

# class MyClass:
#     """A simple example class"""    # __doc__ attribute is assigned
#     i = 12345
#     def f(self):
#         return 'hello world'
# x = MyClass()   # create new instance, class automatically invoke __init__()
# print(x)    # <__main__.MyClass object at 0x0000015715216F90>


# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
# x = Complex(3.0, -4.5)
# print(x.r, x.i) # 3.0 -4.5


# ===========================================================
# 9.3.3. Instance Objects
#
# มี 2 ส่วนหลัก  attribute + method
# attribute ไม่จำเป็นต้องประกาศล่วงหน้า สร้างขณะไหนก็ได้เมื่อถูก assign 
# method คือ function ของ instance นั้นๆ ที่ถูกกำหนดไว้ใน class 
# ===========================================================

# class MyClass:
#     """A simple example class"""    # __doc__ attribute is assigned
#     i = 12345
#     def f(self):
#         return 'hello world'
# x = MyClass()      
# x.counter = 1     # x สร้าง attribute counter ขึ้นมาเองขณะ runtime ได้เลย
# while x.counter < 10:
#     x.counter = x.counter * 2
# print(x.counter)    # 16
# del x.counter
# # print(x.counter)    # AttributeError: 'Complex' object has no attribute 'counter'


# ===========================================================
# 9.3.4. Method Objects
#
# ===========================================================

# class MyClass:
#     """A simple example class"""    # __doc__ attribute is assigned
#     i = 12345
#     def f(self):
#         return 'hello world'
# x = MyClass()
# xf = x.f    # x.f is a method object so you can assign variable to its
# print(xf()) # xf() = x.f() = MyClass.f(x)


# ===========================================================
# 9.3.5. Class and Instance Variables
#
# ===========================================================

class Dog:
    kind = 'canine'         # class variable shared by all instances
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)                  # shared by all dogs > 'canine'
print(e.kind)                  # shared by all dogs > 'canine'
print(d.name)                  # unique to d > 'Fido'
print(e.name)                  # unique to e > 'Buddy'

class Warehouse:
   purpose = 'storage'
   region = 'west'
w1 = Warehouse()
print(w1.purpose, w1.region)    # storage west
w2 = Warehouse()
w2.region = 'east'              # w2 ไม่เคยมี region เป็นของมันเอง จนถึงบรรทัดนี้  พอมีการ assign w2 จึงสร้าง region ของมันเองขึ้นมา
print(w2.purpose, w2.region)    # storage east > east ในที่นี้คือ w2.region จริงๆ มันไม่ได้กลับไปเอาที่ class แล้ว
print(w1.purpose, w1.region)    # storage west > west ในที่นี้คือ w1.region ไม่มี มันจึงกลับไปเอาที่ class มา


# ===========================================================
# 9.4. Random Remarks
#
# ลำดับความสำคัญในการค้นหาแอตทริบิวต์ 
#   instance attribute
#   class attribute > super class > . . .
# ไม่มีการบังคับซ่อนข้อมูล (No Enforced Data Hiding) 
# การเรียกใช้เมธอดภายใน (Calling Methods Internally) จะใช้ self.method() เสมอ
# self เป็นเพียงข้อตกลง: อาร์กิวเมนต์แรกของเมธอดมักจะถูกเรียกว่า self ตามข้อตกลง แต่ชื่อนี้ ไม่มีความหมายพิเศษ ทางภาษาต่อ Python
# ค่าทุกค่าใน Python เป็น Object  >> สามารถเข้าถึงได้ผ่าน object.__class__
# ===========================================================

class Bag:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)

# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)
class C:
    f = f1                      # f is a class method 
    def g(self):                # g is a class method 
        return 'hello world'
    h = g                      # h is a class method 


# ===========================================================
# 9.5. Inheritance
#
# Inheritance คือการสร้างคลาสใหม่ (Derived Class หรือคลาสลูก) 
# โดยรับคุณสมบัติ (แอตทริบิวต์และเมธอด) จากคลาสที่มีอยู่แล้ว (Base Class หรือคลาสแม่)
#
# การแทนที่: คลาสลูกสามารถ แทนที่ (Override) เมธอดที่มีชื่อเดียวกันกับเมธอดในคลาสแม่ได้
# เมธอดทั้งหมดใน Python ทำงานคล้ายกับเมธอดเสมือน (Virtual Methods)
# การเรียกเมธอดแม่โดยตรง BaseClassName.methodname(self, arguments)
#
# isinstance(obj, ClassName): ใช้ตรวจสอบว่าวัตถุ obj เป็นอินสแตนซ์ของ ClassName หรือเป็นอินสแตนซ์ของคลาสใด ๆ ที่ สืบทอดมาจาก ClassName หรือไม่
# issubclass(DerivedClass, BaseClass): ใช้ตรวจสอบว่า DerivedClass เป็น คลาสลูก (Subclass) ของ BaseClass หรือไม่
# ===========================================================


# ===========================================================
# 9.5.1. Multiple Inheritance
#
# class DerivedClassName(Base1, Base2, Base3):
#
# ลำดับการค้นหาแอตทริบิวต์ (Method Resolution Order - MRO) > Depth-First, Left-to-Right
#     DerivedClassName
#     Base1 > super class
#     Base2 > super class
#     ...
#     Basex
# ===========================================================


# ===========================================================
# 9.6. Private Variables
#
# !!! Python ไม่มีตัวแปรอินสแตนซ์ที่ห้ามเข้าถึงจากภายนอก 
# แต่มี ข้อตกลง (Convention) ที่โปรแกรมเมอร์ส่วนใหญ่ใช้
# ชื่อที่ขึ้นต้นด้วยขีดล่างเดี่ยว (_spam): ควรถูกถือว่าเป็นส่วนที่ ไม่เป็นสาธารณะ (Non-public)
#
# ชื่อชนกัน (Name Clashes) ระหว่างชื่อที่กำหนดในคลาสแม่กับชื่อที่อาจถูกกำหนดในคลาสลูก (Subclasses) Python มีกลไกจำกัดที่เรียกว่า Name Mangling
# ตัวระบุใด ๆ ที่อยู่ในรูปแบบ __spam เมื่อโค้ดถูกคอมไพล์ 
# ชื่อนั้นจะถูกแทนที่ด้วยข้อความใหม่เป็น _ClassName__spam โดย ClassName คือชื่อคลาสปัจจุบัน (ที่ตัดขีดล่างนำหน้าออก)
# ===========================================================


# ===========================================================
# 9.7. Odds and Ends
#
# การใช้ dataclass สำหรับโครงสร้างข้อมูล (Idiomatic) ใน Python คือการใช้ @dataclass
#   ประโยชน์: การใช้ @dataclass จะช่วยสร้างเมธอดพื้นฐานที่จำเป็น (เช่น __init__, __repr__) ให้โดยอัตโนมัติ
# ===========================================================
from dataclasses import dataclass
@dataclass
class Employee:
    name: str
    dept: str
    salary: int
john = Employee('john', 'computer lab', 1000)
print(john.dept)       # 'computer lab'
print(john.salary)     # 1000


# ===========================================================
# 9.8. Iterators
#
# Behind the scenes, the for statement calls iter() on the container object.
#   The function returns an iterator object that defines the method __next__()
#   When there are no more elements, __next__() raises a StopIteration
# ===========================================================

for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("workfile.txt"):
    print(line, end='')
print()
print()
s = 'abc'
it = iter(s)
print(it)   # <str_iterator object at 0x10c90e650>
print(next(it))    # 'a'
print(next(it))    # 'b'
print(next(it))    # 'c'
# next(it)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     next(it)
# StopIteration

# Example Implement 
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
rev = Reverse('spam')
print(iter(rev))   # <__main__.Reverse object at 0x00A1DB50>
for char in rev:
    print(char)
# m
# a
# p
# s


# ===========================================================
# 9.9. Generators
#
# Generators are a simple and powerful tool for creating iterators.
#   They are written like regular functions but use the 'yield' statement whenever they want to return data.
#   Each time next() is called on it, the generator resumes
# ===========================================================

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
for char in reverse('golf'):
    print(char)
# f
# l
# o
# g


# ===========================================================
# 9.10. Generator Expressions
#
# ===========================================================

# sum(i*i for i in range(10))                 # sum of squares 285

# xvec = [10, 20, 30]
# yvec = [7, 5, 3]
# sum(x*y for x,y in zip(xvec, yvec))         # dot product 260

# unique_words = set(word for line in page  for word in line.split())

# valedictorian = max((student.gpa, student.name) for student in graduates)

# data = 'golf'
# list(data[i] for i in range(len(data)-1, -1, -1))
# ['f', 'l', 'o', 'g']