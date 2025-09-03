# CONDITIONAL STATEMENTS
"""
if: Executes code if a condition is True
elif: Adds additional conditions after the initial if 
else: Executes code if none of the previous conditions are met
"""
    # Example 1: Checking a condition
"""
    num = -15
    if num > 0:
        print("Positive Number")
    elif num == 0:
        print("Zero")
    else: 
        print ("Negative Number")
"""
    # Example 2: Nested conditions 
"""
    age = 19
    if age > 18:
        if age < 30:
            print("Young Adult")
        else:
            print("Adult")
    else:
        print ("Teen")
"""


    
#LOOPS
"""
forLoop: Iterates over a sequence
whileLoop: Executes as long as a condition is True
"""
    #Loop through a list
"""
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print (fruit)    
"""
    #Loop with range
"""
    for i in range(5): #[0,1,2,3,4]
        print(i)
"""
    #Count down from 5
"""
    count = 5
    while count > 0:
        print(count)
        count -= 1
        
    print("Outside While Loop")
"""
    # Using break adn continue for Control Flow 
        # break: Terminates the loop prematurely when a condition is met
"""
            for i in range(10)
                if i == 5:
                    break
                print (i)
                
            print ("Outside For Loop")
"""
        # continue : Skips the current iteration and proceeds to the next 
"""
            for i in range(10)
                if i % 2 == 0:
                    continue 
                print(i)
"""

#HANDS-ON EXERCISE
    # 1. Check if a Number is Prime
"""
    num = int(input("Enter a number: "))

    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print (f"{num} is not a prime number")
                break
        else:
            print (f"{num} is a prime number")
    else:
        print (f"{num} is not a prime number")
"""
    # 2. Create a Menu-Driven Calculator
""" 
    def add(a, b):
        return a + b     
    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide (a, b):
        if b!=0:
            return a / b 
        else: 
            return "Division by zero is not allowed"
        
    while True:
        print("\nMenu:")
        print("1. Addition")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Division")    
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "5":
            print("Exiting Program.")
            break
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", subtract(num1, num2))
        else:
            print("Invalid choice, Please try again")
"""        
        
    # 3. Create program to calculate the factorial of a number using a while loop
        
def calculate_factorial(number):
    if not isinstance(number, int) or number < 0:
        return "Factorial is not defined for negative or non-integer numbers."
    if number == 0:
        return 1

    result = 1
    current_number = number

    while current_number > 0:
        result *= current_number
        current_number -= 1        
    return result

try:
    user_input = int(input("Enter a non-negative integer to calculate its factorial: "))
    
    factorial_result = calculate_factorial(user_input)
    
    if isinstance(factorial_result, int):
        print(f"The factorial of {user_input} is: {factorial_result}")
    else:
        print(factorial_result)
        
except ValueError:
    print("Invalid input. Please enter a valid integer.")
        
        
    
#ARITHMETHIC OPERATORS IN PYTHON 
"""
        `+`         : Addition
        `-`         : Subtraction
        `*`         : Multiplication
        `/`         : Division (returns a float)
        `//`        : Floor division (returns an integer, discarding any fractional part)
        `%`         : Modulus (returns the remainder of division)
        `**`        : Exponentiation (power)
        `@`         : Matrix multiplication (used in libraries like NumPy)
        `num**0.5`  : Square root
        `int()`     : Rounds it down to a whole number
    Also, note the comparison operators:
        `==`        : Equal to
        `!=`        : Not equal to
        `>`         : Greater than
        `<`         : Less than
        `>=`        : Greater than or equal to
        `<=`        : Less than or equal to
        `*=`        : Multiplication to current number on loop (applies to all basic arithmathic operation)
    And assignment operators:
        `=`         : Assignment
        `+=`        : Add and assign
        `-=`        : Subtract and assign
        `*=`        : Multiply and assign
        `/=`        : Divide and assign
        `//=`       : Floor divide and assign
        `%=`        : Modulus and assign
        `**=`       : Exponentiate and assign
    Additional:
        `s[::-1]`   : Slicing / reverses the string by stepping backward through it
"""
