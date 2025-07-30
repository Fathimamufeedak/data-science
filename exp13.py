import numpy as np

# Function to take matrix input from user
def input_matrix(name):
    print(f"Enter elements for matrix {name} (3x3):")
    matrix = []
    for i in range(3):
        row = list(map(int, input(f"Row {i+1} (3 space-separated numbers): ").split()))
        while len(row) != 3:
            print("Please enter exactly 3 numbers.")
            row = list(map(int, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    return np.array(matrix)

# Get user input
A = input_matrix("A")
B = input_matrix("B")

scalar = int(input("Enter a scalar value: "))

# (a) Addition
add_result = A + B

# (b) Subtraction
sub_result = A - B

# (c) Matrix Multiplication
mul_result = A @ B  # or np.dot(A, B)

# (d) Scalar Multiplication
scalar_mul_result = scalar * A

# (e) Transpose
transpose_A = A.T
transpose_B = B.T

# Display results
print("\nMatrix A:\n", A)
print("Matrix B:\n", B)
print("\n(a) Addition:\n", add_result)
print("\n(b) Subtraction:\n", sub_result)
print("\n(c) Matrix Multiplication:\n", mul_result)
print(f"\n(d) Scalar Multiplication of A by {scalar}:\n", scalar_mul_result)
print("\n(e) Transpose of A:\n", transpose_A)
print("Transpose of B:\n", transpose_B)
