import os

# Function to input and store grades
def input_grades(filename):
    grades = []
    while True:
        try:
            # Prompt the user to input a grade
            grade = input("Enter the grade for the subject (or type 'done' to finish): ")
            
            # If the user types 'done', exit the loop
            if grade.lower() == 'done':
                break

            # Try to convert the grade to a float (for numeric input)
            grade = float(grade)
            
            # If the grade is valid, add it to the grades list
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Please enter a grade between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numeric grade.")
    
    # Write the grades to the file
    try:
        with open(filename, 'a') as file:
            for grade in grades:
                file.write(f"{grade}\n")
        print(f"Grades successfully saved to {filename}.")
    except IOError:
        print("Error writing to the file. Please check the file permissions.")

# Function to read grades from the file and calculate the average
def calculate_average(filename):
    if not os.path.exists(filename):
        print(f"The file {filename} does not exist.")
        return

    try:
        with open(filename, 'r') as file:
            grades = file.readlines()
        
        # Convert the grades from strings to floats
        grades = [float(grade.strip()) for grade in grades]
        
        if grades:
            average = sum(grades) / len(grades)
            print(f"Average grade: {average:.2f}")
        else:
            print("No grades found in the file.")
    
    except IOError:
        print("Error reading from the file.")
    except ValueError:
        print("Error: Non-numeric data found in the file.")

# Function to display the menu and handle user choices
def main():
    filename = 'grades.txt'

    while True:
        print("\nStudent Grade Tracker")
        print("1. Input grades")
        print("2. Calculate average grade")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            input_grades(filename)
        elif choice == '2':
            calculate_average(filename)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
