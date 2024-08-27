# Day 2: Introduction to pandas

## 1. Introduction to pandas

pandas is a powerful Python library for data manipulation and analysis. It provides high-performance, easy-to-use data structures and tools for working with structured data.

### How To Install

`pip install pandas`

Key features of pandas:

- Fast and efficient DataFrame object
- Tools for reading and writing data between in-memory data structures and different file formats
- Intelligent data alignment and integrated handling of missing data
- Reshaping and pivoting of datasets
- Powerful group by functionality for performing split-apply-combine operations on datasets
- Robust time series functionality

## 2. Core Data Structures: DataFrames and Series

### 2.1 Series

A Series is a one-dimensional labeled array capable of holding data of any type (integers, floats, strings, Python objects, etc.).

Example:

```python
import pandas as pd

# Creating a Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# output
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
```

### 2.2 DataFrame

A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.

Example:

```python
# Creating a DataFrame

data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 34, 29, 32],
        'City': ['New York', 'Paris', 'Berlin', 'London']}
df = pd.DataFrame(data)
print(df)

#output
Name  Age      City
0   John   28  New York
1   Anna   34     Paris
2  Peter   29    Berlin
3  Linda   32    London
```

### Reading and Writing Data

pandas provides various functions to read and write data in different formats.

CSV Files
Reading CSV:

```py
# reading the csv file
df = pd.read_csv('file.csv')

# writing to a csv file
df.to_csv('output.csv', index=False)

#reading excel files
df = pd.read_excel('file.xlsx', sheet_name='Sheet1')

# writing excel files
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)

#reading json files
df = pd.read_json('file.json')

# writing to json
df.to_json('output.json', orient='records')
```

## 4. Basic Data Operations

### 4.1 Filtering

Filtering allows you to select specific rows based on conditions.

```py
# Select all rows where Age is greater than 30
filtered_df = df[df['Age'] > 30]
print(filtered_df)

# Select all rows where Age is greater than 30
filtered_df = df[df['Age'] > 30]
print(filtered_df)


# Sort the DataFrame by Age in descending order
sorted_df = df.sort_values('Age', ascending=False)
print(sorted_df)


# Grouping allows you to split the data into groups based on some criteria and apply a function to each group.
# Group by City and calculate mean Age
grouped = df.groupby('City')['Age'].mean()
print(grouped)

### Strings And Categorical Data
# Pandas String and Categorical Data Handling Guide

## Table of Contents
1. [Handling Strings in Pandas](#handling-strings-in-pandas)
2. [Handling Categorical Variables in Pandas](#handling-categorical-variables-in-pandas)

## Handling Strings in Pandas

### How to handle strings using Pandas

Pandas provides a variety of string methods that can be accessed using the `str` accessor on Series objects.

```python
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'text': ['Hello, World!', 'Python is awesome', 'Data Science is fun', 'Pandas makes life easier']
})

# Convert to lowercase
df['lowercase'] = df['text'].str.lower()

print(df)
```

### How to perform text analysis using Pandas

You can use string methods to analyze text data, such as counting occurrences or checking for substrings.

```python
# Count occurrences of a word
df['contains_is'] = df['text'].str.contains('is')
df['word_count'] = df['text'].str.split().str.len()

print(df)
```

### How to extract information from text using Pandas

Use string methods or regular expressions to extract specific information from text.

```python
# Extract the first word
df['first_word'] = df['text'].str.split().str[0]

print(df)
```

### How to apply regular expressions using Pandas

Pandas integrates well with Python's `re` module for applying regular expressions.

```python
import re

# Extract words starting with 'P'
df['p_words'] = df['text'].str.findall(r'\b[Pp]\w+')

print(df)
```

### How to split and join strings using Pandas

Splitting and joining strings is straightforward with pandas string methods.

```python
# Split text into words
df['words'] = df['text'].str.split()

# Join words with a hyphen
df['hyphenated'] = df['words'].str.join('-')

print(df)
```

### How to replace and remove characters using Pandas

Use `str.replace()` to substitute characters or patterns, and `str.strip()` to remove leading/trailing characters.

```python
# Replace 'is' with 'was'
df['replaced'] = df['text'].str.replace('is', 'was')

# Remove leading and trailing whitespace
df['stripped'] = df['text'].str.strip()

print(df)
```

## Handling Categorical Variables in Pandas

### Categorical Variables?

Categorical Variables:Categorical variables have a fixed number of possible values, often referred to as "categories" or "levels." For example, a column representing the day of the week would have categories like "Monday," "Tuesday," etc.

### Ordered vs. Unordered Categories

1. Unordered (Nominal): The categories do not have a specific order. For example, the color of a car (e.g., "Red," "Blue," "Green") is a categorical variable without any inherent order.

2. Ordered (Ordinal): The categories have a meaningful order or ranking. For example, the size of a T-shirt (e.g., "Small," "Medium," "Large") is a categorical variable with an inherent order.

3. Memory Efficiency: Storing data categorically rather than as strings can be more memory efficient, especially when there are repeated values. Pandas will store each category only once and use a reference to that category in the DataFrame.
Pandas provides a special data type called Categorical for handling categorical variables. When a column is converted to this type, Pandas treats the data differently, optimizing memory usage and providing specific methods for categorical operations.

Categorical variables can be created using the `Categorical` data type in pandas.

```python
import pandas as pd

