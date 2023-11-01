# Graded Project, Ch. 4: APIs

In this project we will create an API to serve data from the Spotify database that we used in Chapter 2. The goal is to make a fully functioning API that can perform CRUD (Create, Read, Update, Delete) operations.

## Data

In the [graded project for Chapter 2](../../ch2/graded-projects/) you loaded three tables of Spotify data into a MariaDB Docker container. You will use that container pre-loaded with Spotify data in this week's graded project to perform the necessary data operations that your API will require when it receives requests.

## Accepting Criteria

1. Create a basic API using the code samples and exercises from throughout this chapter.

1. Create routes to GET from your API:
    1. song tags using a `song_id`
    1. similar songs using a `song_id`
    1. all tracks from a given artist using an `artist_id`
1. Make sure that your API returns the object(s) in the proper format

1. Create routes to POST to your API:
    1. adding a new song
    1. adding a new artist
    1. update an existing song title
    1. delete an existing song (using a `song_id`)
1. Use Postman to submit the necessary form data for these operations

**Optional: Additional Challenges**

You can implement none, one, or more of these options:

1. Make sure that your API implements user authentication.
1. Implement a cloud version of the API using BigQuery and AppEngine. This exercise requires you to load the Spotify dataset to BigQuery and deploy a Flask App on Google AppEngine.

