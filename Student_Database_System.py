class Student:
    def __init__(self, name, age):
        self.name = name  # Student's name
        self.age = age  # Student's age
        self.grades = []  # List to store student's grades
    
    def add_grade(self, grade):
        """Method to add a grade to the student's grade list."""
        self.grades.append(grade)
    
    def average_grade(self):
        """Method to calculate the average of the student's grades."""
        if len(self.grades) == 0:
            return 0  # Prevent division by zero if there are no grades
        return sum(self.grades) / len(self.grades)
    
    def display_info(self):
        """Method to display the student's name, age, and grades."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.average_grade():.2f}")
        print("-" * 30)


# Simulating the database of students
students_db = []  # A list to store multiple students

def add_student_to_database(name, age):
    """Function to create a new student and add to the database."""
    new_student = Student(name, age)
    students_db.append(new_student)

def display_all_students():
    """Function to display all students in the database."""
    if not students_db:
        print("No students in the database.")
        return
    
    for student in students_db:
        student.display_info()


def main():
    # Adding some students and their grades
    add_student_to_database("Alice", 20)
    students_db[0].add_grade(90)
    students_db[0].add_grade(85)
    
    add_student_to_database("Bob", 22)
    students_db[1].add_grade(78)
    students_db[1].add_grade(82)
    students_db[1].add_grade(88)
    
    add_student_to_database("Charlie", 19)
    students_db[2].add_grade(95)
    
    # Displaying all students in the database
    print("Student Database:")
    display_all_students()

if __name__ == "__main__":
    main()
