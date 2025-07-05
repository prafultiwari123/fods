import numpy as np

# Create a 1D array of 10 random integers between 0 and 99
arr = np.random.randint(0, 100, size=10)
print("Original array:")
print(arr)

# Sort the array
arr_sorted = np.sort(arr)
print("\nSorted array:")
print(arr_sorted)

# Reshape the array into 2x5
arr_2x5 = arr_sorted.reshape(2, 5)
print("\nReshaped array (2 x 5):")
print(arr_2x5)

# Reshape the array into 5x2
arr_5x2 = arr_sorted.reshape(5, 2)
print("\nReshaped array (5 x 2):")
print(arr_5x2)