# Create a sample DataFrame with a categorical variable
df = pd.DataFrame({
    'color': ['red', 'blue', 'green', 'red', 'blue', 'green', 'red']
})

# Convert to categorical
df['color'] = pd.Categorical(df['color'])

print(df['color'].dtype)
print(df['color'].cat.categories)
```

### How to perform categorical analysis using Pandas

You can use various methods to analyze categorical data, such as value counts and cross-tabulation.

```python
# Value counts
print(df['color'].value_counts())

# Cross-tabulation
df['size'] = ['small', 'medium', 'large', 'medium', 'small', 'large', 'small']
print(pd.crosstab(df['color'], df['size']))
```

### How to encode and decode categories using Pandas

Encoding converts categories to numeric values, while decoding does the reverse.

```python
# Encode categories
df['color_code'] = df['color'].cat.codes

# Decode categories
df['color_name'] = df['color_code'].map(dict(enumerate(df['color'].cat.categories)))

print(df)
```

### How to compare and order categories using Pandas

You can set an order for categories and then use comparison operations.

```python
# Set category order
df['color'] = pd.Categorical(df['color'], categories=['red', 'blue', 'green'], ordered=True)

# Compare categories
print(df[df['color'] > 'blue'])
```

### How to rename categories using Pandas

Use the `rename_categories()` method to change category names.

```python
# Rename categories
df['color'] = df['color'].cat.rename_categories({'red': 'crimson', 'blue': 'azure', 'green': 'emerald'})

print(df['color'].cat.categories)
```

This guide covers the basics of handling strings and categorical variables in pandas. Remember to import pandas (`import pandas as pd`) at the beginning of your script when using these examples.

### Practice Exercises

1. Create a DataFrame with at least 10 rows and 5 columns of your choice.
2. Read a CSV file of your choice and perform basic exploratory data analysis.
3. Filter the DataFrame to show only rows where a numeric column is above its mean value.
4. Sort the DataFrame by two columns of your choice.
5. Group the data by a categorical column and calculate multiple aggregations on numeric columns.

### Solutions

```py
import pandas as pd
import numpy as np

# Exercise 1: Create a DataFrame with at least 10 rows and 5 columns of your choice
data = {
    'Name': ['John', 'Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'Ethan', 'Sophia', 'Mason', 'Isabella'],
    'Age': [28, 34, 22, 31, 45, 29, 36, 27, 33, 30],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'],
    'Salary': [75000, 82000, 60000, 78000, 95000, 72000, 88000, 69000, 81000, 76000],
    'Experience': [3, 7, 1, 5, 12, 4, 8, 2, 6, 4]
}

df = pd.DataFrame(data)
print("Exercise 1: Created DataFrame")
print(df)
print("\n" + "="*50 + "\n")

# Exercise 2: Read a CSV file and perform basic exploratory data analysis
# For this example, we'll create a CSV file first
df.to_csv('employee_data.csv', index=False)

# Now, let's read the CSV file and perform some basic analysis
df_from_csv = pd.read_csv('employee_data.csv')

print("Exercise 2: Basic Exploratory Data Analysis")
print(df_from_csv.describe())
print("\nData Types:")
print(df_from_csv.dtypes)
print("\nMissing Values:")
print(df_from_csv.isnull().sum())
print("\n" + "="*50 + "\n")

# Exercise 3: Filter the DataFrame to show only rows where a numeric column is above its mean value
salary_mean = df_from_csv['Salary'].mean()
high_salary_df = df_from_csv[df_from_csv['Salary'] > salary_mean]

print("Exercise 3: Filtered DataFrame (Salary > Mean)")
print(high_salary_df)
print("\n" + "="*50 + "\n")

# Exercise 4: Sort the DataFrame by two columns of your choice
sorted_df = df_from_csv.sort_values(['Age', 'Salary'], ascending=[False, True])

print("Exercise 4: Sorted DataFrame (by Age descending, then Salary ascending)")
print(sorted_df)
print("\n" + "="*50 + "\n")

# Exercise 5: Group the data by a categorical column and calculate multiple aggregations on numeric columns
grouped_df = df_from_csv.groupby('City').agg({
    'Salary': ['mean', 'min', 'max'],
    'Age': ['mean', 'min', 'max'],
    'Experience': ['mean', 'min', 'max']
})

print("Exercise 5: Grouped DataFrame with multiple aggregations")
print(grouped_df)
```
