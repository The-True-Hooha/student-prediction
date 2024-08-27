
# Introduction to NumPy

## What is NumPy?

NumPy (Numerical Python) is a fundamental library for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a vast collection of high-level mathematical functions to operate on these arrays efficiently.

Key features:

- Fast and efficient multidimensional array object (`ndarray`)
- Tools for integrating C/C++ and Fortran code
- Useful linear algebra, Fourier transform, and random number capabilities

### Importance in Data Science and Scientific Computing

NumPy is crucial because:

1. It provides a foundation for many other libraries (pandas, scipy, scikit-learn)
2. Offers high-performance array operations
3. Enables vectorized operations, reducing loop usage
4. Provides a wide range of mathematical functions

### Difference between Lists and NumPy Arrays

| Lists | NumPy Arrays |
|-------|--------------|
| Can contain elements of different types | Homogeneous (all elements must be the same type) |
| Dynamic size | Fixed size |
| Slower for numerical operations | Optimized for numerical operations |
| More memory-intensive | Memory-efficient |

## Installing NumPy

To install NumPy using pip:

```bash
pip install numpy
```

Verify installation:

```python
import numpy as np
print(np.__version__)
```

## Creating NumPy Arrays

### 1D Arrays

```python
import numpy as np

# From a list
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)  # Output: [1 2 3 4 5]

# Using np.arange()
arr2 = np.arange(0, 10, 2)
print(arr2)  # Output: [0 2 4 6 8]

# Using np.linspace()
arr3 = np.linspace(0, 1, 5)
print(arr3)  # Output: [0.   0.25 0.5  0.75 1.  ]
```

### 2D Arrays

```python
# From a list of lists
arr4 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr4)
# Output:
# [[1 2 3]
#  [4 5 6]]

# Using np.zeros()
arr5 = np.zeros((3, 3))
print(arr5)
# Output:
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]

# Using np.ones()
arr6 = np.ones((2, 4))
print(arr6)
# Output:
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]]
```

## Basic Operations with Arrays

### Element-wise Operations

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Addition
print(a + b)  # Output: [5 7 9]

# Subtraction
print(b - a)  # Output: [3 3 3]

# Multiplication
print(a * b)  # Output: [ 4 10 18]

# Division
print(b / a)  # Output: [4.  2.5 2. ]
```

### Broadcasting

NumPy can perform operations between arrays of different shapes:

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 2

print(arr + scalar)
# Output:
# [[3 4 5]
#  [6 7 8]]
```

### Mathematical Functions

```python
arr = np.array([0, 30, 45, 60, 90])

# Sin function
print(np.sin(arr * np.pi / 180))
# Output: [0.         0.5        0.70710678 0.8660254  1.        ]

# Exponential
print(np.exp(arr))
# Output: [1.00000000e+00 1.06864745e+13 2.81712046e+19 1.14200739e+26 1.22040329e+39]
```

# Array Indexing and Slicing in NumPy

NumPy provides powerful indexing and slicing capabilities for accessing and modifying array elements. Understanding these operations is crucial for efficient data manipulation.

## 1. Basic Indexing

### 1D Arrays

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Accessing elements
print(arr[0])    # Output: 1
print(arr[-1])   # Output: 5 (last element)

# Modifying elements
arr[2] = 10
print(arr)       # Output: [ 1  2 10  4  5]
```

### 2D Arrays

```python
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])


# Accessing elements
print(arr_2d[0, 1])  # Output: 2
print(arr_2d[1][2])  # Output: 6 (alternative syntax)

# Modifying elements
arr_2d[2, 2] = 0
print(arr_2d)
# Output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 0]]
```

## 2. Slicing

Slicing syntax: `array[start:stop:step]`

### 1D Array Slicing

```python
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Basic slicing
print(arr[2:5])    # Output: [2 3 4]
print(arr[:4])     # Output: [0 1 2 3]
print(arr[6:])     # Output: [6 7 8 9]

# Slicing with step
print(arr[1:8:2])  # Output: [1 3 5 7]
print(arr[::-1])   # Output: [9 8 7 6 5 4 3 2 1 0] (reverse array)
```

### 2D Array Slicing

```python
arr_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

# Slicing rows
print(arr_2d[1:])
# Output:
# [[ 5  6  7  8]
#  [ 9 10 11 12]]

# Slicing columns
print(arr_2d[:, 1:3])
# Output:
# [[ 2  3]
#  [ 6  7]
#  [10 11]]

# Combining row and column slicing
print(arr_2d[0:2, 1:3])
# Output:
# [[2 3]
#  [6 7]]
```

## 3. Boolean Indexing

Boolean indexing allows you to select array elements based on conditions.

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Create a boolean mask
mask = arr > 5
print(mask)
# Output: [False False False False False  True  True  True  True  True]

# Use the mask to index the array
print(arr[mask])
# Output: [ 6  7  8  9 10]

# Combine conditions
print(arr[(arr > 3) & (arr < 8)])
# Output: [4 5 6 7]
```
