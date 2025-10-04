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

import numpy as np

def generate_and_normalize_dataset(size=100, low=0.0, high=100.0):
    """
    Generate a dataset of random floats and normalize values between 0 and 1.
    
    Args:
        size (int or tuple): Size of the dataset (can be 1D, 2D, or 3D)
        low (float): Lower bound for random values
        high (float): Upper bound for random values
        
    Returns:
        tuple: (original_data, normalized_data, stats_dict)
    """
    # Generate random floats
    original_data = np.random.uniform(low, high, size=size)
    
    # Calculate statistics before normalization
    stats = {
        'original_min': np.min(original_data),
        'original_max': np.max(original_data),
        'original_mean': np.mean(original_data),
        'original_std': np.std(original_data)
    }
    
    # Normalize the data (min-max scaling)
    normalized_data = (original_data - stats['original_min']) / (stats['original_max'] - stats['original_min'])
    
    # Calculate statistics after normalization
    stats['normalized_min'] = np.min(normalized_data)
    stats['normalized_max'] = np.max(normalized_data)
    stats['normalized_mean'] = np.mean(normalized_data)
    stats['normalized_std'] = np.std(normalized_data)
    
    return original_data, normalized_data, stats

def print_comparison(original, normalized, stats, title=""):
    """Print comparison between original and normalized data."""
    if title:
        print(f"\n{title}")
        print("=" * 50)
    
    print(f"Original data shape: {original.shape}")
    print(f"First 10 original values: {original.flatten()[:10]}")
    print(f"Original - Min: {stats['original_min']:.4f}, Max: {stats['original_max']:.4f}, "
          f"Mean: {stats['original_mean']:.4f}, Std: {stats['original_std']:.4f}")
    
    print(f"\nNormalized data shape: {normalized.shape}")
    print(f"First 10 normalized values: {normalized.flatten()[:10]}")
    print(f"Normalized - Min: {stats['normalized_min']:.4f}, Max: {stats['normalized_max']:.4f}, "
          f"Mean: {stats['normalized_mean']:.4f}, Std: {stats['normalized_std']:.4f}")

# Example usage
if __name__ == "__main__":
    print("Dataset Generation and Normalization")
    print("=" * 50)
    
    # Example 1: 1D array
    original_1d, normalized_1d, stats_1d = generate_and_normalize_dataset(size=20, low=10, high=50)
    print_comparison(original_1d, normalized_1d, stats_1d, "1D Array Example")
    
    # Example 2: 2D array
    original_2d, normalized_2d, stats_2d = generate_and_normalize_dataset(size=(5, 4), low=-5, high=5)
    print_comparison(original_2d, normalized_2d, stats_2d, "2D Array Example")
    
    # Example 3: 3D array
    original_3d, normalized_3d, stats_3d = generate_and_normalize_dataset(size=(2, 3, 4), low=0, high=1000)
    print_comparison(original_3d, normalized_3d, stats_3d, "3D Array Example")
    
    # Example 4: Large dataset visualization
    print("\n" + "=" * 50)
    print("Large Dataset Statistics")
    print("=" * 50)
    
    large_original, large_normalized, large_stats = generate_and_normalize_dataset(size=1000, low=-100, high=100)
    
    print(f"Large dataset size: {large_original.shape}")
    print(f"Original range: [{large_stats['original_min']:.2f}, {large_stats['original_max']:.2f}]")
    print(f"Normalized range: [{large_stats['normalized_min']:.2f}, {large_stats['normalized_max']:.2f}]")
    print(f"Mean before normalization: {large_stats['original_mean']:.4f}")
    print(f"Mean after normalization: {large_stats['normalized_mean']:.4f}")
    
    # Verify normalization worked correctly
    print("\nVerification:")
    print(f"All normalized values ≥ 0: {np.all(large_normalized >= 0)}")
    print(f"All normalized values ≤ 1: {np.all(large_normalized <= 1)}")
    print(f"Contains 0: {np.any(large_normalized == 0)}")
    print(f"Contains 1: {np.any(large_normalized == 1)}")








# 5. Implement conditional replacement to create a binary mask for values above threshold

import numpy as np

def create_binary_mask(data, threshold):
    """
    Create a binary mask where values above threshold become 1, others become 0.
    
    Args:
        data: Input array
        threshold: Value threshold for binary classification
        
    Returns:
        Binary mask array with the same shape as input
    """
    # Method 1: Direct boolean to integer conversion
    mask = (data > threshold).astype(int)
    
    return mask

