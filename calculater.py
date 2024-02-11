# this calculator can perform " +-*/ square squreRoot "

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "denominator couldn't be zero"
    else:
        return x / y

def square(x):
    return x ** 2

def squareRoot(x):
    if x < 0:
        return "Error! Cannot calculate square root of a negative number."
    else:
        return math.sqrt(x)


print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square")
print("6. Square Root")

choice = int(input("\nEnter choice:: "))

if choice in (1, 2, 3, 4):
    num1 = int(input("enter first number"))
    num2 = int(input("enter second number"))
    
    if choice == 1:
        result = add(num1, num2)
        print('Result= ',result)
        
    if choice == 2:
        result = subtract(num1, num2)
        print('Result= ', result)  
        
    if choice == 3:
        result = multiply(num1, num2)
        print('Result= ',result)
    
    if choice == 4:
        result = divide(num1, num2)
        print('Result= ',result)
    

elif choice in (5, 6):
    num = int(input("enter number"))
    
    if choice == 5:
        result = square(num)
        print('Result= ', result)
    
    if choice == 6:
       result = squareRoot(num)
       print('Result= ', result)
       
else:
    print("invalid choice")
