import datetime

def calculate_operations(numbers):
    addition = sum(numbers)
    subtraction = numbers[0]
    multiplication = 1
    division = numbers[0]

    for num in numbers[1:]:
        subtraction -= num
        multiplication *= num
        if num != 0:
            division /= num
        else:
            division = "Undefined (division by zero)"
            break

    return addition, subtraction, multiplication, division

def write_to_file(filename, numbers, results):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as f:
        f.write(f"Date/Time: {now}\n")
        f.write(f"Numbers: {numbers}\n")
        f.write(f"Addition: {results[0]}\n")
        f.write(f"Subtraction: {results[1]}\n")
        f.write(f"Multiplication: {results[2]}\n")
        f.write(f"Division: {results[3]}\n")
        f.write("-" * 40 + "\n")

def read_file(filename):
    print("\n=== Operation History ===\n")
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No records found.")

def main():
    filename = "calculations_log.txt"
    
    while True:
        try:
            input_str = input("\nEnter a list of numbers separated by space: ")
            number_list = list(map(float, input_str.strip().split()))
            if len(number_list) < 2:
                print("Please enter at least two numbers.")
                continue

            results = calculate_operations(number_list)
            write_to_file(filename, number_list, results)
            print("Operations saved successfully.")

            repeat = input("Do you want to continue? (yes/no): ").strip().lower()
            if repeat not in ('yes', 'y'):
                break
        except ValueError:
            print("Invalid input. Please enter only numbers.")

    read_file(filename)

if __name__ == "__main__":
    main()
