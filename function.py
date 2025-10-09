# Defining Functions

def fib(n):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)


# Default Argument Values
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# !!!! Default Arg values
## Important warning: The default value is evaluated only once. 
## This makes a difference when the default is a mutable object.
i = 5
def f(arg=i):
    print(arg)
i = 6
f()
#will print 5.


print()
# !!!! subsequent calls shared
def g(a, L=[]):
    L.append(a)
    return L
print(g(1))
print(g(2))
print(g(3))
# [1]
# [1, 2]
# [1, 2, 3]

print()
def h(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(h(1))
print(h(2))
print(h(3))


# Keyword Arguments & Position Arguments
print()
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    print("-" * 40)
    print(">> args")
    print("-" * 40)
    for arg in arguments:
        print(arg)
    print("-" * 40)    
    print(">> keywords")
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

print()
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

#  lambda expression > return a function
print()
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)   # f is a function
print(f)
print(f(0))
print(f(10))

print()
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)


# Documentation Strings
print()
def my_function():
    """Do nothing, but document it.
    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)


# Function Annotations
print()
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs
print(f('spam'))