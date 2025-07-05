# Initialize empty lists for even and odd numbers
even_numbers = []
odd_numbers = []

print("Enter numbers one by one. Type 'exit' to stop.")

while True:
    user_input = input("Enter a number (or type 'exit' to finish): ")
    
    # Check if the user wants to exit
    if user_input.lower() == 'exit' or user_input.lower() == 'quit':
        break

    # Try to convert the input to an integer
    try:
        num = int(user_input)
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a number or type 'exit'.")

# Display the results
print("\nEven Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
