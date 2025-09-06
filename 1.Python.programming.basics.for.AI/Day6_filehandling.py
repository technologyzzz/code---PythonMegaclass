# 1. Reading and Writing Text File
    #opening files
        # r (read) | w (write) | a (append) | r+ (read&write)
    
    #reading files, opening only
        #.read() | .readline() | .readlines() |
        
    #writing files, destroy all old content
        #.write() | .writelines() |      
        
    #append files, keep old content and edit
        #.append()  
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
"""     
    def count_words_and_lines(filename):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                line_count = len(lines)
                word_count = sum(len(line.split()) for line in lines)
        
                print(f"Number of lines : {line_count}")
                print(f"Number of words : {word_count}")
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
    write_item_to_file("fruits.txt", fruits)
    read_items_from_file("fruits.txt")
"""

    # 3. Write a program to copy the contents of one file to another
"""
# 1. IMPORTS GO AT THE TOP. This is non-negotiable professional practice.
    import argparse
    import sys
    import shutil
    import os

    def copy_file_robust(source_path: str, dest_path: str, force_overwrite: bool = False):
        
        #Robustly copies a file from a source to a destination.
        #This function's only job is to perform the copy and report errors by raising exceptions.
        #It does not print friendly messages; that is the caller's responsibility.

        #Args:
            #source_path (str): The path to the file to be copied.
            #dest_path (str): The path to the destination.
            #force_overwrite (bool): If True, will overwrite the destination.

        #Raises:
            #FileNotFoundError: If the source file does not exist.
            #FileExistsError: If the destination exists and force_overwrite is False.
            #Exception: For other potential OS-level errors (e.g., permissions).
        
        # 2. A function should validate its preconditions.
        if not force_overwrite and os.path.exists(dest_path):
            raise FileExistsError(f"Destination '{dest_path}' already exists. Use --force to overwrite.")
            
        try:
            # 3. Use the right tool for the job. shutil.copy is optimized and safe.
            shutil.copy(source_path, dest_path)
        except FileNotFoundError:
            # Re-raise the exception with a more informative message.
            raise FileNotFoundError(f"Source file '{source_path}' not found.")
        except Exception as e:
            # Let other exceptions (like PermissionError from shutil) propagate.
            raise e

    def main():
        
        #Main function to parse command-line arguments and orchestrate the file copy.
        #This function handles all user interaction (parsing arguments, printing results).
        
        # 4. Use 'argparse' for professional command-line arguments, not input().
        parser = argparse.ArgumentParser(description="A robust program to copy file contents.")
        parser.add_argument("source", help="Path of the source file.")
        parser.add_argument("destination", help="Path of the destination file.")
        parser.add_argument("-f", "--force", action="store_true", help="Force overwrite if destination exists.")
        
        args = parser.parse_args()

        # 5. The main logic block handles exceptions and prints user-friendly messages.
        try:
            copy_file_robust(args.source, args.destination, force_overwrite=args.force)
            print("✅ Success!")
            print(f"Copied '{args.source}' to '{args.destination}'")
        except (FileNotFoundError, FileExistsError) as e:
            # Catch specific, expected errors.
            print(f"❌ Error: {e}", file=sys.stderr)
            sys.exit(1) # Exit with a non-zero status code to signal failure.
        except Exception as e:
            # Catch any other unexpected errors.
            print(f"❌ An unexpected error occurred: {e}", file=sys.stderr)
            sys.exit(1)

    if __name__ == "__main__":
        main()
"""    
    # 4. Create a program that counts the number of occurrences of a specific word in a text file

def simple_word_count(filename, target_word, case_sensitive=False):
    """
    Simple word count using string splitting.
    Note: This may count word parts, not just whole words.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
        
        if not case_sensitive:
            text = text.lower()
            target_word = target_word.lower()
        
        # Split text into words (simple approach)
        words = text.split()
        
        # Count exact matches
        count = words.count(target_word)
        
        return count
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return 0

# Usage
filename = "sample.txt"
target_word = "Python"
count = simple_word_count(filename, target_word, case_sensitive=False)
print(f"The word '{target_word}' appears {count} times.")
    
    
    # 5. Write a program to log messages with timestamps into a file
    
import datetime
import os

def log_message(message, log_file="message_log.txt"):
    """
    Log a message with a timestamp to a file.
    
    Args:
        message (str): The message to log
        log_file (str): The path to the log file
    """
    # Get current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Format the log entry
    log_entry = f"[{timestamp}] {message}\n"
    
    try:
        # Open the log file in append mode
        with open(log_file, 'a', encoding='utf-8') as file:
            file.write(log_entry)
        
        print(f"Message logged: {log_entry.strip()}")
        
    except Exception as e:
        print(f"Error writing to log file: {str(e)}")

def view_log(log_file="message_log.txt", num_entries=None):
    """
    View the contents of the log file.
    
    Args:
        log_file (str): The path to the log file
        num_entries (int): Number of recent entries to show (None for all)
    """
    try:
        # Check if the log file exists
        if not os.path.exists(log_file):
            print("No log file found.")
            return
        
        # Read all lines from the log file
        with open(log_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Show only recent entries if requested
        if num_entries is not None and num_entries > 0:
            lines = lines[-num_entries:]
        
        # Display the log entries
        if not lines:
            print("Log file is empty.")
        else:
            print(f"\n--- Log Entries ({len(lines)}) ---")
            for line in lines:
                print(line.strip())
            print("--- End of Log ---")
    
    except Exception as e:
        print(f"Error reading log file: {str(e)}")

def clear_log(log_file="message_log.txt"):
    """
    Clear the contents of the log file.
    
    Args:
        log_file (str): The path to the log file
    """
    try:
        # Confirm before clearing
        confirm = input("Are you sure you want to clear the log? (y/n): ")
        if confirm.lower() != 'y':
            print("Operation cancelled.")
            return
        
        # Clear the file by opening in write mode
        with open(log_file, 'w', encoding='utf-8') as file:
            file.write("")
        
        print("Log file cleared.")
    
    except Exception as e:
        print(f"Error clearing log file: {str(e)}")

def main():
    """
    Main function to run the message logger.
    """
    log_file = "message_log.txt"  # Default log file
    
    while True:
        print("\nMessage Logger")
        print("1. Log a message")
        print("2. View log")
        print("3. View recent entries")
        print("4. Clear log")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            message = input("Enter your message: ")
            log_message(message, log_file)
        
        elif choice == "2":
            view_log(log_file)
        
        elif choice == "3":
            try:
                num_entries = int(input("How many recent entries to show? "))
                view_log(log_file, num_entries)
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "4":
            clear_log(log_file)
        
        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1-5.")

if __name__ == "__main__":
    main()

    
    
    
    
    
    
    
    
    
    
    
    
    
     