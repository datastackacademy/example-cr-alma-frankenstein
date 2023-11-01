## Independent Project Overview
Before you begin, take a moment to revisit and review the [Independent Projects and Code Reviews](https://www.learnhowtoprogram.com/introduction-to-programming/getting-started-at-epicodus/independent-projects-and-code-reviews) lesson.

## Chapter 7 Code Review #1: Intro to Spark
Just like we did in chapter 1, we'll be profiling, cleaning, and answering questions with the Spotify artists data. This time, we'll be using Spark!

### Setup Git
1. As always, create a repository on GitHub for this project. 
1. Include a README, a `.gitignore` file, a `requirements.txt` file and at least 8 commits.

### Install Requirements
- Include whatever dependencies you need in your requirements.txt.
- Create a virtualenv, activate it, then install the dependencies from your `requirements.txt` file.

### Get Data
For this project, we'll be using the Spotify artists data again. Create a `/data` directory, and get the CSV file:
```bash
gsutil -m cp gs://data.datastack.academy/spotify/spotify_artists.csv .
```

### Project Instructions:
#### Project Setup:
- In a `main.ipynb` file, make an instance of a SparkSession called 'spark'.
- In the header of the data, give the index column a name. Otherwise, you'll get the error "CSVHeaderChecker: CSV header does not conform to the schema".
- Read the Spotify artists CSV file into a Spark DataFrame with the following snippet:
```python
spark_df = (spark.read.format("csv").options(header="true").load("../project-1/data/spotify_artists.csv"))
```

#### Profile the Data:
- Show a description (summary) of the Spark DataFrame.
- Print the schema of the DataFrame.
- Select and show just the first 10 values in the 'name' and 'genres' columns.

#### Clean the Data:
- Where the genre is an empty list, replace it with `['elevator music']`. 
- For the columns 'artist_popularity' and 'followers', cast the data type as integers.
- Sort the data in descending order by number of followers.
- 'artist_popularity' is a rank out of 100. Write a user defined function that will divide each popularity value by 100. Rename the column 'popularity_percent'.

#### Extract Information
- Show only the values in the DataFrame that have 'Queen' in the name.
- Group the data by artist popularity, and show the count for each group.

#### Save as Parquet
- Lastly, write the code to save the DataFrame as a Parquet file in the `/data` directory. Your `/data` directory shouldn't be pushed to GitHub, so this file won't show up in the submitted repository.

### Accepting Criteria

Your submitted repository should:
- Include a completed README, a `requirements.txt` file, a `.gitignore` file, at least 8 commits, and well-commented code with no unused code.
- Complete all the criteria in the 'Profile the Data' section above.
- Complete all the criteria in the 'Clean the Data' section above.
- Complete all the criteria in the 'Extract Information' section above.
- Save the DataFrame as a Parquet file in a `/data` directory.





