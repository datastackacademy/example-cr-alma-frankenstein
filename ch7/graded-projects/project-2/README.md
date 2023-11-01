# Project Overview
In this project you will create a data pipeline to ingest Amazon review data from GCS and land it in a BigQuery table using Dataproc. 

## Git
As usual, create a new git project for this challenge. As you complete the script(s) and supporting files, be sure to update your README.md to explain their contents and how to run them.

## Data
For this project, you will be ingesting Amazon review data from GCS. The input file for this project is: 

`gs://data.datastack.academy/amazon/All_Amazon_Review.json`

This is a new-line delimited file containing _many_ Amazon reviews (over 20GB). Each row is of this format:

```json
{
  "overall":1.0,
  "verified":false,
  "reviewTime":"12 11, 2015",
  "reviewerID":"A27BTSGLXK2C5K",
  "asin":"B017O9P72A",
  "reviewerName":"Jacob M. Wessler",
  "reviewText":"Alexa is not able to control my lights. If I ask her to tell me what LIFX can do, she will give me an example with one of my group names. If I use that exact same group name in a new request, she'll await that she doesn't recognize the name. This skill is VERY buggy and has not yet worked for me. I even rest Alexa, uninstalled LIFX, and set everything up again.",
  "summary":"VERY Buggy, doesn't work.",
  "unixReviewTime": 1449532800
  }
```

There may be additional fields as noted in the dataset documentation [here.](https://nijianmo.github.io/amazon/index.html) A small, 10 row sample data set is provided in `data/sample.json` to get you started. Because this is a large, real-world dataset, it can have issues with unforeseen fields and formatting but defining a schema _before_loading the data can help alleviate these issues as we did in Episodes 6 & 7.

## Accepting criteria
1. Create a  script(s) that do the following:
    1. Create `amazon` dataset in BigQuery.
    1. Define `reviews` table in `amazon` dataset.
        1. Use the sample data to define the columns and data types.
        1. Make a corresponding Spark `StructType` schema (or load from JSON).
    1. Define `summary` table in the `amazon` dataset.
        1. This will have 3 columns:
            1. `asin`: the same `asin` as we see in the `reviews` data.
            1. `total_reviews`: an integer column.
            1. `average_rating`: a float column.
        1. Make a corresponding Spark `StructType` schema.
    1. Ingest `All_Amazon_Review.json` from GCS into a Spark DataFrame and do the following:
        1. Load using your previously defined schema.
        1. Assure that only the desired columns are present and that the data types are correct.
        1. Create new DataFrame for item `summary`.
            1. Group the input data by `asin`.
            1. Calculate the total number of reviews and average `overall` rating for each `asin`.
        1. Write to your tables in BigQuery.
1. Crate a **Dataproc** instance and use it to run your script!

Once you have successful script(s), submit them, a link to your `amazon` dataset, and a link to your Dataproc logs (which can be found in the Cloud Console under Dataproc -> Jobs -> click the successful job). Then remove your Dataproc instance to avoid extra charges.
