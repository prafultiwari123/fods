import csv

def read_students(filename):
    try:
        with open(filename, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            print("Student Records:")
            print("----------------")
            for row in reader:
                print(f"Name: {row['name']}, ID: {row['id']}, Course: {row['course']}, Level: {row['level']}, Section: {row['section']}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except KeyError as e:
        print(f"Missing expected column: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    read_students("students.csv")

