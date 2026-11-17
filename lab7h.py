# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date:
# Purpose: Create Histograms.
# Usage: ./lab7h.py

import matplotlib.pyplot as plt
import pandas as pd

# TODO 1: Create a new data frame from the link of csv file provided in README.md file.
# TODO 1: Create a new data frame from the link of csv file provided in README.md file.
link = "https://raw.githubusercontent.com/itiievskyi/IMDB-Top-250/master/imdb_top_250.csv"
df = pd.read_csv(link)
print(df.columns)

# TODO 2: Perform the operations provided in readme.md file on this data.
# - Copy year column in a new series


# - Sort years data in ascending order


# - Process this sorted years data to find unique year and number of times a year occurs


# - Draw a histogram with X-axis as the years and bar height equal to corresponding count.  
    # - If number of unique years is very large, only display histogram for first 10 years



# TODO 3: Run the script and take a screenshot of the result.

