# 1. Understanding the Role of NumPy in Data Science and AI
    
    # NumPy, short for Numerical Python, is a fundamental open-source library in Python for numerical computing. 
    # It provides support for large, multi-dimensional arrays and matrices, along with a comprehensive collection of high-level mathematical functions to operate efficiently on these data structures. 
        #N-dimensional Array Object (ndarray):
            #The core of NumPy is the ndarray object, which efficiently stores homogeneous data of various types (integers, floats, complex numbers, etc.) in N-dimensional arrays. This structure enables fast and memory-efficient operations compared to standard Python lists for numerical data.
        #Efficient Operations:
            #NumPy's operations are often implemented in optimized, pre-compiled C or Fortran code, leading to significant performance advantages for numerical computations on large datasets.
        #Mathematical Functions:
            #It offers a vast library of functions for various mathematical operations, including linear algebra, statistics, Fourier transforms, random number generation, and more, all designed to work efficiently with ndarray objects.
        #Broadcasting:
            #This powerful feature allows NumPy to perform operations on arrays of different shapes and sizes, automatically expanding smaller arrays to match the dimensions of larger ones when possible, simplifying code and enhancing efficiency.
        #Integration:
            #NumPy serves as the foundation for many other scientific computing and data analysis libraries in Python, such as SciPy, Pandas, and Matplotlib, facilitating a robust ecosystem for various numerical tasks.

# 2. Creating and Manipulating NumPy Arrays
"""
        #creating arrays
    import numpy as np #import

    arr = np.array([1,2,3,4]) #creating array
    print(arr)

    zeroes = np.zeroes((3,3)) #built-in functions for 3.3matrix
    print(zeroes)

    ones = np.ones((2,4)) #built-in functions for 2.4matrix
    print(ones)

    range_array = np.arrange(1, 10, 2) #built-in functions for skips linear pattern
    print(range_array)

    linspace_array = np.linspace(0, 1, 5) #built-in functions for provide number division in between
    print(linespace_array)

        #manipulating arrays

    import numpy as np

    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    reshaped = arr.reshape((2,3)) #create 2.3 matrix with variable's list value in it
    print(reshaped)

    arr = np.array([1, 2, 3])
    expanded = arr[:, np.newaxis] #create matrix newaxis every variable's list value
    print(expanded)
"""

# 3. Basic Operations on Arrays
"""
    import numpy as np

    #matrix operation
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print(a + b)
    print(a * b)
    print(a / b)

    arr = np.array([4, 16, 25])
    print(np.sqrt(arr)) #division square
    print(np.sum(arr)) #sum
    print(np.mean(arr)) #mean
    print(np.max(arr)) #max
"""

# 4. Array Indexing, Slicing, and Reshaping
"""
    import numpy as np

    arr = np.array([10, 20, 30, 40, 50, 60])
    print(arr[2]) #30 #array list index
    print(arr[-1]) #60

    print(arr[1:4]) # 20 30 40 index from 1-3
    print(arr[:3]) # 10 20 30 index before 3

    reshaped = arr.reshape(2,3) #reshape
    print(reshaped)
"""
# HANDS-ON EXERCISES

# 1. Generate Arrays for Basic Mathematical Operations
"""
    import numpy as np

    a = np.arrange(1, 6)
    b = np.arrange(6,11)

    print(a)
    print(b)

    print("Add: ", a + b)
    print("Sub: ", a - b)
    print("Mult: ", a * b)
    print("Div: ", a / b)
"""
# 2. Create a 3.3 Marix and Perform Operations 
"""
    import numpy as np 

    matrix = np.array([1, 2, 3], [4, 5, 6], [7, 8, 9])
    print("Original Matrix: \n", matrix)

    #transpose (reflecting the matrix from horizontal to vertical)
    transpose  = matrix.T 
    print("Transpose:\n", transpose)

    another_matrix = np.array([9,8,7], [6,5,4], [3,2,1])
    print("Addition: \n", matrix + another_matrix)
    print("Multiplication: \n", matrix * another_matrix)
"""

