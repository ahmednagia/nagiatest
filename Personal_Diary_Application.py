import os
from datetime import datetime

def write_diary_entry(file_name, entry, add_timestamp=True):
    try:
        with open(file_name, 'a') as file:
            if add_timestamp:
                # Add current timestamp to the entry
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"Date: {timestamp}\n")
            file.write(f"{entry}\n\n")
        print("Diary entry saved successfully!")
    except PermissionError:
        print("Error: You do not have permission to write to this file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_diary_entries(file_name):
    try:
        if not os.path.exists(file_name):
            print("No diary entries found.")
            return
        
        with open(file_name, 'r') as file:
            content = file.read()
            if content:
                print("\nPrevious Diary Entries:\n")
                print(content)
            else:
                print("No entries found in the diary.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_name = "diary.txt"  # File to store diary entries
    
    while True:
        print("\nDiary Application Menu:")
        print("1. Create a new diary entry")
        print("2. View previous diary entries")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")
        
        if choice == "1":
            # Create a new diary entry
            entry = input("Write your diary entry: ")
            add_timestamp = input("Do you want to add a timestamp? (y/n): ").lower() == 'y'
            write_diary_entry(file_name, entry, add_timestamp)
        
        elif choice == "2":
            # View previous diary entries
            view_diary_entries(file_name)
        
        elif choice == "3":
            # Exit the application
            print("Goodbye! Thank you for using the diary app.")
            break
        
        else:
            print("Invalid choice. Please choose again.")

# Run the main function
if __name__ == "__main__":
    main()
