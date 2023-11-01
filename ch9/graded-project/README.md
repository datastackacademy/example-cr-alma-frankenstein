# Graded Project - Ch. 9 (Streaming Architecture)

In this graded project you will create a streaming application using the reference architecture we have discussed in class, using GitHub event data. We will use streaming architecture to reproduce a portion of the GitHub database.

## Data

The data for this project is a JSON file of GitHub event data. Run:

```bash
gsutil -m cp \
  "gs://data.datastack.academy/github/events/2021/github-events-2021-01-01-15.json" \
  .
``` 
to download.

## Accepting Criteria  

This project will closely follow the architecture used in the previous episodes, although it will not be quite as complex, because the structure of the data is different. We will use streaming architecture, with Pub/Sub and functions, to automatically recreate a portion of the GitHub database, using a combination of the event data above, with corresponding author and repository data retrieved from the GitHub API.

Your application should:

1. Ingest event data in JSON format from a Cloud Storage bucket

1. Set up a topic/subscription for events

1. Create tables in BigQuery for
    1. Events
    1. Repos
    1. Authors
1. Make sure to enforce the correct key relationships between the tables

1. Create an event publisher in Python

1. Use Cloud Functions to process the event data when it is published
    1. Retrieve full author and repo data from the GitHub API, using ID values from the events data
    1. Each event should just have an associated author ID and repo ID, which will allow you to link the tables

1. Write the full author, repo, and event data to tables in BigQuery
    1. Perform a query which joins event, repo, and author data to demonstrate that your data relationships have been implemented correctly

1. When you have the application working, save the logs and screenshots showing the successful pipeline execution and a sample of the data present in the tables. 

