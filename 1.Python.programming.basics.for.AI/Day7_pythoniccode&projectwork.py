# 1. Writing Clean, "Pythonic" Code
    #Pythonic code refers to a style of writing Python code that adheres to the principles and idioms of the Python programming language and its community. 
    #It emphasizes readability, simplicity, and elegance, leveraging Python's distinctive features to create code that is not only functional but also easy to understand and maintain.
        
        #Readability and Clarity:
            #Prioritizing code that is self-documenting and easily understood by others, often achieved through clear variable names, concise expressions, and adherence to style guides like PEP 8.
        
        #Leveraging Built-in Features:
            #Utilizing Python's powerful built-in functions, data structures (like lists, dictionaries, sets), and language constructs (like list comprehensions, generators, context managers) to write more efficient and expressive code.
        
        #Embracing Python's Philosophy:
            #Following the principles outlined in "The Zen of Python" (accessible by typing import this in a Python interpreter), such as "Beautiful is better than ugly," "Explicit is better than implicit," and "Readability counts."
        
        #Idiomatic Usage:
                #Employing common Python idioms and patterns, such as unpacking for variable assignment, using str.join() for string concatenation from a list, and favoring dictionaries or sets for efficient lookups when appropriate.
        
        #Avoiding "Un-Pythonic" Practices: 
            #Refraining from coding patterns more common in other languages that might be less efficient or clear in Python, such as over-reliance on traditional loops when comprehensions are more suitable, or excessive use of explicit if/else checks when Python's truthiness can be leveraged.

# 2. List Comprehension
"""   
        #[expression for item in iterable if condition]

            # Create a list of squares
    squares = [x**2 for x in range(10)]
    print(squares)

            # Filters Even Numbers
    evens = [x for x in range(100) if x % 2 == 0] #!== for Odd Numbers
    print(evens)
"""
# 3. Lambda Functions
    #A Python lambda function is a small, anonymous function defined using the lambda keyword. 
    #Unlike regular functions defined with def, lambda functions are concise, typically written in a single line, and do not require a return statement as they implicitly return the result of their single expression. 
        #Anonymous: They do not have a name unless explicitly assigned to a variable. 
        #Single expression: They are limited to a single expression, meaning they cannot contain multiple statements or complex control flow like loops or conditional blocks. 
        #Concise: Their compact nature makes them suitable for quick, one-time operations.
        #Often used with higher-order functions: They are frequently employed as arguments to functions like map(), filter(), and sorted(), where a small, inline function is needed to perform a specific operation on data.
"""
        #Lambda arguments: expression
    add = lambda x, y: x + y #custom function
    print(add(3,5))

    numbers = [1, 2, 3, 4]
            #map()
    squares = map(lambda x: x**2, numbers) 
    print(list(squares))
            #filter()
    evenList = filter(lambda x: x % 2 == 0, numbers)
    print(list(evens))
            #reduce()
    from functools import reduce
    product = reduce(lambda x,y: x * y, numbers)
    print(product)
"""      
# 4. Python's os and sys Modules
"""
    # os
    import os 

    print(os.getcwd())
    os.mkdir("test_dir")
    os.remove("file.txt")

        # sys module
    import sys

    print(sys.argv)
    print(sys.version)
"""



# HANDS-ON PROJECT

# 1. Command-Line Task Manager

import os

# file to store tasks
FILE_NAME = "tasks.txt"

# load tasks from file
def load_tasks():
    tasks = {}
    # --- FIX --- 'exists' is the correct method name.
    if os.path.exists(FILE_NAME):
        # --- FIX --- Correct variable name.
        with open(FILE_NAME, "r") as file:
            # --- FIX --- Loop over 'file', not a non-existent 'files'.
            for line in file:
                # --- FIX --- Added a check for empty lines to prevent crashes.
                if line.strip(): 
                    task_id, title, status = line.strip().split(" | ")
                    # --- FIX --- Trailing underscore removed from task_id.
                    tasks[int(task_id)] = {"title": title, "status": status}
    return tasks

# save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task_id, task_data in tasks.items():
            # --- CRITICAL LOGIC FIX ---
            # You must use the loop variables ('task_id', 'task_data'),
            # not the entire 'tasks' dictionary in the f-string.
            file.write(f"{task_id} | {task_data['title']} | {task_data['status']}\n")

# add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    # --- FIX --- 'task_id' is the correct variable name.
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title": title, "status": "incomplete"}
    print(f"Task '{title}' added.")

# view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for task_id, task_data in tasks.items():
            # --- CRITICAL LOGIC FIX --- Use the loop variables.
            print(f"[{task_id}] {task_data['title']} - {task_data['status']}")

# mark task as complete / delete
def mark_task_complete(tasks):
    # --- FIX --- Typo in 'task_id'.
    task_id = int(input("Enter task ID to mark as complete: "))
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print(f"Task '{tasks[task_id]['title']}' marked as complete.")
    else:
        print("Task ID not found.")

def delete_task(tasks):
    # --- FIX --- Typo in 'task_id'.
    task_id = int(input("Enter task ID to delete: "))
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"Task '{deleted_task['title']}' deleted.")
    else:
        print("Task ID not found.")

# main menu
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task(tasks)
            # --- SUGGESTION for robust code ---
            # To fix the data loss flaw, you should save after every change.
            # save_tasks(tasks) 
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            # --- FIX --- Correct function name.
            mark_task_complete(tasks)
            # save_tasks(tasks) # Also save here
        elif choice == "4":
            delete_task(tasks)
            # save_tasks(tasks) # And here
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye")
            break
        else:
            # --- FIX --- Typo in 'Invalid'.
            print("Invalid Choice. Please try again")

if __name__ == "__main__":
    main()
