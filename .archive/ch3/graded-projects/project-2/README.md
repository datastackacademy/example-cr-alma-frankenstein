## Independent Project Overview
Before you begin, take a moment to revisit and review the [Independent Projects and Code Reviews](https://www.learnhowtoprogram.com/introduction-to-programming/getting-started-at-epicodus/independent-projects-and-code-reviews) lesson.

## Chapter 3 Code Review 2: BigQuery
For this code review, you will download a CSV from a dataset on kaggle.com, load that CSV into a Pandas DataFrame, and then upload the data as a table in a BigQuery dataset.

### Setup Git
1. As always, create a repository on GitHub for this project. 
1. Include a README and at least 8 commits.
1. Include a `.gitignore` file that excludes the `data/` directory, or all `.csv` files

### Instructions:

#### Get Data
1. Make a `data/` directory in your repository for this project.
1. View the publicly available datasets at [kaggle.com](https://www.kaggle.com/datasets?fileType=csv) and select one you'd like to work with. This project allows you some creative freedom, so pick something you're interested in!
>Note that some of the datasets have more than one CSV file.
1. Click the 'Download' button in the upper right corner of the Kaggle dataset page, and save the downloaded CSV file to your `data/` directory

#### Load CSV to DataFrame
In a `main.py` file, write a Python script to load your Kaggle CSV file into a Pandas DataFrame. This script may be a simple function.

#### Clean Data
Using Python in a `main.py` file:
1. Drop duplicate rows.
1. Add an index column to your DataFrame if there isn't one already.
1. Datasets from Kaggle may include bad data. Transform your DataFrame in any way you see fit before uploading it on BigQuery.

#### Load Data to BigQuery
Create a dataset for this project on BigQuery and load your data table into it. You may use any method you like. See [chapter 3, episode 7](https://github.com/datastackacademy/data-engineering-bootcamp/tree/main/deb/ch3/ep7) for more instructions on using the BigQuery console and gsutil.

#### Query the Data
1. In your repository, create a SQL file.
1. Using the 'Query' tab in BigQuery, write at least 8 queries on your data. Use each of the following SQL statements at least once:
    - ORDER BY
    - WHERE
    - IN
    - LIKE
    - COUNT
    - MAX
    - GROUP BY
1. Copy each of your SQL queries from BigQuery and paste it into the `.sql` file in your repository. For each query, write a comment explaining what it does, with a brief summary of the results.


### Accepting Criteria

Your submitted repository should include:

1. A _.gitignore_ file to ignore either the entire content of _data/_ folder, or only files ending in _".csv"_

1. A `main.py` file that contains a Python script to load a Kaggle CSV file into a Pandas DataFrame and do any necessary transformations on the data

1. A `.sql` file with at least 8 queries, commented with explanations and a summary of the outputs

1. A README and at least 8 commits. Your code should be readable and well-commented.

