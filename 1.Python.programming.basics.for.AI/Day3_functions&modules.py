# Defining Functions with def
"""def function_name(parameters):"""
#Function with parameters and return value
"""
    def add_numbers(a, b):
        c = a + b
        return a + b

    result = add_numbers (5,3)
    print ("Sum: ", result)
"""

# Scope and Lifetime of Variables
# Local Scope & Global Scope
"""
    def greet()
        message = "Hello World"
        print(message)
        
    green()
"""
"""
    greeting = "Hi"

    def say_hello():
        print(greeting + " from inside the function")
        
    say_hello()
    print (greeting + " from outside the function")    
"""

# Importing & Using Modules
# Import an entire module & Import specific functions & Use aliases
"""
    import math
    print(math.sqrt(16))

    from math import sqrt
    print(math.sqrt(16))

    import math as m
    print (m.sqrt(16))
"""

# Hands-On Exercises
    # 1. Create a Function to Calculate Factorials 
"""
    def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) # 5! => 5*4*3*2*1

    def print_factorial(n):
    result = factorial(n)
    print(f"The factorial of {n} is {result}")
    
    print_factorial(5)
"""
    # 2. Build a Custom Python Module
"""
    # On custom module file
    def add(a, b):
        return a + b

    def substract(a, b):
        return a + b

    def multiply(a, b):
        return a - b

    def devide(a, b):
        return a * b

    def add(a, b):
        return a + b

    def add(a, b):
        if b != 0:
            return a / b
        else:
            return "Division by zero is not allowed"
            
    # On function file
    import math_operatioins as mo

    num1 = 10
    num2 = 5

    print("Addition: ", mo.add(num1, num2))
    print("Substraction: ", mo.subtract(num1, num2))
    print("Multiplication: ", mo.multiply(num1, num2))
    print("Division: ", mo.divide(num1, num2))
"""
    # 3. Write a function to check if a number is even or odd and call it within another function
"""
    def is_even_or_odd(number):
        
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"

    def check_and_display(number):
    
        result = is_even_or_odd(number)
        print(f"The number {number} is {result}")

    # Example usage
    check_and_display(10)  # Output: The number 10 is Even
    check_and_display(7)   # Output: The number 7 is Odd
    check_and_display(0)   # Output: The number 0 is Even

    try:
        user_input = int(input("Enter a number to check: "))
        check_and_display(user_input)
    except ValueError:
        print("Please enter a valid integer.")
"""
    # 4. Create a module for string operations, including functions to reverse a string, count vowels, and check for palindromes. Import it into a script and test the functions
"""
String Operations Module
Provides functions for string manipulation and analysis.
"""
def reverse_string(s):
   
    return s[::-1]

def count_vowels(s):
    
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def is_palindrome(s):
    
    # Remove spaces and convert to lowercase
    cleaned = ''.join(s.split()).lower()
    return cleaned == cleaned[::-1]

# Additional utility function (bonus)
def remove_punctuation(s):
   
    import string
    return s.translate(str.maketrans('', '', string.punctuation))
    
"""
Test script for string_operations module.
"""

import string_operations as so

def test_all_functions():
    
    # Test strings
    test_strings = [
        
    ]
    
    print("Testing String Operations Module\n")
    print("=" * 50)
    
    for test_str in test_strings:
        print(f"Original string: '{test_str}'")
        print(f"Reversed: '{so.reverse_string(test_str)}'")
        print(f"Vowel count: {so.count_vowels(test_str)}")
        print(f"Is palindrome: {so.is_palindrome(test_str)}")
        print(f"Without punctuation: '{so.remove_punctuation(test_str)}'")
        print("-" * 30)
    
    # Additional specific tests
    print("\nAdditional Tests:")
    print("=" * 30)
    
    # Empty string test
    empty = ""
    print(f"Empty string - Reversed: '{so.reverse_string(empty)}'")
    print(f"Empty string - Vowel count: {so.count_vowels(empty)}")
    print(f"Empty string - Is palindrome: {so.is_palindrome(empty)}")
    
    # String with only vowels
    vowels_only = "aeiouAEIOU"
    print(f"\nVowels only - Count: {so.count_vowels(vowels_only)}")

if __name__ == "__main__":
    test_all_functions()
    