# Q10: Mini Project - Simple Statistics Calculator

# Import NumPy library
import numpy as np

try:
    # Ask the user for the number of random numbers
    n = int(input("Enter how many random numbers you want to generate: "))

    # Generate random numbers between 10 and 100
    arr = np.random.randint(10, 101, n)

    # Print the array
    print("\nGenerated Array:")
    print(arr)

    # Print statistics
    print("\nMean:", np.mean(arr))
    print("Median:", np.median(arr))
    print("Standard Deviation:", np.std(arr))
    print("Minimum:", np.min(arr))
    print("Maximum:", np.max(arr))

    # Reshape into a 2D array if possible
    if n % 2 == 0:
        arr2 = arr.reshape(2, n // 2)
        print("\nReshaped 2D Array:")
        print(arr2)

        print("\nRow-wise Sum:")
        print(np.sum(arr2, axis=1))
    else:
        print("\nCannot reshape into a 2D array because the number of elements is odd.")

except ValueError:
    print("Invalid input! Please enter an integer.")
except Exception as e:
    print("Error:", e)