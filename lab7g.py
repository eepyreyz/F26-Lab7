# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/11/16
# Purpose: Create data frame from CSV file.
# Usage: ./lab7g.py

import pandas as pd
import matplotlib.pyplot as plt

# TODO 1: Create a new data frame from the link of csv file provided in README.md file.
link = "https://raw.githubusercontent.com/itiievskyi/IMDB-Top-250/master/imdb_top_250.csv"
df = pd.read_csv(link)
print(df.columns)

# TODO 2: Perform the following operations as demonstrated in the README.md file on this data frame.
# - Print the summary of the data contained in the data frame
print(df.describe())

# - Print first 10 and last 10 rows of this dataframe
print(df.head(10))
print(df.tail(10))

# - Using operation ondata frame print the year of the earliest and latest movie (hint: min function on year column)
print(df["Year"].min())
print(df["Year"].max())

# - Print unique values in the "Genre" column
print(df["Genre"].unique()) 

# - Count how many movies are not made in USA
not_usa_count = 0
for country in df["Origin"]:
    if "USA" not in country:
        not_usa_count+=1
print(f"Movies not made in USA: {not_usa_count}")

# - Find the top 10 Highest-Rated Movies
print(df.head(10)[["Title", "IMDB rating"]]) # The database already sorted

# TODO 3: Find out what the best decade of movies is.  Also display using a scatter plot

# - First define a python  function that getsa decade from the year
def get_decade(year):
    decade = (year // 10) * 10
    return decade


# - Add a decade column to the dataframe
decades = []
for year in df["Year"]:
    decades.append(get_decade(year))
df["Decade"] = decades

# - Group by decade to get the mean rating for each decate
decade_ratings = df.groupby("Decade")["IMDB rating"].mean()

print(decade_ratings)

highest_rating = decade_ratings.max()
for decade in decade_ratings.index:
    if decade_ratings[decade] == highest_rating:
        print("Best decade:", decade)


# - Create a scatterplot using MATPLOT
# plot
fig, ax = plt.subplots()
ax.scatter(decade_ratings.index, decade_ratings.values)
plt.show()

# TODO 4: Run the script and take a screenshot of the result.

