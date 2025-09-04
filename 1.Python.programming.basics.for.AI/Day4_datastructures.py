"""
# 1. Storing the ordered sequence of lecture topics.
# A LIST is perfect: the order is crucial, and we might change it later.
lecture_topics = ["Introduction", "Data Types", "Functions", "Modules"]
lecture_topics.append("Final Project") # MUTABLE: We can add an item.
lecture_topics[1] = "Core Data Types"  # MUTABLE: We can change an item.
print(f"Course Topics: {lecture_topics}")
print(f"The second topic is: {lecture_topics[1]}") # Access by index.


# 2. Storing a fixed course identifier (ID, Start Date).
# A TUPLE is perfect: it's a permanent record that should not be changed.
course_config = (101, "2025-09-15") 
# course_config[0] = 102 # This would cause a TypeError! TUPLES ARE IMMUTABLE.
print(f"Course Config (ID, Start Date): {course_config}")


# 3. Mapping student usernames to their grades.
# A DICTIONARY is the only choice: we map a unique key (username) to a value (grade).
student_grades = {
    "aziz": 95,
    "iman_k": 88,
    "budi": 92
}
student_grades["aziz"] = 97 # MUTABLE: We can update a student's grade.
student_grades["diana"] = 85 # MUTABLE: We can add a new student.
print(f"Aziz's current grade is: {student_grades['aziz']}") # Access by key.


# 4. Tracking unique students who completed orientation.
# A SET is perfect: we only care if a student is in the group, and we don't want duplicates.
completed_orientation = {"aziz", "budi", "aziz"} # Note: 'aziz' duplicate is ignored.
completed_orientation.add("charlie") # MUTABLE: We can add a new student.
print(f"Students who completed orientation: {completed_orientation}")
print(f"Did Iman complete orientation? {'iman_k' in completed_orientation}") # Fast membership checking.
"""






# 1. LISTS
    # A Python list is a built-in data structure that represents an ordered, mutable collection of items. Key characteristics of Python lists include:
        # Ordered: The elements in a list maintain a specific sequence, and their position can be accessed using zero-based indexing (e.g., the first element is at index 0). Negative indexing can also be used to access elements from the end of the list (e.g., -1 for the last element).
        # Mutable: Lists are dynamic, meaning their contents can be modified after creation. Elements can be added, removed, or changed in place without creating a new list object.
        # Heterogeneous: A single list can contain elements of different data types, such as integers, floats, strings, booleans, or even other lists (creating nested lists).
        # Defined by square brackets: Lists are created by enclosing a comma-separated sequence of elements within square brackets [].
    # Contoh penggunaan list:
"""
    numbers = [1, 2, 3, 4]

    fruits = ["apple", "banana", "cherry"]

    mixed = [1, "apple", True]

    print(numbers[0]) # print by index
    print(fruits[2])
    print(mixed[1])

    fruits.append("orange") # add string
    fruits.insert(1, "grape") # add with index+string (perbaikan dari 'inser')
    fruits.remove("banana") # remove by string
    del fruits[0] # remove by index
    fruits.pop() # remove and return the last item
    sliced_fruits = fruits[1:3] # creates a new list from index 1 up to (but not including) 3
"""
    # In Python, an index refers to the position of an element within a sequence data type, such as a string, list, or tuple. Python uses zero-based indexing, meaning the first element in a sequence is at index 0, the second at index 1, and so on. 
        # Zero-based: The counting of positions starts from 0 for the first element.
        # Positive indexing: Accessing elements from the beginning of the sequence using non-negative integers (e.g., my_list[0]).
        # Negative indexing: Accessing elements from the end of the sequence using negative integers, where -1 refers to the last element, -2 to the second-to-last, and so on (e.g., my_string[-1]).
        # Square brackets: Indexes are specified within square brackets [] after the sequence variable name to retrieve the element at that position.  

