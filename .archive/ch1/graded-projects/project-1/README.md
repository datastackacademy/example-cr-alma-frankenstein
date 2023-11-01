# Week 1 Graded Project

In this project we will create a simple music library application using the Python tools we have learned so far in the course.

## Data

Since we haven't yet learned how to load data from files, this project project will be entirely self-contained in Python. 

## Accepting Criteria
1. Create a `.py` file to hold your code
1. Create classes for artists and songs
    1. For artists, create the following attributes:
        1. Artist ID (a _unique_ numeric identifier)
            1. Make sure that you create some mechanism to ensure that the same artist ID is not used more than once when you are creating artists
        1. Artist's name
        1. Genre
        1. Date of birth
    1. For songs, create the following attributes: 
        1. Artist (this will hold an artist ID)
        1. Song title
        1. Song length
        1. Lyrics
    1. Create getter and setter functions for all attributes in your classes
    1. Create validation functions:
        1. to see if an artist exists in the list of artists
        1. to check whether a song is created by a particular artist
    1. Make a primitive database for artists by storing artists names in a dictionary with their ID as a key (so that you can look up an artist by their Artist ID)
1. Create a command line interface that will let you:
    1. Add some artists and songs so that you have some data (two or three artists and a handful of songs is fine)
    1. Implement a search functionality that will let the user display all the songs for an artist, or all the songs whose title contains the search string the user inputs. HINT: You might want to consider storing all your Song objects in a list or dict so that you can iterate over them.