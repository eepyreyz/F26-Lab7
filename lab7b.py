# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/11/14
# Purpose: Change Dimensions and create special arrays.
# Usage: ./lab7b.py

import numpy as np  

# TODO 1: Copy the code from your lab7a.py file and paste here.
numbers = list(range(20, 50))
array1 = np.array(numbers)

array2 = np.arange(20, 50)

print("Array 1:", array1)
print("Array 2:", array2)

array3 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
array4 = np.array([
    [
        ["Januray", "February"],
        ["March", "April"],
        ["May", "June"]
    ],
    [
        ["July","August"],
        ["September","October"],
        ["November", "December"]
    ]
])

# TODO 2: Reshape array 1 into a 5x6 shape.   
array1_reshaped = np.reshape(array1, (5, 6))
print(array1_reshaped)

# TODO 3: Reshape array 2 into a 2x3x5 matrix
array2_reshaped = np.reshape(array2,(2,3,5))
print(array2_reshaped)

# TODO 4: Create array5 according to instructions given in README.md file.
# - Create a matrix that has 5 rows and 5 columns and initialize diagonal values to (45, 7, 61, 8, 9).  The rest of the values should be zeros
array5 = np.diag([45, 7, 61, 8, 9])
print(array5)

# TODO 5: Create array6 according to instructions given in README.md file.
# - Create a 7x7 matrix and initialize with values sampled from a normal distribution
array6 = np.random.randn(7,7)
print(array6)



