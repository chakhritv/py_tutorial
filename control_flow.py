x = 10
if x < 0:
    print("Negative")
elif x == 0:
    print("Zero")
else:
    print("Positive")

print()
n = 5
while n > 0:
    print(n, end=' ')
    n -= 1

# For 
## for statement iterates over the items of any sequence (a list or a string)
print()
print(list(range(5)))               #[0, 1, 2, 3, 4]
print(list(range(5,10)))            #[5, 6, 7, 8, 9]
print(list(range(0,10,3)))          #[0, 3, 6, 9]
print(list(range(-10,-100,-30)))    #[-10, -40, -70]


print()
for i in range(2, 10, 2):
    print(i, end=' ')
# 2 4 6 8

print()
for i in range(5):
    if i == 3:
        break      # ออกจาก loop ทันที
    print(i, end=' ')

print()
for i in range(5):
    if i == 3:
        continue   # ข้ามรอบนี้
    print(i, end=' ')

print()
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)

# !!!!! special 
## In a for or while loop the break statement may be paired with an else clause. 
## If the loop finishes without executing the break, the else clause executes.
print()
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2
# 5 is a prime number
# 6 equals 2 * 3
# 7 is a prime number
# 8 equals 2 * 4
# 9 equals 3 * 3


print()
if True:
    pass  # ทำอะไรต่อไม่ได้ แต่ code ยัง compile


def greet(name):
    """ฟังก์ชันแสดงข้อความต้อนรับ"""
    print(f"Hello, {name}!")
greet("Alice")


def power(x, n=2):
    return x ** n
print(power(3))    # 9
print(power(3, 3)) # 27


# Variable scope (ขอบเขตตัวแปร)
x = 10  # global
def func():
    y = 5  # local
    global x
    x = x + 1
func()
print(x)  # 11

# Match
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 402:
            return "Not allowed"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

# point is an (x, y) tuple
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# point is an (x, y) tuple
def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            raise ValueError("Not a point")