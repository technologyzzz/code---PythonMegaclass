# Defining Functions with def
    # A Python function is a self-contained block of code designed to perform a specific task. Functions are fundamental building blocks in Python programming, offering several benefits: 
        # Code Reusability: Functions allow you to encapsulate a set of instructions that can be executed multiple times throughout your program without rewriting the same code.
        # Modularity: They help in breaking down complex programs into smaller, more manageable units, improving code organization and readability.
        # Abstraction: Functions allow you to hide the implementation details of a specific task, presenting a clean interface for interaction.
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
    # In Python, scope refers to the region within a program where a variable or name is accessible and can be referenced. It dictates the visibility and lifetime of identifiers, ensuring that names are correctly resolved and preventing unintended name collisions. Python's scope resolution follows the LEGB rule, which stands for:
        #Local (L): This is the innermost scope, typically within a function or a lambda expression. Variables defined within a function are local to that function and are only accessible from within its body.
        # Enclosing (E): This scope applies to nested functions. If a function is defined inside another function, the inner function can access variables from the outer (enclosing) function's scope, even if those variables are not passed as arguments.
        # Global (G): This scope encompasses the entire module or script. Variables defined at the top level of a Python file (outside of any function or class) are considered global and can be accessed from anywhere within that module.
        # Built-in (B): This is the broadest scope, containing Python's pre-defined names like built-in functions (e.g., print(), len()) and exceptions. These names are always available without explicit definition.

# Local Scope & Global Scope
"""
    def greet():
        message = "Hello World"
        print(message)
        
    greet()
"""
"""
    greeting = "Hi"

    def say_hello():
        print(greeting + " from inside the function")
        
    say_hello()
    print (greeting + " from outside the function")    
"""

# Module
    # A Python module is a file containing Python definitions and statements. Essentially, it is a .py file that can define functions, classes, and variables, and can also include runnable code. 
    # Modules serve as a mechanism for organizing related code into logical, reusable units. This modularity promotes code reusability, improves code readability, and simplifies the management of larger programs by breaking them down into smaller, more manageable components.
    # When a module is imported into another Python script or interactive session using the import statement, its contents (functions, classes, variables) become accessible within the importing scope. This allows developers to leverage pre-written code without having to rewrite it, fostering efficient and organized programming practices.

# Importing & Using Modules
# Import an entire module & Import specific functions & Use aliases
"""
    import math
    print(math.sqrt(16))

    from math import sqrt
    print(sqrt(16))

    import math as m
    print(m.sqrt(16))
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
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Division by zero is not allowed"
            
    # On function file
    import math_operations as mo

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
# String Operations Module. Provides functions for string manipulation and analysis.
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
        
# Test script for string_operations module.

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
"""    