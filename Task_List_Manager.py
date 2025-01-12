import os

# Function to load tasks from the file
def load_tasks(file_name):
    tasks = []
    try:
        with open(file_name, 'r') as file:
            tasks = [task.strip() for task in file.readlines()]
    except FileNotFoundError:
        print("No previous tasks found. Starting a new task list.")
    except IOError:
        print("Error reading from the file.")
    return tasks

# Function to save tasks to the file
def save_tasks(file_name, tasks):
    try:
        with open(file_name, 'w') as file:
            for task in tasks:
                file.write(task + '\n')
    except IOError:
        print("Error writing to the file.")

# Function to add a task to the list
def add_task(task, file_name, tasks):
    tasks.append(task)
    save_tasks(file_name, tasks)
    print(f"Task '{task}' added successfully.")

# Function to remove a task from the list
def remove_task(task, file_name, tasks):
    if task in tasks:
        tasks.remove(task)
        save_tasks(file_name, tasks)
        print(f"Task '{task}' removed successfully.")
    else:
        print(f"Task '{task}' not found in the list.")

# Function to view the current task list
def view_tasks(tasks):
    if not tasks:
        print("Your task list is empty.")
    else:
        print("\nCurrent Task List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

# Main program to interact with the user
def main():
    file_name = "tasks.txt"
    tasks = load_tasks(file_name)

    while True:
        print("\nTask List Manager")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. View tasks")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the task you want to add: ")
            add_task(task, file_name, tasks)
        elif choice == '2':
            task = input("Enter the task you want to remove: ")
            remove_task(task, file_name, tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the main function
if __name__ == "__main__":
    main()