# 2. TUPLES
    # In Python, a tuple is an ordered, immutable sequence of objects. It is one of the four built-in data types in Python used to store collections of items, alongside lists, sets, and dictionaries.
        # Ordered: The elements in a tuple maintain a specific order, and this order is preserved when accessing or iterating through the tuple.
        # Immutable: Once a tuple is created, its elements cannot be modified, added, or removed. This immutability makes tuples suitable for storing data that should not be changed, such as configuration settings or database records.
        # Heterogeneous: Tuples can contain elements of different data types (e.g., integers, strings, floats, or even other tuples or lists).
        # Defined using parentheses: Tuples are typically created by enclosing comma-separated values within parentheses (). For a single-element tuple, a trailing comma is required (e.g., (item,)).
"""        
    colors = ("red", "green", "blue")
    single_item = ("glass",)

    print(colors[0]) # print by index
    print(colors[-1]) # print by index from last element
"""

# 3. DICTIONARIES
    # A Python dictionary is a built-in data structure that stores data in unordered, mutable collections of key-value pairs. Each key within a dictionary must be unique and immutable (e.g., strings, numbers, or tuples), while the corresponding values can be of any data type and are mutable.
    # Dictionaries are defined using curly braces {}, with each key-value pair separated by a colon : and individual pairs separated by commas.
    # Dictionaries are highly efficient for data retrieval and manipulation because values are accessed directly by their associated keys, rather than by numerical indices as in lists. 
    # This makes them a suitable choice for representing data where elements are logically associated with unique identifiers.
"""    
    student = {"name": "Alice", "age": 25, "grade": "A"}

    student["subject"] = "Math" #add new key:value
    student["age"]= 32 #change existing integer value

    del student["grade"]

    print(student) #print all
    print(student["name"]) #print value by input key
    student.pop("subject") #

        # Iteration
    for key, value in student.items():
        print (key, value) # Print both key:value side by side
"""     
     
# 4. SETS
    # A Python set is an unordered collection of unique elements. Key characteristics of Python sets include: 
        # Unordered: Elements within a set do not maintain any specific order, meaning their position is not guaranteed and can change.
        # Unique Elements: Sets automatically handle duplicates, ensuring that each element stored within a set appears only once. If you attempt to add a duplicate element, it will simply be ignored.
        # Mutable (but elements are immutable):While you can add or remove elements from a set (making the set itself mutable), the individual elements stored within a set must be immutable (e.g., numbers, strings, tuples). You cannot store mutable objects like lists or dictionaries directly within a set.
        # Unindexed: Due to their unordered nature, set elements cannot be accessed using indexing or slicing.
        # Mathematical Set Operations: Python sets support various mathematical set operations like union, intersection, difference, and symmetric difference, which can be performed using dedicated methods or operators.
            # Sets are commonly used for tasks such as removing duplicate elements from a list, performing efficient membership tests (checking if an element is present in a set), and carrying out set-theoretic operations. They are created using curly braces {} or by using the set() constructor. An empty set must be created using set() as {} creates an empty dictionary
"""            
    numbers = {1, 2, 3, 4}
    empty_set = set () #create empty set

    numbers.add(5) #add sets
    numbers.add(4) #add sets but 4 already exist, no duplicate
    numbers.remove(2) #remove sets

    set1 = {1, 2, 3}
    set2 = {3, 4, 5}

    print(set1 | set2) #union : 12345
    print(set1 & set2) #intersection : 3
    print(set1 - set2) #difference : {1, 2}
"""


# HANDS-ON EXERCISES

# 1. Manipulate Data in a Dictionary
"""
    person = {"name": "Alice", "age": 25, "grade": "A"}

    print(person)

    #add new key-value pair
    person["address"] = "123 Main St"

    #update age
    person["age"] = 32

    #remove grade
    if "grade" in person:
        del person["grade"]
        
    print(person)
"""

# 2. Word Frequency Counter
"""
    sentence = input("Enter a Sentence: ")

    #split the sentence into words
    words = sentence.split()

    #initialize dictionary
    word_count = {}

    #count word frequence
    for word in words :
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    print(word_count)
"""

