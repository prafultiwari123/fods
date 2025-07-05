
user_input = input("Enter numbers separated by spaces: ")


num_list = list(map(int, user_input.split()))


unique_list = []


for num in num_list:
    if num not in unique_list:
        unique_list.append(num)


print("List without duplicates:", unique_list)