def create_binary_mask_with_conditions(data, conditions):
    """
    Create binary mask with multiple conditions.
    
    Args:
        data: Input array
        conditions: List of tuples (operator, value) 
                   e.g., [('>', 5), ('<', 10)] for values between 5 and 10
        
    Returns:
        Binary mask array
    """
    mask = np.ones_like(data, dtype=int)  # Start with all ones
    
    for operator, value in conditions:
        if operator == '>':
            mask = mask & (data > value)
        elif operator == '>=':
            mask = mask & (data >= value)
        elif operator == '<':
            mask = mask & (data < value)
        elif operator == '<=':
            mask = mask & (data <= value)
        elif operator == '==':
            mask = mask & (data == value)
        elif operator == '!=':
            mask = mask & (data != value)
    
    return mask.astype(int)

# Example usage and demonstration
if __name__ == "__main__":
    # Generate sample data
    np.random.seed(42)  # For reproducible results
    data = np.random.randint(0, 100, size=(5, 5))
    
    print("Original Data:")
    print(data)
    print()
    
    # Example 1: Simple threshold
    threshold = 50
    binary_mask = create_binary_mask(data, threshold)
    
    print(f"Binary Mask (values > {threshold}):")
    print(binary_mask)
    print()
    
    # Example 2: Using the mask to extract values
    values_above_threshold = data * binary_mask  # Element-wise multiplication
    print(f"Values above {threshold}:")
    print(values_above_threshold)
    print()
    
    # Example 3: Multiple conditions
    print("Advanced Conditional Masking:")
    data_float = np.random.rand(4, 4) * 100
    print("Float Data:")
    print(data_float)
    
    # Create mask for values between 25 and 75
    conditions = [('>=', 25), ('<=', 75)]
    range_mask = create_binary_mask_with_conditions(data_float, conditions)
    
    print("\nMask for values between 25 and 75:")
    print(range_mask)
    print("Values in range 25-75:")
    print(data_float * range_mask)
    
    # Example 4: Using np.where for conditional replacement
    print("\n" + "="*50)
    print("Using np.where() for Conditional Replacement")
    print("="*50)
    
    # Replace values above threshold with 1, others with 0
    mask_where = np.where(data > threshold, 1, 0)
    print(f"Mask using np.where (values > {threshold}):")
    print(mask_where)
    
    # More complex replacement: above threshold -> 'HIGH', below -> 'LOW'
    labels = np.where(data > threshold, 'HIGH', 'LOW')
    print("\nLabeled data:")
    print(labels)
    
    # Example 5: Statistical analysis with masks
    print("\n" + "="*50)
    print("Statistical Analysis with Binary Mask")
    print("="*50)
    
    # Create a larger dataset for analysis
    large_data = np.random.normal(50, 20, 1000)  # Normal distribution
    
    # Create masks for different percentiles
    percentile_25 = np.percentile(large_data, 25)
    percentile_75 = np.percentile(large_data, 75)
    
    mask_bottom_25 = create_binary_mask_with_conditions(large_data, [('<=', percentile_25)])
    mask_top_25 = create_binary_mask_with_conditions(large_data, [('>=', percentile_75)])
    
    print(f"Dataset statistics:")
    print(f"Mean: {np.mean(large_data):.2f}")
    print(f"Std: {np.std(large_data):.2f}")
    print(f"25th percentile: {percentile_25:.2f}")
    print(f"75th percentile: {percentile_75:.2f}")
    print(f"Values in bottom 25%: {np.sum(mask_bottom_25)}")
    print(f"Values in top 25%: {np.sum(mask_top_25)}")
    
    # Example 6: Image-like binary masking
    print("\n" + "="*50)
    print("Image-like Binary Masking Example")
    print("="*50)
    
    # Create an image-like array (grayscale values 0-255)
    image_data = np.random.randint(0, 256, size=(8, 8))
    print("Original 'image' data:")
    print(image_data)
    
    # Create mask for bright pixels (above 200)
    bright_mask = create_binary_mask(image_data, 200)
    print("\nBright pixels mask (values > 200):")
    print(bright_mask)
    
    # Count bright pixels
    bright_pixel_count = np.sum(bright_mask)
    total_pixels = image_data.size
    bright_percentage = (bright_pixel_count / total_pixels) * 100
    
    print(f"\nBright pixel analysis:")
    print(f"Total pixels: {total_pixels}")
    print(f"Bright pixels: {bright_pixel_count}")
    print(f"Percentage bright: {bright_percentage:.1f}%")






