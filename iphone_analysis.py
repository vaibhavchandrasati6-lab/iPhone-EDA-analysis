# Importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the CSV file
df = pd.read_csv('apple_products.csv', encoding_errors='ignore')

# Display first 5 rows of dataset
print(df.head())

# Display column names
print(df.columns)

# Display dataset information (data types, null values etc.)
print(df.info())


# Function to extract only numeric value from RAM column
# Example: "8 GB" -> "8"
def changetoint(value):
    s = str(value).split(' ')   # Split by space
    value = s[0]               # Take first part (number)
    return value


# Apply function to clean RAM column
df['Ram'] = df['Ram'].apply(changetoint)
print(df['Ram'])

# Convert RAM column from object to integer
df['Ram'] = df['Ram'].astype('int')
print(df['Ram'].dtype)


# Sorting data by Star Rating (highest first)
highest_rated = df.sort_values(by=['Star Rating'], ascending=False)

# Selecting top 10 highest rated products
highest_rated = highest_rated.head(10)

# Print only Product Names of top 10
print(highest_rated['Product Name'])


# Again sorting and selecting top 10 (this part is repeated but okay for practice)
highest_rated = df.sort_values(by=['Star Rating'], ascending=False)
highest_rated = highest_rated.head(10)

# Print Product Name and Number Of Ratings
print(highest_rated[['Product Name', 'Number Of Ratings']])


# Display selected columns
print(df.columns)
print(df[['Product Name', 'Number Of Reviews']])


# Scatter plot: Relationship between Number Of Ratings and Sale Price
plt.figure(figsize=(8,5))
sns.scatterplot(x='Number Of Ratings', y='Sale Price', data=df, marker='o')
plt.show()


# Scatter plot: Relationship between Discount Percentage and Number Of Ratings
plt.figure(figsize=(8,5))
sns.scatterplot(x='Discount Percentage', y='Number Of Ratings', data=df, marker='o')
plt.show()


# Finding most expensive product using idxmax()
most_expensive = df.loc[df['Sale Price'].idxmax()]

# Finding least expensive product using idxmin()
least_expensive = df.loc[df['Sale Price'].idxmin()]

print("Most expensive product:")
print(most_expensive)

print("Least expensive product:")
print(least_expensive)
