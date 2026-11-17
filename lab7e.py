# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/11/16
# Purpose: Create Series.
# Usage: ./lab7e.py

import pandas as pd

# TODO 1: Create a series according to instructions given in README.md file.
# - Create a series of values   "<50", "50-59", "60-69", "70-79", "80-89", "90-100"
# - Corresponding index names as "F",    "D",     "C",     "B",     "A",     "A+"
grades = pd.Series(
    [      "<50", "50-59", "60-69", "70-79", "80-89", "90-100"],
    index=[ "F",    "D",     "C",     "B",     "A",     "A+"]
)

print(grades)


# TODO 2: Perform the following operations on this series as seen in the README.md file.
# - Write code to print out the values of indices C and A+
print(grades.loc[["C","A+"]])
# - Write code to print value "60-69" without directly printing its index name.
print(grades.iloc[2])

# - Writecode to show the * operation on this list
print(grades * 2 )

