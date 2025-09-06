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
    digits = re.findall(r"\d+", text) #functions to split (find an list) components
    print(digits)

    updated_text = re.sub(r"\d+", "X", text) #functions to change chro(find and replace) components
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
"""    
    def is_palindrome(text):
        text = "".join(char.lower() for char in text if char.isalnum())
        return text == text[::-1]

    input_text = input("Enter a string: ")
    if is_palindrome(input_text):
        print(f'"{input_text}" is a palindrome,')
    else:
        print(f'"{input_text}" is not a palindrome.')
"""
    # 3. Write a program to count the number of vowels in a string
"""
    def count_vowels(text):
        
        # Count the number of vowels in a string (case-insensitive).
        # Args: text (str): The input string to analyze
        # Returns: int: The number of vowels in the string

        vowels = "aeiou"
        
        count = 0
        text_lower = text.lower()

        for char in text_lower:
            if char in vowels:
                count += 1
        
        return count

    # Alternative method using list comprehension
    def count_vowels_short(text):

        # Count vowels using a more concise approach.
        
        vowels = "aeiou"
        return sum(1 for char in text.lower() if char in vowels)

    # Get input from user and display results
    if __name__ == "__main__":
        user_input = input("Enter a string to count its vowels: ")
        
        # Count vowels using both methods
        vowel_count = count_vowels(user_input)
        vowel_count_short = count_vowels_short(user_input)
        
        print(f"\nIn the string: '{user_input}'")
        print(f"Number of vowels (method 1): {vowel_count}")
        print(f"Number of vowels (method 2): {vowel_count_short}")
        
        vowels_found = [char for char in user_input.lower() if char in "aeiou"]
        print(f"Vowels found: {vowels_found}")
"""
    
    # 4. Create a program to find and replace all email addresses in a text using regex

import re

def find_and_replace_emails(text, replacement="[EMAIL REDACTED]"):
    
    #Find and replace all email addresses in the given text.
    #Args:
        #text (str): The input text containing email addresses
        #replacement (str): The text to replace email addresses with
    #Returns:
        #str: Text with email addresses replaced
        #list: List of found email addresses

    # Regular expression pattern for matching email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # Find all email addresses in the text
    found_emails = re.findall(email_pattern, text)
    
    # Replace all email addresses with the replacement text
    modified_text = re.sub(email_pattern, replacement, text)
    
    return modified_text, found_emails

def main():
    # Example text with email addresses
    sample_text = """
    Please contact us at support@company.com for assistance. 
    You can also reach our sales team at sales@company.com or 
    john.doe@example.org. For urgent matters, email emergency@company.com.
    Don't forget to cc: admin@department.example.co.uk on all correspondence.
    """
    
    print("Original Text:")
    print(sample_text)
    print("-" * 50)
    
    # Find and replace emails
    modified_text, found_emails = find_and_replace_emails(sample_text)
    
    print("Found Email Addresses:")
    for email in found_emails:
        print(f"  - {email}")
    
    print("-" * 50)
    print("Modified Text:")
    print(modified_text)
    
    # Interactive example
    print("\n" + "="*50)
    user_text = input("Enter your own text to test (or press Enter to use sample): ")
    
    if not user_text.strip():
        user_text = sample_text
    
    user_modified, user_found = find_and_replace_emails(user_text)
    
    print("\nFound Email Addresses:")
    for email in user_found:
        print(f"  - {email}")
    
    print("\nModified Text:")
    print(user_modified)

if __name__ == "__main__":
    main()




# f'' formattedstring : template to embed variables/expression {}
# r'' rawstring : literal string where punctuations with \ is normal character (not special codes)
# b'' bytes : no plain text (https, images, audio, cryptography), raw sequence of number
# u'' unicodestring : old python all starndar strings, rarely used

 