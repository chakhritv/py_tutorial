x = 10
y = 3.5
name = "Alice"
a, b = 1, 2

print(x)
print(y)
print(name)
print(a)
print(b)

word = "Python"
print(word[0])   # 'P'
print(word[-1])  # 'n'
print(word[0:2])  # 'Py'   (เริ่มที่ index 0 ถึง 2-1)
print(word[:3])   # 'Pyt'
print(word[2:])   # 'thon'

fruits = ['apple', 'banana', 'cherry']
print(fruits[0])         # apple
fruits.append('orange')  # เพิ่มข้อมูล
print(fruits)
fruits[1] = 'mango'      # แก้ค่า
print(fruits)

nums = [0, 1, 2, 3, 4, 5]
print(nums[2:5])  # [2, 3, 4]
nested = [fruits, nums]
print(nested[0][1])  # mango

len("Python")    # 6
len([1, 2, 3])   # 3

for x in [1, 2, 3]:
    print(x)

if 5 > 3:
    print("Yes")

a = 0.1 + 0.2
print(a)  
# Output: 0.30000000000000004

from decimal import Decimal

a = Decimal('0.1') + Decimal('0.2')
print(a)  
# Output: 0.3