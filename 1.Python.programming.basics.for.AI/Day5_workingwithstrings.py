# 1. String Manipulation
    # String manipulation is the process of manipulating and analyzing strings. 
    # It involves modification and parsing of strings to use and change their data. 
    # Python has several built-in functions in the standard library to help programmers manipulate strings in different ways.
"""    
        #concatenation 
    first = "Hello"
    second = "World"
    result = first + " " + second
    print(result)

        #slicing
    text = "Python Programming"
    print(text[0:6]) #print first 6word
    print(text[-11:]) #print last 11word

        #formatting
    name = "Alice"
    age = 25
    print(f"My name is {name} and I am {age} years old.") #f-string
"""
# 2. Common String Methods
    # Python has a set of built-in methods that you can use on strings.
    # All string methods returns new values. They do not change the original string.
"""
        #split()
    sentence = "Python, is, fun"
    words = sentence.split(",") #split by (,)
    print(words)

        #join()
    new_sentence = "|".join(words)
    print(new_sentence)
            
        #replace()
    text = "I love Java"
    updated_text = text.replace("Java", "Python")
    print(updated_text)

        #strip()
    messy = "     Hello, World    "
    print(messy)
    cleaned_text = messy.strip()
    print(cleaned_text)
"""
# 3. Regular Expressions for Pattern Matching (regex)
    # Regular expressions, also called regex, are descriptions of a pattern of text. 
    # It can detect the presence or absence of a text by matching it with a particular pattern and also can split a pattern into one or more sub-patterns.

#common functions
"""
    import re #using re module
    re.search #pattern,string

    text = "Contact me at 123-456-7890"
    digits = re.findall(r"\d+", text) #functions to split integer
    print(digits)

    updated_text = re.sub(r"\d+", "X", text) #functions to 'censore integer / change all to X"
    print(updated_text)
"""

# HANDS-ON EXERCISES

    # 1. Create a Text Cleaner
"""
    def clean_text(text):
        text = re.sub()r"[^\w\s]", "", text) #functions to 'clear all punctuations'
        text = " ".join(text.split()) #function to 'remove extra spaces'
        return text.lower(0) #function to 'lowercase'

    input_text = " Hello, World. !!! Welcome to Python, Programming..."
    cleaned_text = clean_text(input_text) 
    print("Cleaned Text: ", cleaned_text)
"""

    # 2. Check if a String is a Palindrome
    
def is_palindrome(text):
    text = "".join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]

input_text = input("Enter a string: ")
if is_palindrome(input_text):
    print(f'"{input_text}" is a palindrome,')
else:
    print(f':{input_text}" is not a palindrome.')









