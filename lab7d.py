# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Slice 2D NumPy Arrays.
# Usage: ./lab7d.py

import numpy as np 

# TODO 1: Create numArray according to instructions given in README.md file.
# - Create a 2D array numArray and initialize it with values given in README
# Creating a 2D NumPy array
arr_2d = np.array([
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100],
    [110, 120, 130, 140, 150],
    [160, 170, 180, 190, 200]])

# array[rows, columns]

# TODO 2: Perform the following operations on numArray as seen in README.md file.
# - Slice the first two rows and the last three columns of arr_2D.  Store result in variable called slice_1
slice_1 = arr_2d[0:2, -3:]
print(slice_1)

# - Extract the middle 2x2 subarray (elements 70, 80, 120, 130) from arr_2D and store it in variable called slice_2
slice_2 = arr_2d[1:3, 1:3]
print(slice_2)

# - Slice ever other row and every other column from arr_2d.  Store the result in a variable called slice_3
# start, stop(to the end), step 2
slice_3 = arr_2d[0::2, 0::2]

