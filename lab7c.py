# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/11/14
# Purpose: Slice NumPy Arrays.
# Usage: ./lab7c.py

import numpy as np  # Step 1: Import NumPy

# TODO 1: Create numArray according to instructions given in README.md file.
# - Create a 1D array numArray and initialize it with 100 random numbers
numArray = np.random.randint(0,100,100)
print(numArray)
# TODO 2: Perform the follow operations on numArray as seen in README.md file.
# - Slice and print first 10 values
print(numArray[0:10])

# - Slice and print last 10 values
print(numArray[-10:])

# - Slice and print 30 values starting from index 21
print(numArray[21:51])

# - With one statement, change all values to 101 from index 50 to 65.
numArray[50:66] = 101
print(numArray)

