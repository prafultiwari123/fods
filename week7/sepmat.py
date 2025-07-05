import numpy as np

def input_matrix(name):
    while True:
        try:
            rows = int(input(f"Enter number of rows for {name}: "))
            cols = int(input(f"Enter number of columns for {name}: "))
            print(f"Enter elements for {name} row-wise (space separated):")
            elements = list(map(float, input().split()))
            if len(elements) != rows * cols:
                print(f"Error: Number of elements entered ({len(elements)}) does not match matrix size ({rows*cols}). Try again.")
                continue
            matrix = np.array(elements).reshape(rows, cols)
            return matrix
        except ValueError:
            print("Invalid input. Please enter integers for size and numbers for elements.")

def main():
    print("Input first matrix:")
    mat1 = input_matrix("Matrix 1")
    print("\nInput second matrix:")
    mat2 = input_matrix("Matrix 2")

    print("\nMatrix 1:")
    print(mat1)
    print("\nMatrix 2:")
    print(mat2)

    # Addition
    try:
        if mat1.shape != mat2.shape:
            raise ValueError("Addition requires matrices of the same dimensions.")
        add_result = mat1 + mat2
        print("\nAddition Result:")
        print(add_result)
    except ValueError as e:
        print(f"Addition Error: {e}")

    # Subtraction
    try:
        if mat1.shape != mat2.shape:
            raise ValueError("Subtraction requires matrices of the same dimensions.")
        sub_result = mat1 - mat2
        print("\nSubtraction Result:")
        print(sub_result)
    except ValueError as e:
        print(f"Subtraction Error: {e}")

    # Multiplication
    try:
        if mat1.shape[1] != mat2.shape[0]:
            raise ValueError("Multiplication requires columns of first matrix to equal rows of second matrix.")
        mul_result = np.matmul(mat1, mat2)
        print("\nMultiplication Result:")
        print(mul_result)
    except ValueError as e:
        print(f"Multiplication Error: {e}")

if __name__ == "__main__":
    main()
