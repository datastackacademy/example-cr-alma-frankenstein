# Challenge project
To wrap up this week, we will be completing a **NON-GRADED** challenge project. This will give us a lower pressure way tie together all the concepts we've learned in this chapter using a familiar dataset. We will use the same format as our usual projects.

The goal of this project is to use **Spark** to process the Spotify dataset we have been using and output the fully cleaned and processed data as parquet files, ready for upload to BigQuery.

## Git
As usual, create a new git project for this challenge. As you complete the script(s) and supporting files, be sure to update your README.md to explain their contents and how to run them.

## Data
We will once again be working from the three CSVs of Spotify data and the JSON file with new track data. The `data/` directory contains a `get_data.sh` script that will pull them from GCS using `gsutil`. After running the script, you should have the following files in your `data/` directory:
- `spotify_albums.csv`
- `spotify_artists.csv`
- `spotify_tracks.csv`
- `new_tracks.json`

These are exactly as seen in earlier chapters, so you should be familiar with their format and contents. If you'd like a refresher, [please refer to the Chapter 2 graded project](/deb/ch2/graded-project/README.md) and the [Chapter 3, week 1 graded project](/deb/ch3/graded-projects/project-1/README.md).

## Accepting criteria
Our goal is to create a script that replicates the data pipeline we created in Chapter 2 & 3 graded projects but uses Spark to do the data processing. As such, the following steps will look very familiar, but they will serve to reinforce your ability to make Spark pipelines.
1. Create a Spark script with the following steps:
    1. Read all the 3 CSVs into Spark DataFrames using SparkSQL.
    1. Clean the data:
        1. Drop the following columns from all DataFrames: `available_markets`, `images`, `external_urls`, and `Unnamed`.
        1. Drop the `track_id`, `track_name_prev` columns from `albums` and `artists`. This data set has put an arbitrary track in each of the spots for the artist and album.
        1. Drop the `lyrics` column from `tracks`
        1. Convert any `date` column to a datetime data type.
        1. For columns that are lists like `genre` in our `artists` data, make sure the data type of your column is `ArrayType`
    1. Read the `new_tracks.json` file into a Spark DataFrame.
        1. Clean and format these data to match your `tracks` data from CSV.
        1. Merge this new data into your existing `tracks` DataFrame, adding new tracks and updating any already present.
    1. Write all 3 datasets as parquet files.
1. Run your script with the local Spark engine.

Analysis extension:
Now that our data is all nice and processed, let's use SparkSQL's API to answer the same analytical questions we tackled in Chapter 2 but with the updated track data.
1. Create a Spark script to load your parquet files and answer the following questions:
    1. Find all artists with more than 1000 followers whose genres include any form of 'pop'.
    1. Find the average `energy`, `dancibility`, and `tempo` for all tracks and then for each `time_signature`.
    1. For each artist, find the total number of albums present in our `albums` table.
    1. Find all albums released before 2000 and order by artist popularity score. 
    1. For each album, find the difference between the total tracks in the `albums` table and the number of tracks present in the `tracks` table.
