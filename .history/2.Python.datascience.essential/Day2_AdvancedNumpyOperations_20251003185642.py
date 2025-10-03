# 1. Broadcasting in Numpy
    # Broadcasting in NumPy is a powerful mechanism that allows arithmetic operations to be performed on arrays of different shapes. Instead of requiring arrays to have identical dimensions for element-wise operations, NumPy automatically adjusts the shapes of the smaller arrays to make them compatible with the larger arrays. This process occurs without explicitly creating copies of the data, which leads to efficient memory usage and faster computations.
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
    # NumPy provides a rich set of aggregation functions to summarize data in arrays, often returning a single value or an array of reduced dimensions. These functions are highly optimized for performance compared to explicit Python loops.

import numpy as np

arr = np.array([[1,2,3] , [4,5,6]])

print("Sum: ", np.sum(arr))
print("Mean: ", np.mean(arr))
print("Max: ", np.max(arr))
print("Min: ", np.min(arr))
print("Standard Deviation: ", np.std(arr))
print("Sum along rows: ", np.sum(arr, axis=1))
print("Sum along columns: ", np.sum(arr, axis=0))
