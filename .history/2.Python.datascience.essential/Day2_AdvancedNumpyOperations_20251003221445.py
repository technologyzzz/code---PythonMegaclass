# 1. Broadcasting in Numpy
    # Broadcasting in NumPy is a powerful mechanism that allows arithmetic operations to be performed on arrays of different shapes. 
    # Instead of requiring arrays to have identical dimensions for element-wise operations, NumPy automatically adjusts the shapes of the smaller arrays to make them compatible with the larger arrays. 
    # This process occurs without explicitly creating copies of the data, which leads to efficient memory usage and faster computations.
        # Rules of Broadcasting:
            # For two arrays to be compatible for broadcasting, the following rules must be met when comparing their shapes from right to left (trailing dimensions):
            # Equal Dimensions: The dimensions must be of the same size.
            # One of the Dimensions is One: If the dimensions are not of the same size, one of them must be 1.
            # Padding with Ones: If arrays have a different number of dimensions, the shape of the smaller-dimensional array is padded with ones on its left side until both shapes have the same length. 
"""        
            import numpy as np

            # Array and scalar broadcasting
            arr = np.array([1, 2, 3])
            print(arr + 10) #sum the value into arr

            matrix = np.array([[1, 2, 3] , [4, 5, 6]])
            vector = np.array([1, 0, 1])
            print(matrix + vector) #sum the vector into each matrix
"""

# 2. Aggregation Functions
    # NumPy provides a rich set of aggregation functions to summarize data in arrays, often returning a single value or an array of reduced dimensions. 
    # These functions are highly optimized for performance compared to explicit Python loops.
"""
    import numpy as np

    arr = np.array([[1,2,3] , [4,5,6]])

    print("Sum: ", np.sum(arr))
    print("Mean: ", np.mean(arr))
    print("Max: ", np.max(arr))
    print("Min: ", np.min(arr))
    print("Standard Deviation: ", np.std(arr))
    print("Sum along rows: ", np.sum(arr, axis=1))
    print("Sum along columns: ", np.sum(arr, axis=0))
"""


# 3. Boolean Indexing and Filtering 
    # Boolean indexing, also known as boolean masking, in NumPy is a powerful technique for filtering and selecting elements from arrays based on a condition. 
    # It involves creating a boolean array (a mask) with True and False values, where True indicates that the corresponding element in the original array should be selected, and False indicates it should be excluded.

"""
import numpy as np

arr = np.array([[1,2,3,4,5,6]])


    evens = arr[arr % 2 == 0]
    print("Evens: ", evens)

    arr[arr > 3] = 0 #change values more than 3 to 0
    print("Modified Array: ", arr) 


    # Random Number Generation

    np.random.seed(42)

    random_array = np.random.rand(3, 3)
    print("Random Array: \n", random_array)

    random_integers = np.random.randint(0, 10, size=(2,3))
    print("Random Integers: \n", random_integers)
"""

# HANDS-ON EXERCISES

# 1. Broadcasting Operations
"""
    import numpy as np

    matrix = np.array([[1,2,3], [4,5,6], [7,8,9]])
    vector = np.array([1, 0, -1])

    result_add = matrix + vector
    print("Add: \n", result_add)

    result_mul = matrix * 2
    print("Multiplication: \n", result_mul)
"""

# 2. Generate and Filter a Random Dataset
"""
    import numpy as np

    #generate random dataset
    dataset = np.random.randint(1, 51, size=(5,5))
    print("Original: \n", dataset)

    #filter values > 25 and replace with 0
    dataset[dataset > 25] = 0
    print("Modified Dataset: \n", dataset)

    #calculate summary stats
    print("Sum: ", np.sum(dataset))
    print("Mean: ", np.mean(dataset))
    print("Standard Deviasion: ", np.std(dataset))
"""

# 3. Create a 3D random array and compute statistics along specific axes

import numpy as np

# Generate the array
arr = np.random.rand(3, 3, 3)

print("Original 3D Array Shape:", arr.shape)

print("\n--- Statistics along Axis 0 ---")
print("Sum (axis=0):\n", np.sum(arr, axis=0))
print("Mean (axis=0):\n", np.mean(arr, axis=0))

print("\n--- Statistics along Axis 1 ---")
print("Sum (axis=1):\n", np.sum(arr, axis=1))
print("Mean (axis=1):\n", np.mean(arr, axis=1))

print("\n--- Statistics along Axis 2 ---")
print("Sum (axis=2):\n", np.sum(arr, axis=2))
print("Mean (axis=2):\n", np.mean(arr, axis=2))

# 4. Write a program to generate a dataset of random floats and normalize the values between 0 and 1

# 5. Implement conditional replacement to create a binary mask for values above threshold







