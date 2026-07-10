# Q7: Matrices and Operations

# Import NumPy library
import numpy as np

# Create Matrix A
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Create Matrix B
B = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

# Matrix Addition
addition = A + B

# Matrix Multiplication
multiplication = A @ B
# (You can also use: np.dot(A, B))

# Element-wise Multiplication
elementwise = A * B

# Print Results
print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nMatrix Addition:")
print(addition)

print("\nMatrix Multiplication:")
print(multiplication)

print("\nElement-wise Multiplication:")
print(elementwise)