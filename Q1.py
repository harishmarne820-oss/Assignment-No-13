# Q1: Basic Array Creation

# Import the NumPy library
import numpy as np

# Create a 1D array
arr_1D = np.array([10, 20, 30, 40, 50])

# Print the 1D array
print("1D Array:")
print(arr_1D)
print("Shape:", arr_1D.shape)
print("Data Type:", arr_1D.dtype)

# Create a 2D array (3×3)
arr_2D = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# Print the 2D Array
print("\n2D Array:")
print(arr_2D)
print("Shape:", arr_2D.shape)
print("Data Type:", arr_2D.dtype)