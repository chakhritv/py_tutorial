# ===========================================================
# 8. Errors and Exceptions
#
# ===========================================================


# ===========================================================
# 8.1 Syntax Errors
# 
# Syntax errors, also known as parsing errors
# ===========================================================

# while True print('Hello world')
#   File "<stdin>", line 1
#     while True print('Hello world')
#                ^^^^^
# SyntaxError: invalid syntax


# ===========================================================
# 8.2 Exceptions
# 
# Errors detected during execution are called exceptions
# ===========================================================

# 10 * (1/0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     10 * (1/0)
#           ~^~
# ZeroDivisionError: division by zero
# 4 + spam*3
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     4 + spam*3
#         ^^^^
# NameError: name 'spam' is not defined
# '2' + 2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     '2' + 2
#     ~~~~^~~
# TypeError: can only concatenate str (not "int") to str


# ===========================================================
# 8.3 Handling Exceptions
# 
# Errors detected during execution are called exceptions
#
# BaseException is the common base class of all exceptions. 
# One of its subclasses, Exception, is the base class of all the non-fatal exceptions. 
# Exceptions which are not subclasses of Exception are not typically handled, 
# because they are used to indicate that the program should terminate.
# ===========================================================

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")


# # การจับหลาย Exception พร้อมกัน
# try:
#     risky_operation()
# except (ValueError, TypeError):
#     print("เกิดข้อผิดพลาดของข้อมูล")


# # Best pactise  catch exceptio from smallest class to super class
# class B(Exception): # B inherite from Exception
#     pass
# class C(B):         # C inherite from B
#     pass
# class D(C):         # D inherite from C
#     pass
# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")
# # B
# # C
# # D



# # เก็บข้อความ error ไว้ใช้งาน
# try:
#     10 / 0
# except ZeroDivisionError as e:
#     print("Error:", e)


# # The except clause may specify a variable after the exception name.
# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))    # the exception type
#     print(inst.args)     # arguments stored in .args
#     print(inst)          # __str__ allows args to be printed directly, but may be overridden in exception subclasses
#     x, y = inst.args     # unpack args
#     print('x =', x)
#     print('y =', y)
# # <class 'Exception'>
# # ('spam', 'eggs')
# # ('spam', 'eggs')
# # x = spam
# # y = eggs


# # useful for code that must be executed if the try clause does not raise an exception.
# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except OSError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()


# ===========================================================
# 8.4 Raising Exceptions
# 
# ===========================================================

# raise NameError('HiThere')
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# #     raise NameError('HiThere')
# # NameError: HiThere


# ===========================================================
# 8.5 Exception Chaining
# 
# ===========================================================

# def func():
#     raise ConnectionError
# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError('Failed to open database') from exc
# # Traceback (most recent call last):
# #   File "<stdin>", line 2, in <module>
# #     func()
# #     ~~~~^^
# #   File "<stdin>", line 2, in func
# # ConnectionError
# # The above exception was the direct cause of the following exception:
# # Traceback (most recent call last):
# #   File "<stdin>", line 4, in <module>
# #     raise RuntimeError('Failed to open database') from exc
# # RuntimeError: Failed to open database


# # It also allows disabling automatic exception chaining using the from None
# try:
#     open('database.sqlite')
# except OSError:
#     raise RuntimeError from None
# # Traceback (most recent call last):
# #   File "<stdin>", line 4, in <module>
# #     raise RuntimeError from None
# # RuntimeError


# ===========================================================
# 8.6 User-defined Exceptions
# 
# ===========================================================


# ===========================================================
# 8.7 Defining Clean-up Actions
# 
# If a finally clause is present, 
# the finally clause will execute as the last task > before the try statement completes.
# if an exception occur during try statement and handled by except statement 
#   yes > finally execute after except statement
#   no  > the exception is re-raised after finally statement
# ===========================================================

# def bool_return():
#     try:
#         return True
#     finally:
#         return False
# print(bool_return())    # False

# more complicated
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
divide(2, 1)
# result is 2.0
# executing finally clause
divide(2, 0)
# division by zero!
# executing finally clause
divide("2", "1")
# executing finally clause
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     divide("2", "1")
#     ~~~~~~^^^^^^^^^^
#   File "<stdin>", line 3, in divide
#     result = x / y
#              ~~^~~
# TypeError: unsupported operand type(s) for /: 'str' and 'str'


