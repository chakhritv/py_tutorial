# ===========================================================
# 6. Modules
#
# A module is a file containing Python definitions and statements.
# Within a module, the module’s name (as a string) is available as the value of the global variable __name__.
# ===========================================================


import module.fibo
module.fibo.fib(150)            #  0 1 1 2 3 5 8 13 21 34 55 89 144 

print(module.fibo.__name__)     # 'module.fibo'

## assign function into 'x' variable
x = module.fibo.fib
x(120)                          # 0 1 1 2 3 5 8 13 21 34 55 89


# ===========================================================
# 6.1 More on Modules
#
# A module can contain executable statements as well as function definitions. 
# These statements are intended to initialize the module. 
# They are executed only the first time the module name is encountered in an import statement.
#
# !! each module is only imported once per interpreter session. !!
# ===========================================================

from module.fibo import *
fib(500)                        # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

from module.fibo import fib, fib2
fib(500)                        # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

# import with alias
from module.fibo import fib as fibonacci
fibonacci(500)                  # 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377


# ===========================================================
# 6.1.1 Executing modules as scripts
#
# ===========================================================

# see this code in "fibo.py"
# if __name__ == "__main__":
#     import sys
#     fib(int(sys.argv[1]))
# ถ้าเรียก python .\module\fibo.py 1000 → โค้ดใน if __name__ == "__main__": จะทำงาน


# ===========================================================
# 6.1.2 The Module Search Path
#
# Python จะค้นหา module ตาม sys.path (enviroment)
# 
# ===========================================================

# ถ้าอยากเพิ่ม path ชั่วคราวใน runtime:
import sys
print(sys.path)
sys.path.append('C:\\My Documents\\chakhritk\\Veng Learning\\py_workspace\\module')
print(sys.path)

import fibo
print(fibo.fib2(50))


# ===========================================================
# 6.1.3 “Compiled” Python files
#
# Python caches the compiled version of each module in the __pycache__ directory under the name module.version.pyc
# For example, in CPython release 3.3 the compiled version of spam.py would be cached as __pycache__/spam.cpython-33.pyc.
# ===========================================================


# ===========================================================
# 6.2 Standard Modules
#
# Python comes with a library of standard modules
# Some modules are built into the interpreter. 
# ===========================================================
import sys
print(sys.platform)
print(sys.version)


# ===========================================================
# 6.3 The dir() Function
#
# Python comes with a library of standard modules
# Some modules are built into the interpreter. 
# ===========================================================
print(dir(fibo))
print(dir(sys))
print(dir())


# ===========================================================
# 6.4 Packages
#
# Packages are a way of structuring Python’s module namespace by using “dotted module names”
# Package = folder ที่มีไฟล์ __init__.py     ใช้จัดกลุ่ม module หลายไฟล์ให้เป็นหมวดหมู่
#
# sound/
#     __init__.py
#     effects/
#         __init__.py
#         echo.py
#         surround.py
#     filters/
#         __init__.py
#         equalizer.py
#
# __init__.py
# บอก Python ว่าโฟลเดอร์นี้เป็น package
# สามารถใส่โค้ด init ได้ เช่น define __all__ เพื่อกำหนดว่า from package import * จะดึง module ไหนบ้าง
# __all__ = ["echo", "surround"]
# ===========================================================

