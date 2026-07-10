# Q9: Combined - Random + Reshape + Statistics

# Import NumPy library
import numpy as np

# Generate a 1D array of 20 random integers between 1 and 50
arr = np.random.randint(1, 51, 20)

# Print the 1D array
print("1D Array:")
print(arr)

# Reshape into a 4x5 matrix
matrix = arr.reshape(4, 5)

# Print the matrix
print("\n4x5 Matrix:")
print(matrix)

# Print sum, mean, and standard deviation
print("\nSum:", np.sum(matrix))
print("Mean:", np.mean(matrix))
print("Standard Deviation:", np.std(matrix))

# Find maximum value in each row
print("\nMaximum Value in Each Row:")
print(np.max(matrix, axis=1))