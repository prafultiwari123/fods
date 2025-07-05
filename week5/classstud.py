class Student:
    def __init__(self):
        # Take input for each attribute
        self.id = input("Enter student ID: ")
        self.name = input("Enter student name: ")
        self.address = input("Enter address: ")
        self.admission_year = input("Enter admission year: ")
        self.level = input("Enter level (e.g., Undergraduate/Graduate): ")
        self.section = input("Enter section: ")

    def display_info(self):
        print("\n--- Student Information ---")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Admission Year: {self.admission_year}")
        print(f"Level: {self.level}")
        print(f"Section: {self.section}")

# Main program
if __name__ == "__main__":
    student = Student()       # Create object and take input
    student.display_info()    # Display the student details
