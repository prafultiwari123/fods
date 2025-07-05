import csv

class Employee:
    def __init__(self, empid, name, address, contact_number, spouse_name, number_of_child, salary):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.spouse_name = spouse_name
        self.number_of_child = number_of_child
        self.salary = salary

    def to_dict(self):
        return {
            "empid": self.empid,
            "name": self.name,
            "address": self.address,
            "contact_number": self.contact_number,
            "spouse_name": self.spouse_name,
            "number_of_child": self.number_of_child,
            "salary": self.salary
        }

def input_employee():
    try:
        empid = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        address = input("Enter Address: ")
        contact_number = input("Enter Contact Number: ")
        spouse_name = input("Enter Spouse Name: ")
        number_of_child = int(input("Enter Number of Children: "))
        salary = float(input("Enter Salary: "))
        return Employee(empid, name, address, contact_number, spouse_name, number_of_child, salary)
    except ValueError:
        print("Invalid input for number of children or salary. Please try again.")
        return None

def save_employees_to_file(employees, filename="employees.csv"):
    try:
        with open(filename, mode='w', newline='') as file:
            fieldnames = ["empid", "name", "address", "contact_number", "spouse_name", "number_of_child", "salary"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for emp in employees:
                writer.writerow(emp.to_dict())
        print(f"{len(employees)} employee(s) saved to {filename}.")
    except Exception as e:
        print(f"Error saving to file: {e}")

def read_employees_from_file(filename="employees.csv"):
    employees = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                employees.append(row)
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print(f"Error reading the file: {e}")
    return employees

def display_employees(employees):
    if not employees:
        print("No employees to display.")
        return
    print("\nEmployee List:")
    print("-" * 70)
    for emp in employees:
        print(f"ID: {emp['empid']}, Name: {emp['name']}, Address: {emp['address']}, Contact: {emp['contact_number']}, Spouse: {emp['spouse_name']}, Children: {emp['number_of_child']}, Salary: {emp['salary']}")
    print("-" * 70)

def main():
    employees = []

    while True:
        print("\nOptions:")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            emp = input_employee()
            if emp:
                employees.append(emp)
        elif choice == '2':
            # Read from file and display
            emp_list = read_employees_from_file()
            display_employees(emp_list)
        elif choice == '3':
            save_employees_to_file(employees)
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