# 4. Create 4.4 matrix and calculate the sum of its rows and columns

import numpy as np

# Create a 4x4 matrix
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

print("Original 4x4 Matrix:")
print(matrix)
print()

# Calculate row sums (sum of elements in each row)
row_sums = np.sum(matrix, axis=1)
print("Row sums:")
for i, row_sum in enumerate(row_sums):
    print(f"Row {i+1} sum: {row_sum}")

print()

# Calculate column sums (sum of elements in each column)
col_sums = np.sum(matrix, axis=0)
print("Column sums:")
for i, col_sum in enumerate(col_sums):
    print(f"Column {i+1} sum: {col_sum}")

print()

# Additional operations
print("Additional Matrix Operations:")
print(f"Total sum of all elements: {np.sum(matrix)}")
print(f"Matrix shape: {matrix.shape}")
print(f"Matrix determinant: {np.linalg.det(matrix)}")



# 5. Write a program to normalize an array(scale values between 0 and 1

import numpy as np

def normalize_array(arr):
    """
    Normalize an array to scale values between 0 and 1.
    
    Args:
        arr: Input array to normalize
        
    Returns:
        Normalized array with values between 0 and 1
    """
    # Calculate min and max values
    min_val = np.min(arr)
    max_val = np.max(arr)
    
    # Avoid division by zero (if all values are the same)
    if max_val == min_val:
        return np.zeros_like(arr)
    
    # Apply normalization formula: (x - min) / (max - min)
    normalized = (arr - min_val) / (max_val - min_val)
    
    return normalized

# Example usage
if __name__ == "__main__":
    # Create a sample array
    original_array = np.array([10, 20, 30, 40, 50])
    print("Original array:", original_array)
    
    # Normalize the array
    normalized_array = normalize_array(original_array)
    print("Normalized array:", normalized_array)
    
    # Verify the range
    print("Min value in normalized array:", np.min(normalized_array))
    print("Max value in normalized array:", np.max(normalized_array))
    
    # Test with a 2D array
    matrix = np.random.randint(0, 100, size=(3, 4))
    print("\nOriginal 2D array:")
    print(matrix)
    
    normalized_matrix = normalize_array(matrix)
    print("\nNormalized 2D array:")
    print(normalized_matrix)
    
    print("\nRange of normalized 2D array:")
    print("Min:", np.min(normalized_matrix))
    print("Max:", np.max(normalized_matrix))




# 6. Generate a random array and find the minum and maxium values

import numpy as np

# Generate a random array with 10 elements between 0 and 100
random_array = np.random.randint(0, 101, size=10)

print("Random Array:", random_array)

# Find minimum and maximum values
min_value = np.min(random_array)
max_value = np.max(random_array)

print("Minimum value:", min_value)
print("Maximum value:", max_value)

# Additional information
print("Array shape:", random_array.shape)
print("Array size:", random_array.size)
print("Array dtype:", random_array.dtype)



#2D ARRAY
import numpy as np

# Generate a random 3x4 matrix with values between 0 and 100
random_matrix = np.random.randint(0, 101, size=(3, 4))

print("Random Matrix:")
print(random_matrix)

# Find minimum and maximum values
min_value = np.min(random_matrix)
max_value = np.max(random_matrix)

print("\nMinimum value:", min_value)
print("Maximum value:", max_value)

# Find min/max along specific axes
row_mins = np.min(random_matrix, axis=1)
row_maxs = np.max(random_matrix, axis=1)
col_mins = np.min(random_matrix, axis=0)
col_maxs = np.max(random_matrix, axis=0)

print("\nRow minimums:", row_mins)
print("Row maximums:", row_maxs)
print("Column minimums:", col_mins)
print("Column maximums:", col_maxs)
