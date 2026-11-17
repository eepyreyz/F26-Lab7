# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/11/16
# Purpose: Create Data Frames.
# Usage: ./lab7f.py

import pandas as pd  

# TODO 1: Create dataframe from provided dictionaries in readme.md file.
# - Create a datatable from the three dictionaries provided in the README
data = [
    {"Apple": "Green", "Carrot": "Red", "Radish": "Purple"},
    {"Okra": "Thin", "Potato": "blob", "Radish": "Round"},
    {"Apple": 2.1, "Okra": 3.5, "Carrot": 1.3, "Potato": 2.0, "Radish": 3.0}
]

df = pd.DataFrame(data)
print(df)

# TODO 2: Create a data frame provided in dataframe.jpg file.
students = {
    "student name" : ["A","B","C","D"],
    "student marks" : [22, 344, 55, 77]
}
df2 = pd.DataFrame(students, index = ["Maths", "English", "Urdu", "Science"])
print(df2)

