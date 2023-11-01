# Project Overview
This graded project will create a dataset of Spotify data in BigQuery.

## Setup git
For this graded assessment, create a new Git project to store your code. As you write your code to meet the accepting criteria below, commit your files to this repo _and_ update the README.md to provide information about the organization and use of the code you're writing.

## Data
We are once again going to work with the Spotify data for artists, albums, and tracks that we used for our Chapter 2 graded project. As in Chapter 2, you can run the `get_data.sh` script in the `data/` directory to download the following files:
- `spotify_albums.csv`
- `spotify_artists.csv`
- `spotify_tracks.csv`

These are the same files as we saw in Chapter 2.

## Accepting criteria
Create a Python script or Jupyter notebook that does the following:
1. Data loading and cleaning. Create functions and/or classes to perform the following loading and cleaning (note these are the same as Chapter 2):
    1. Set the `id` column as your index.
    1. Drop the following columns from all tables: `available_markets`, `images`, `external_urls`, and `Unnamed`.
    1. Drop the `track_id`, `track_name_prev` columns from `albums` and `artists`. This data set has put an arbitrary track in each of the spots for the artist and album.
    1. Drop the `lyrics` column from `tracks`
    1. Convert any `date` column to a datetime data type.
    1. For columns that are lists like `genre` in our `artists` data, convert the whole list to a string.
    3. Check for duplicate rows and drop any you find.
1. Data writing class:
    1. Create a parent data loading class with required methods and implement 2 children classes that do the following:
        1. Load data using your data loading class/functions
        1. Make one child class that writes the data to MariaDB (you can reuse/update your Chapter 2 work for this)
        1. Make one child class that write the data to BigQuery.
1. Use your BigQuery class to write all tables to a BigQuery dataset called `spotify`.
    1. Verify all data has been written.
    1. Verify that all columns are the correct data type.