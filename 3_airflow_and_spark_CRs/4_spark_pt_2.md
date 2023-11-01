## Independent Project Overview
Before you begin, take a moment to revisit and review the [Independent Projects and Code Reviews](https://www.learnhowtoprogram.com/introduction-to-programming/getting-started-at-epicodus/independent-projects-and-code-reviews) lesson.

## Code Review: Spark 2
This project creates a start-to-finish pipline using Spark to organize [Kaggle.com data about daily coffee prices on the stock market](https://www.kaggle.com/datasets/psycon/daily-coffee-price), and use that data to answer questions about the prices of coffee shares on the stock market.
Please name the submitted file `main`. It can be either a Python or a notebook file.

### Setup Git
1. As always, create a repository on GitHub for this project. 
1. Include a README, a `.gitignore` file, a `requirements.txt` file and at least 8 commits.

### Install Requirements
- Include whatever dependencies you need in your requirements.txt.
- Create a virtualenv, activate it, then install the dependencies in your `requirements.txt` file.

### Get the Data:
Create a `/data` directory, and download the coffee data in it:
```bash
gsutil -m cp gs://data.datastack.academy/coffee_price/coffee.csv .
```

### Instructions:
#### Set Up the Data
- Read the coffee data CSV file into a Spark DataFrame.
- All the columns should be floats except for the 'Date' and 'Currency' columns.

#### Columns from Aggregate Functions
- Add a column to the DataFrame where the values are the difference between 'Open' and 'Close'.
- Add a column to the DataFrame where the values are the difference between 'High' and 'Low'.
- Add a column to the DataFrame where the values are 'True' if the volume for that day was 100 or above, and otherwise 'False'.

- Once you have a column for the difference between 'Open' and 'Close', add another column that contains the absolute values of the numbers in that column.

    - Note: Absolute value is how far a number is from zero; it ignores whether a number is positive or negative. The Python standard library has a built-in function for this.
- Compute a column called _net\_sales_ which is the average of opening, high, low, and closing cost times the volume: net_sales = avg(opening, high, low, closing price) * volume

#### Stats
- Find the average of the values in the column that has the absolute values of the difference between 'Open' and 'Close'.
- Get the count of values where the 'Volume' was less than 100.
- Find the average 'Open' value.
- Get the highest 'High' value.

#### Write File
- Write the code to save the DataFrame with the four new columns created above as a Parquet file in the `/data` directory. This directory won't be pushed to GitHub.


### Accepting Criteria
Your submitted repository should:
- Include a completed README, a requirements.txt file, a .gitignore file, at least 8 commits, and well-commented code with no unused code.
- Create a DataFrame that includes the five columns of aggregate data created above.
- Include code to find the statistical values listed above.
- Include code to write the final DataFrame to a Parquet file.


#### Three Point Bonus 1
Use Matplotlib to create a visualization (i.e. a chart) using the coffee data.

#### Three Point Bonus 2
Include code in the pipeline to write the Parquet file to BigQuery.

