# Graded Project - Ch. 6 (Airflow)

The graded project for this week will require you to build a cloud version of the Spotify database using Google Cloud Composer. We will automate the process of database creation that you worked on in the [second graded project for Ch. 3](../../ch3/graded-projects/project-2).

The goal for this project is to build a fully automated, cloud-deployed pipeline for building the database from input files. You will write code and set up cloud services that check for the presence of the data, and trigger a DAG to perform the steps of processing the data, loading it into a database, and cleaning up.

## Data

This project will use the Spotify track, album, and artist files we have worked with previously. These are available in GCS at `data.datastack.academy/spotify`. The following command will download the necessary files:

```
gsutil -m cp \
  "gs://data.datastack.academy/spotify/spotify_albums.csv" \
  "gs://data.datastack.academy/spotify/spotify_artists.csv" \
  "gs://data.datastack.academy/spotify/spotify_tracks.csv" \
  .
```

## Accepting Criteria

1. Set up a new Cloud Composer environment for this project.
    1. Make sure that your new environment has the required packages available (you might want to do this using [the requirements.txt file](../ep5/requirements.txt) from the last episode)
    1. Creating this environment will [automatically create an associated GCS bucket](https://cloud.google.com/composer/docs/concepts/cloud-storage) which you will use to hold the files for this project

1. Create schema files (YAML) for the track, album, and artist tables, so that your database can be constructed automatically
    1. Refer to [Episode 4](../ep4/) from this chapter for details on how to do this - you will need a separate YAML file for each of the tables (tracks, albums, and artists)
    1. Copy the schema files for the Spotify data (you should already have these from Ch. 3) and data files into the new bucket

1. Using the DAG developed in [episode 5](../ep5/) as a model, implement a DAG that can be deployed to Composer and will do the following:
    1. Use a `GCSObjectExistenceSensor` that checks for the presence of the track, album, and artist data files in our GCS bucket.
    1. Load schema information for the Spotify data from YAML files in your GCS bucket
    1. Create the necessary tables in BigQuery to hold the data
    1. Load the data from CSV files and populate it to the BigQuery tables created from your schema

1. Deploy your DAG to Composer
    1. If the DAG won't run, troubleshoot any issues that are present
        1. When troubleshooting, it will be helpful to check the logs to determine the source of any errors
    1. *When you get your DAG working, save the log files showing that it ran successfully*

1. When you are finished, and have verified that your DAG will run, clean up by deleting the Composer environment you created for the project, so that we will not be charged for unused resources.

## What to submit

To grade the project, we will look at your Python code, schema and config files (YAML), and the logs from your Composer DAG run. In order to get your DAG to run on Composer, you should have already put your code and config files in the GCS bucket created for this project. Also make sure to save the log files showing that your DAG ran successfully to the same bucket. 

## Extra credit

If you have time and want further practice, or need to make up some points from a previous project, extra credit will be awarded for the following tasks:

1. Add the ability to write to both a local MariaDB and to BigQuery when constructing the database
2. Automatically perform weekly or monthly updates
    1. Use `new_tracks.json` as the source of track update data:
        - `gsutil -m cp "gs://data.datastack.academy/spotify/new_tracks.json" .` to download
    1. Create a new DAG, which you schedule to run weekly or monthly, which uses a GCS connection and `GCSObjectExistenceSensor` to check for the presence of the new tracks file and, if it is present, automatically writes this new data to the tracks table in BigQuery
    1. If you choose to do this, also include (in your bucket) a screenshot showing the scheduled run, so that you can close your Composer environment when you finish work on the project.
