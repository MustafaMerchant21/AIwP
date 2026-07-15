# ============================================
# Variables
# ============================================

name = "Sachin"
age = 20
height = 176.6

print(name, age, height)


# ============================================
# Input & Output
# ============================================

a = int(input("Enter Number : "))
b = int(input("Enter Number : "))

if a > b:
    print(f"{a} is greater than {b}")
elif b > a:
    print(f"{b} is greater than {a}")
else:
    print("Both numbers are equal")


# ============================================
# Type Casting
# ============================================

x = int("10")
y = float(5)
z = str(25)
flag = bool(1)

print("Integer:", x)
print("Float:", y)
print("String:", z)
print("Boolean:", flag)


# ============================================
# Modules
# ============================================

import math

number = int(input("Enter Number to find out it's factorial : "))

print(f"Factorial of {number} is {math.factorial(number)}")

if number > 0:
    print(f"Log of {number}: {math.log(number):.2f}")

print("Value of Pi:", math.pi)


# ============================================
# Conditional Statements
# ============================================

a = int(input("Enter Number : "))
b = int(input("Enter Number : "))
operator = input("Enter operator (+,-,*,/) : ")

if operator == "+":
    print(f"Addition of {a} + {b} = {a+b}")

elif operator == "-":
    print(f"Subtraction of {a} - {b} = {a-b}")

elif operator == "*":
    print(f"Product of {a} x {b} = {a*b}")

elif operator == "/":
    if b != 0:
        print(f"Division of {a} / {b} = {a/b}")
    else:
        print("Division by zero is not allowed")

else:
    print("Enter valid operator")


# ============================================
# Operators
# ============================================

a = 10
b = 5

# Arithmetic Operators
print("\nArithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Floor Division:", a // b)
print("Exponent:", a ** b)

# Comparison Operators
print("\nComparison Operators")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b :", a > b)
print("a < b :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# Logical Operators
print("\nLogical Operators")
print(a > 0 and b > 0)
print(a > 0 or b < 0)
print(not (a > b))

# Assignment Operators
print("\nAssignment Operators")
x = 10
x += 5
print("x += 5 :", x)

x -= 3
print("x -= 3 :", x)

x *= 2
print("x *= 2 :", x)

x /= 4
print("x /= 4 :", x)


# ============================================
# Math Module Examples
# ============================================

import time

number = int(input("\nEnter Number to find out it's factorial : "))

start = time.time()

print(f"Factorial of {number} is {math.factorial(number)}")

if number > 0:
    print(f"Log of {number}: {math.log(number):.2f}")

print("Value of Pi:", math.pi)

# Distance Formula
print("\nDistance Formula")

x1 = int(input("X1 : "))
x2 = int(input("X2 : "))
y1 = int(input("Y1 : "))
y2 = int(input("Y2 : "))

distance = math.sqrt(
    math.pow((x2 - x1), 2) +
    math.pow((y2 - y1), 2)
)

print(f"Distance = {distance} units")

# Pythagoras Theorem
print("\nPythagoras Theorem")

a = int(input("Enter triangle's a side value : "))
b = int(input("Enter triangle's b side value : "))

hypotenuse = math.sqrt(
    math.pow(a, 2) +
    math.pow(b, 2)
)

print(f"Hypotenuse : {hypotenuse:.2f} = {a}^2 + {b}^2")

now = time.time()

print(f"Time taken : {now - start}")