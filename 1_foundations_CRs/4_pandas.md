## Independent Project Overview
Before you begin, take a moment to revisit and review the [Independent Projects and Code Reviews](https://www.learnhowtoprogram.com/introduction-to-programming/getting-started-at-epicodus/independent-projects-and-code-reviews) lesson.

## Code Review: Pandas
In this project we will use Spotify data, first exploring each of the data files individually, and then using Pandas to join the data from multiple files.

### Setup Git
1. As always, create a repository on GitHub for this project. 
1. Include an informative README, a `.gitignore` file, a `requirements.txt` file and at least 8 commits.

### Data
Create a `data/` directory in your repo, and `cd` into it.


The following command
```bash
gsutil -m cp gs://data.datastack.academy/spotify/*csv .
```
will use `gsutil` to download 3 CSV files of Spotify data into the `data/` directory:
- `spotify_albums.csv`
- `spotify_artists.csv`
- `spotify_tracks.csv`
>Note: If you have not installed `gsutil`, please follow the [Google Cloud section of the Getting Started guide](/getting-started/README.md)

> Note: Alternatively you can download the files using this [link](https://storage.googleapis.com/data.datastack.academy/spotify/spotify-data.zip). Unzip this file in your data folder.

Familiarize yourself with the 3 CSV files to see what columns are present and how they are arranged using Pandas (note these files, especially the `spotify_tracks.csv` are large and do not load well with excel or other spreadsheet tools. Pandas is your friend here). Things to note about this dataset:
- Each row of the csv corresponds to a single artist, album, or track.
- Each csv has a unique id column called `id`.
- These `id`s are referenced as `artist_id`, `album_id`, or `track_id` in the other csv.
- This is an incomplete dataset. For example:
    - Not all tracks for every `spotify_albums.csv` are present in `spotify_tracks.csv` (We'll learn how to pull this missing data in the future).
    - Not every `spotify_artists.csv` entry has albums or songs.
    - Take these into account when cleaning and joining this data.

>Note: Don't include the data files when you push to GitHub; there're too large and will cause issues. To avoid pushing them, include them in a `.gitignore` file, or simply ommit them when you `git add`. Include the `get_data.sh` file in your project instead, or add instructions to your README for future reference.

### Accepting Criteria
1. For each dataset, profile the data using `head()`, `tail()`, and `.shape()`. Write a comment for each one, briefly explaining what this technique does, and what the output you got tells you about the dataset.
1. For Albums, use `.loc` to show just rows 10-20 of the 'name' and 'release_date' columns
1. Clean and normalize each dataset:
    1. Remove duplicates from each dataset
    1. For Artists:
        1. Write a `map()` function to replace the empty list (`[]`) entries in the `genres` column with `NaN`s (but don't alter the list entries in `genres` that contain values!)
    1. For Tracks:
        1. Print the names of the columns in Tracks
        1. First, look at the values for `lyrics` to see why you think they don't parse well in Excel and some other programs
        1. Drop the `lyrics` column
        1. Print the names of the Tracks columns again, to show that the 'lyrics' column has been dropped

1. Using Pandas, perform the following joins, choosing the join type that you think is appropriate. Make a comment in your code file on why you chose that join type
    1. Join artists and albums on the artist ID
        - print the `head()` and `shape` of the resulting DataFrame
    1. Join albums and tracks on the album ID
        - print the `head()` and `shape` of the resulting DataFrame

1. Use the Pandas to calculate some statistics on the data, and print the results:
    1. Which artists appear the most times in the Artists data?
    1. Which artists have the highest 'artist_popularity' rankings? (list the top ten in descending order)

1. The project should:
- Include informative README, a `.gitignore` file, a `requirements.txt` file and at least 8 commits.
- Be well-commented, without unused code.
- Profile the data, as outlined above.
- Use `loc`, as outlined above.
- Clean and normalize each dataset.
- Use and explain a join.
- Calculate the statistics outlined above.- Include informative README, a `.gitignore` file, a `requirements.txt` file and at least 8 commits.
- Be well-commented, without unused code.
- Profile the data, as outlined above.
- Use `loc`, as outlined above.
- Clean and normalize each dataset.
- Use and explain a join.
- Calculate the statistics outlined above.


### Bonus Point:
1. How many albums came out in each year? (Notice that the values in the release_date column of Albums is in the format yyyy-mm-dd)
1. Create a vizualization, and add it to your README.

