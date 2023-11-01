# Project overview
For this project, we will be building a report to visualize Spotify data. Let's pretend we're data wranglers at a record company and want to create a Data Studio report to get an insight in to the streaming service.

## Data
In this project, we will be building on the Spotify data you uploaded to BigQuery as the Chapter 3 graded project. If you deleted that dataset, re-run your Chapter 3 code so you have the three Spotify tables present in BigQuery. If you completed any of the challenge projects adding new tracks, great! You will have even more information in your reports but they are not required for this project.

## Accepting Criteria
Using Data Studio, complete the following:

1. Create new data sources for the `tracks`, `albums`, and `artists` data we uploaded to BigQuery in Chapter 3.
1. Popularity tracking:
    1. Make a chart or table to display the top artists by follower _or_ popularity. Add a slider to filter by number of followers and use the 'show top #' option to allow filtering down to 0 followers.
    1. Make a chart showing the top tracks by popularity. Join the artist name and make a checkbox filter to filter by artist.
1. Album analysis:
    1. Create a bar chart that shows the number of albums per artist. Add drill down to the number of tracks per artist.
    1. Create a pie chart to show the number of tracks per album. Create a filter for 'album' vs 'single'.
    1. Create  time series plot tracking the average number of tracks per album over time. Add the filter for 'album' vs 'single'.
    1. Create a time series plot tracking the total number of releases per year. Add a checkbox filter to allow filtering by artist name.
1. World view:
    1. Join the 'country' from tracks with the artist and make a map showing the total number of artists with tracks for each country. Add a date range filter and checkbox to filter by artist name.

Save and submit this report as your graded project.