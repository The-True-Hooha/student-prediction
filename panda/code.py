import pandas as pd
# import numpy as np


data = {
    'Name': ['John', 'Emma', 'Ebube', 'Olivia', 'Noah', 'Mike', 'Ethan', 'Sophia', 'Rukky', 'Bella'],
    'Age': [28, 34, 22, 31, 45, 29, 36, 27, 33, 30],
    'City': ['Lagos', 'Warri', 'Asaba', 'Illorin', 'Uyo', 'Calabar', 'Aba', 'Lokoja', 'Markudi', 'Porthacourt'],
    'Salary': [75000, 82000, 60000, 78000, 95000, 72000, 88000, 69000, 81000, 76000],
    'Experience': [3, 7, 1, 5, 12, 4, 8, 2, 6, 4]
}


class DataAssignment:
    
    def __init__(self):
        self.df = pd.DataFrame(data)

    def question1(self):
        # Exercise 1: Create a DataFrame with at least 10 rows and 5 columns of your choice

        # self.df =
        print("Question 1: The created DataFrame")
        print(self.df)
        print("\n" + "="*50 + "\n")

    def question2(self):
        # Read a CSV file and perform basic exploratory data analysis
        self.df.to_csv('employee_data.csv', index=False)

        # Now, let's read the CSV file and perform some basic analysis
        df_from_csv = pd.read_csv('employee_data.csv')

        print("Exercise 2: Basic Exploratory Data Analysis")
        print(df_from_csv.describe())
        print("\nData Types:")
        print(df_from_csv.dtypes)
        print("\nMissing Values:")
        print(df_from_csv.isnull().sum())
        print("\n" + "="*50 + "\n")

    def question3(self):
        # question3 3: Filter the DataFrame to show only rows where a numeric column is above its mean value
        salary_mean = self.df['Salary'].mean()
        high_salary_df = self.df[self.df['Salary'] > salary_mean]

        print("question 3: Filtered DataFrame (Salary > Mean)")
        print(high_salary_df)
        print("\n" + "="*50 + "\n")

    def question4(self):
        # Exercise 4: Sort the DataFrame by two columns of your choice
        sorted_df = self.df.sort_values(
            ['Age', 'Salary'], ascending=[False, True])

        print("Exercise 4: Sorted DataFrame (by Age descending, then Salary ascending)")
        print(sorted_df)
        print("\n" + "="*50 + "\n")

    # def question5(self):
    #     # Exercise 5: Group the data by a categorical column and calculate multiple aggregations on numeric columns
    #     grouped_df = self.df.groupby('City').agg({
    #         'Salary': ['mean', 'min', 'max'],
    #         'Age': ['mean', 'min', 'max'],
    #         'Experience': ['mean', 'min', 'max']
    #     })

        print("Exercise 5: Grouped DataFrame with multiple aggregations")
        print(grouped_df)

# if __name__ == "__main__":


assignment = DataAssignment()
# assignment.question1()
# assignment.question2()
# assignment.question3()
# assignment.question4()
# assignment.question5()


df = pd.DataFrame({
    'color': ['red', 'blue', 'green', 'red', 'blue', 'green', 'red']
})

# Convert to categorical
df['color'] = pd.Categorical(df['color'])

# print(df['color'].dtype)
# print(df['color'].cat.categories)


df['size'] = ['small', 'medium', 'large', 'medium', 'small', 'large', 'small']
print(pd.crosstab(df['color'], df['size']))
