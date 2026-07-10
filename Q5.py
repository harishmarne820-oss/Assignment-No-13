# Q5: Random Arrays

# Import NumPy library
import numpy as np

# a) Create a 1D array of 10 random numbers between 0 and 1
arr1 = np.random.rand(10)

# b) Create a 3x3 matrix of random numbers
# from standard normal distribution
arr2 = np.random.randn(3, 3)

# Print the arrays
print("a) 1D Array of 10 Random Numbers (0 to 1):")
print(arr1)

print("\nb) 3x3 Matrix of Random Numbers (Standard Normal Distribution):")
print(arr2)