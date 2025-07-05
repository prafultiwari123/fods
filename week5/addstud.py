import csv

def append_student(filename):
    # Take user input
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    course = input("Enter course: ")
    level = input("Enter level (e.g., Undergraduate/Graduate): ")
    section = input("Enter section: ")

    # Create a dictionary for the new record
    new_student = {
        "name": name,
        "id": student_id,
        "course": course,
        "level": level,
        "section": section
    }

    # Append to the CSV file
    try:
        with open(filename, mode='a', newline='') as csvfile:
            fieldnames = ['name', 'id', 'course', 'level', 'section']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write only the row (no header in append mode)
            writer.writerow(new_student)

        print("Student record added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    append_student("students.csv")