# ===========================================================
# 8.8 Predefined Clean-up Actions
# 
# Some objects define standard clean-up actions to be undertaken when the object is no longer needed
# The 'with' statement allows objects like files to be used in a way that 
# ensures they are always cleaned up promptly and correctly.
# ===========================================================

# with open("myfile.txt") as f:
#     for line in f:
#         print(line, end="")


# ===========================================================
# 8.9 Raising and Handling Multiple Unrelated Exceptions
# 
# ===========================================================

# def f():
#     excs = [OSError('error 1'), SystemError('error 2')]
#     raise ExceptionGroup('there were problems', excs)
# f()
# #   + Exception Group Traceback (most recent call last):
# #   |   File "<stdin>", line 1, in <module>
# #   |     f()
# #   |     ~^^
# #   |   File "<stdin>", line 3, in f
# #   |     raise ExceptionGroup('there were problems', excs)
# #   | ExceptionGroup: there were problems (2 sub-exceptions)
# #   +-+---------------- 1 ----------------
# #     | OSError: error 1
# #     +---------------- 2 ----------------
# #     | SystemError: error 2
# #     +------------------------------------

# try:
#     f()
# except Exception as e:
#     print(f'caught {type(e)}: e')
# # caught <class 'ExceptionGroup'>: e


# # By using except* instead of except, we can selectively handle only the exceptions in the group that match a certain type.
# def f():
#     raise ExceptionGroup(
#         "group1",
#         [
#             OSError(1),
#             SystemError(2),
#             ExceptionGroup(
#                 "group2",
#                 [
#                     OSError(3),
#                     RecursionError(4)
#                 ]
#             )
#         ]
#     )
# try:
#     f()
# except* OSError as e:
#     print("There were OSErrors")
# except* SystemError as e:
#     print("There were SystemErrors")
# # There were OSErrors
# # There were SystemErrors
# #   + Exception Group Traceback (most recent call last):
# #   |   File "<stdin>", line 2, in <module>
# #   |     f()
# #   |     ~^^
# #   |   File "<stdin>", line 2, in f
# #   |     raise ExceptionGroup(
# #   |     ...<12 lines>...
# #   |     )
# #   | ExceptionGroup: group1 (1 sub-exception)
# #   +-+---------------- 1 ----------------
# #     | ExceptionGroup: group2 (1 sub-exception)
# #     +-+---------------- 1 ----------------
# #       | RecursionError: 4
# #       +------------------------------------


# ===========================================================
# 8.10 Enriching Exceptions with Notes
# 
# ===========================================================

# try:
#     raise TypeError('bad type')
# except Exception as e:
#     e.add_note('Add some information')
#     e.add_note('Add some more information')
#     raise
# # Traceback (most recent call last):
# #   File "<stdin>", line 2, in <module>
# #     raise TypeError('bad type')
# # TypeError: bad type
# # Add some information
# # Add some more information

# # For example, 
# # when collecting exceptions into an exception group, 
# # we may want to add context information for the individual errors.
# def f():
#     raise OSError('operation failed')
# excs = []
# for i in range(3):
#     try:
#         f()
#     except Exception as e:
#         e.add_note(f'Happened in Iteration {i+1}')
#         excs.append(e)
# raise ExceptionGroup('We have some problems', excs)
# #   + Exception Group Traceback (most recent call last):
# #   |   File "<stdin>", line 1, in <module>
# #   |     raise ExceptionGroup('We have some problems', excs)
# #   | ExceptionGroup: We have some problems (3 sub-exceptions)
# #   +-+---------------- 1 ----------------
# #     | Traceback (most recent call last):
# #     |   File "<stdin>", line 3, in <module>
# #     |     f()
# #     |     ~^^
# #     |   File "<stdin>", line 2, in f
# #     |     raise OSError('operation failed')
# #     | OSError: operation failed
# #     | Happened in Iteration 1
# #     +---------------- 2 ----------------
# #     | Traceback (most recent call last):
# #     |   File "<stdin>", line 3, in <module>
# #     |     f()
# #     |     ~^^
# #     |   File "<stdin>", line 2, in f
# #     |     raise OSError('operation failed')
# #     | OSError: operation failed
# #     | Happened in Iteration 2
# #     +---------------- 3 ----------------
# #     | Traceback (most recent call last):
# #     |   File "<stdin>", line 3, in <module>
# #     |     f()
# #     |     ~^^
# #     |   File "<stdin>", line 2, in f
# #     |     raise OSError('operation failed')
# #     | OSError: operation failed
# #     | Happened in Iteration 3
# #     +------------------------------------