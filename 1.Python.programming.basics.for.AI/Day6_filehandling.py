# 1. Reading and Writing Text File
    #opening files
        # r (read) | w (write) | a (append) | r+ (read&write)
    
    #reading files
        #.read() | .readline() | .readlines() |
        
    #writing files
        #.write() | .writelines() |        
"""        
    with open("sample.txt", "r+") as file: #opening files function
        content = file.read() #reading files function
        print(content)
        file.write("Hello, World!") #writing files function
        file.writelines(["Alice", "Bob", "Cherry"])
"""
        
# 2. Using 'with' Statements for File Management
    #file is automatically closed : 'with' open () as file:

# 3. Basic Exception Handling for File Operations 
    #Python provides a structured way to handle these situations using exception handling with try, except, and finally blocks. 
    #Python Exception Handling handles errors that occur during the execution of a program. Exception handling allows to respond to the error, instead of crashing the running program. 
    #It enables you to catch and manage errors, making your code more robust and user-friendly.     
"""
    try:
        with open("sample.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("File Not Found:")
"""
 #FileNotFoundEError, PermissionError, IOError
    
    
# HANDS-0N EXERCISES

    # 1. Count Words and Lines in a File 
def count_words_and_lines(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readLines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
    
            print(f"Number of lines : {line_count}")
            print(f"Number of lines : {word_count}")
    except FileNotFoundError:
        print (f"File {filename} not found!")
    
count_words_and_lines("sample.txt")
    
    # 2. Write and Read a List of Items
def write_item_to_file(filename, items):
    with open(filename, "w") as file:
        for item in items:
            file.write(item+"\n")

def read_items_from_file(filename):
    try:
        with open(filename, "r") as file:
            items = file.readlines()
            print("Items in the file :")
            for item in items:
                print(item.strip())
    except FileNotFoundError:
        print(f"File {filename} not found!")
        
fruits = ["Apple", "Banana", "Cherry", "Dates"]
write_item_to_file("fuits.txt", fruits)
read_items_from_file("fruits.txt")
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    