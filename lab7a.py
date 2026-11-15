# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/11/14
# Purpose: Create Arrays.
# Usage: ./lab7a.py

import numpy as np  

# TODO 1: Create array1 and array2 according to instructions given in README.md file.
# - Show two different ways of creating a NumPy array that has integer values from 20 to 49 (including both as well)
numbers = list(range(20, 50))
array1 = np.array(numbers)

array2 = np.arange(20, 50)

print("Array 1:", array1)
print("Array 2:", array2)

# TODO 2: Create array3 according to instructions given in README.md file.
# - Write code that will create a 3x3 matrix containing values from 1 to 9 arranged in 3 rows and three columns.
array3 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("Array 3:", array3)

# TODO 3: Create array4 according to instructions given in README.md file.
# - Write code to create a 3D matrix of shape 2x3x2 and initialize with month names.  
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

