# Week 2 Graded Project (Python and Pandas)

In this project we will use Spotify data to test the skills you have learned in the first two weeks of the course, by exploring each of the data files individually, and then using Pandas to join the data from multiple files. 

## Data
We are working with Spotify datasets that includes information on artists, albums, and individual tracks. In the `data/` directory is a script called `get_data.sh`. This will use `gsutil` to download 3 CSV files of Spotify data into the `data/` directory:
- `spotify_albums.csv`
- `spotify_artists.csv`
- `spotify_tracks.csv`
>Note: If you have not installed `gsutil`, please follow the [Google Cloud section of the Getting Started guide](/getting-started/README.md)

Familiarize yourself with the 3 CSV files to see what columns are present and how they are arranged using Pandas (note these files, especially the `spotify_tracks.csv` are large and do not load well with excel or other spreadsheet tools. Pandas is your friend here). Things to note about this dataset:
- Each row of the csv corresponds to a single artist, album, or track.
- Each csv has a unique id column called `id`.
- These `id`s are referenced as `artist_id`, `album_id`, or `track_id` in the other csv.
- This is an incomplete dataset. For example:
    - Not all tracks for every `spotify_albums.csv` are present in `spotify_tracks.csv` (We'll learn how to pull this missing data in the future).
    - Not every `spotify_artists.csv` entry has albums or songs.
    - Take these into account when cleaning and joining this data.

## Accepting Criteria
1. Profile each of the three datasets individually. You do not have to run a full profiling report (though you may if you wish to), but at least use the Pandas preview functions to get some idea of what each dataset looks like.
1. Clean and normalize each dataset:
    1. Check all datasets for duplicates
    1. For Artists:
        1. Replace the empty list (`[]`) entries in the `genres` column with `NaN`s
    1. For songs:
        1. First, look at the values for `lyrics` to see why you think they don't parse well in Excel and some other programs
        1. Drop the `lyrics` column

1. Using Pandas, perform the following joins, choosing the join type that you think is appropriate:
    1. Join artists and albums on the artist ID
    1. Join albums and tracks on the album ID
    1. Join artists, albums, and tracks into a single unified dataset ([See [this thread](https://stackoverflow.com/questions/23668427/pandas-three-way-joining-multiple-dataframes-on-columns) for hints on this])
    1. Make a comment in your code file on why you chose that join type

1. Use the Pandas aggregating functions to calculate some statistics on the data (some of these can be calculated from the separate tables, and some will require using aggregating functions on joined data):
    1. How many albums came out in each year?
    1. What are the top three genres for every year?
    1. Who are the artists with the most albums? (list the top ten in descending order)