# 3. Write a program to reverse a list and remove duplicates using a set
"""
def process_list(original_list):
    
    #Reverse a list and remove duplicates.
    #Args:original_list: The list to process
    #Returns: A new list that is reversed and has duplicates removed
    
    # Step 1: Reverse the list
    reversed_list = original_list[::-1]
    
    # Step 2: Use a set to remove duplicates (sets automatically remove duplicates)
    # Then convert back to a list
    unique_set = set(reversed_list)
    
    # Step 3: Convert the set back to a list
    result_list = list(unique_set)
    
    return result_list

# Alternative one-line version
def process_list_short(original_list):
    
    # Reverse a list and remove duplicates in one line.
    
    return list(set(original_list[::-1]))

# Test the function
if __name__ == "__main__":
    # Example list with duplicates
    my_list = [1, 2, 3, 2, 4, 5, 3, 6, 1]
    
    print("Original list:", my_list)
    
    # Process the list
    processed = process_list(my_list)
    print("Reversed with duplicates removed:", processed)
    
    # Test with the one-line version
    processed_short = process_list_short(my_list)
    print("One-line version result:", processed_short)
    
    # Test with string elements
    string_list = ["apple", "banana", "cherry", "apple", "date", "banana"]
    print("\nOriginal string list:", string_list)
    print("Processed string list:", process_list(string_list))
"""

# 4. Create a program that stores student grades in a dictionary and calculates the average grade

class GradeManager:
    def __init__(self):
        # Dictionary to store student grades
        # Format: {student_name: [list_of_grades]}
        self.grades = {}
    
    def add_student(self, name):
        """Add a new student with an empty grade list"""
        if name not in self.grades:
            self.grades[name] = []
            print(f"Student '{name}' added successfully.")
        else:
            print(f"Student '{name}' already exists.")
    
    def add_grade(self, name, grade):
        """Add a grade for a specific student"""
        if name in self.grades:
            # Validate grade is between 0 and 100
            if 0 <= grade <= 100:
                self.grades[name].append(grade)
                print(f"Grade {grade} added for {name}.")
            else:
                print("Grade must be between 0 and 100.")
        else:
            print(f"Student '{name}' not found. Please add the student first.")
    
    def calculate_average(self, name):
        """Calculate the average grade for a specific student"""
        if name in self.grades:
            if self.grades[name]:  # Check if the student has grades
                average = sum(self.grades[name]) / len(self.grades[name])
                return round(average, 2)
            else:
                return "No grades available"
        else:
            return "Student not found"
    
    def display_student_grades(self, name):
        """Display all grades and average for a specific student"""
        if name in self.grades:
            avg = self.calculate_average(name)
            print(f"\n{name}'s Grades:")
            print(f"All grades: {self.grades[name]}")
            print(f"Average: {avg}")
        else:
            print(f"Student '{name}' not found.")
    
    def display_all_grades(self):
        """Display all students and their average grades"""
        if not self.grades:
            print("No students in the system.")
            return
        
        print("\nAll Student Grades:")
        print("-" * 30)
        for name, grade_list in self.grades.items():
            avg = self.calculate_average(name)
            print(f"{name}: Grades={grade_list}, Average={avg}")

# Main program function
def main():
    manager = GradeManager()
    
    while True:
        print("\nGrade Management System")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Student Grades")
        print("4. View All Grades")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            name = input("Enter student name: ")
            manager.add_student(name)
        
        elif choice == "2":
            name = input("Enter student name: ")
            try:
                grade = float(input("Enter grade (0-100): "))
                manager.add_grade(name, grade)
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "3":
            name = input("Enter student name: ")
            manager.display_student_grades(name)
        
        elif choice == "4":
            manager.display_all_grades()
        
        elif choice == "5":
            print("Exiting Grade Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1-5.")

# Run the program
if __name__ == "__main__":
    main()
