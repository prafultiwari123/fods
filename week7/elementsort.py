def get_numbers():
    while True:
        try:
            nums = list(map(int, input("Enter at least 10 numbers separated by space: ").split()))
            if len(nums) < 10:
                print("Please enter at least 10 numbers.")
            else:
                return nums
        except ValueError:
            print("Invalid input. Please enter only integers.")

def main():
    numbers = get_numbers()
    numbers.sort()
    print("Sorted list:", numbers)

    # Slicing operations
    slice_2_5 = numbers[2:5]
    slice_5_8 = numbers[5:8]
    slice_2_9 = numbers[2:9]

    print("Elements from index 2 to 5 (excluding 5):", slice_2_5)
    print("Elements from index 5 to 8 (excluding 8):", slice_5_8)
    print("Elements from index 2 to 9 (excluding 9):", slice_2_9)

if __name__ == "__main__":
    main()
