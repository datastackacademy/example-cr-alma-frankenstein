# Graded Project

This week you learned how to create GCO Cloud Functions that are triggered by HTTP requests or GCS Storage events. In this project, we're going to practice again by looking at Beijing's air quality dataset. Our dataset includes hourly reports from a dozen different weather stations in the Beijing area from 2013-2017. The stations report various measures such as: PM10 level (particular matter in 10 micrometers), CO, O3, temperature, air pressure, rain, wind, etc. 

It will be your task to:

1. Create a storage triggered Cloud Function that loads a station data file into BigQuery
   1. This function must run automatically based on a GCS storage trigger; meaning the file should be parsed and loaded into BigQuery as soon as it's place into your GCS bucket.
   2. This function should use BigQuery's python SDK to create a table to store records if it doesn't exists
   3. THis function should use pandas to parse and load the data file into BigQuery
   4. This function should merge records into the table; meaning if there are existing records in the table for the station, they should be updated. You cannot insert duplicate rows.
      1. > Hint: Use a **staging table** for merging records. Feel free to refresh yourself with what you learned back in [ch3ep9](../../ch3/ep9/README.md). Try this or googling before you peek at the next hint 😉️
      2. > Hint: Insert records into a temp table first, then run a BigQuery [MERGE](https://cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax#merge_statement) statement to merge records from your temp table into the main table. Drop the temp table after a successful merge. This is called using staging tables in data engineering.
2. Create a http triggered Cloud Function that return daily statistics:
   1. This function will return the daily average values for PM10, temperature, pressure, and wind per station.
   2. The function will accept the following GET params: `station`, `date`.
   3. Return the values in JSON format.
3. **EXTRA CREDIT** (optional):
   1. Use the pypi [matplotlib](https://matplotlib.org/) to create a yearly graph showing daily trends of PM10, rain, wind, and temperature in a line chart.
      1. You should compute daily average of the measures mentioned
      2. Create a line-chart the shows the daily average over the year as separate lines
      3. Assign a different color to each line (PM10, rain, ...)
      4. This chart helps visualize the correlation between PM10, rain, wind, and temperature in a year
      5. Create a HTTP triggered Cloud Function that takes `station` and `year` as a GET params and returns the chart in .jpg or .png format. You must set your HTTP `Content-Type` response header accordingly for this to work.

## Setup

 To download the station data files run the [`data/get_data.sh`](data/get_data.sh) script. You can also directly download the files from our GCS bucket: `gs://data.datastack.academy/beijing_airquality`

## Acceptance Criteria

You must demonstrate **all** of the following to successfully complete this assignment:

1. Data loader function
   1. Function must be storage triggered and run automatically as soon as a station file is placed into a storage bucket.
   2. Use python pandas to read station data files. Use BigQuery client `load_table_from_dataframe()` function to load data into BigQuery.
   3. Demonstrate that records are correctly merged and not duplicated if a station file is loaded twice.
   4. Successfully load station data files by placing them into your GCS bucket.
2. Daily summary function
   1. Function must be HTTP triggered. Accepts two params for `station` and `date`. It should return daily averages for PM10, rain, wind, and temperature.
   2. Demonstrate your function running successfully by running a few station/dates combinations:
      1. Huairou, 2013-03-03
      2. Aotizhongxin, 2017-02-16
      3. Tiantan, 2015-08-05

For Extra Credits you must demonstrate:

1. Your Cloud Function must download a line-chart image for a `station`/`year` combination. 
2. Line-char must include yearly trend for: PM10, rain, wind, and temperature as separate lines on the same chart.
3. Show the trend for a couple of combinations:
   1. Wanliu, 2016
   2. Dongsi, 2017

