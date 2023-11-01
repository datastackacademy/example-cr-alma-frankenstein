## Independent Project Overview
Before you begin, take a moment to revisit and review the [Independent Projects and Code Reviews](https://www.learnhowtoprogram.com/introduction-to-programming/getting-started-at-epicodus/independent-projects-and-code-reviews) lesson.

## Chapter 3 Code Review 1
In this project you will take two Spotify CSV files, load them into Pandas DataFrames, and then write those DataFrames as tables to a MariaDB database. The outline of the class and functions need for this pipeline has been created for you, and can be found at the bottom of this code review. You may copy it to your submitted repository to use as a starting point.
 
### Setup Git
As always, create a repository on GitHub for this project. Include a README and at least 8 commits.

### Start database
Start an empty database called 'spotify' with our usual script:

```bash
# start mariadb docker container with empty database named spotify
docker run --name mariadb \
    -p 127.0.0.1:3306:3306 \
    -e MYSQL_ROOT_PASSWORD=mysql \
    -e MYSQL_DATABASE=spotify \
    --rm -d \
    mariadb:latest
```
You can connect to it via the command line (below) or using BeeKeeper Studio:

```bash
docker exec -it mariadb mysql -D spotify -u root -pmysql
```

### Install Requirements
- Create a Python virtual environment
- Activate it
- `pip install` the following packages:
```bash
numpy==1.20.2
pandas==1.2.4
SQLAlchemy==1.4.13
PyMySQL==1.0.2
jupyterlab==3.0.14
notebook==6.3.0
```

...or copy the `requirements.txt` file from ch3/ep3 and install its contents

### Get Data
Make a `data/` directory in your repo, and within it run:

```bash
gsutil -m cp gs://data.datastack.academy/spotify/spotify_artists.csv gs://data.datastack.academy/spotify/spotify_albums.csv .
```
This will copy the Spotify CSV files to your `data/` directory.

### Accepting Criteria
1. In your submitted repository, include a _.gitignore_ file to ignore either the entire content of _data/_ folder or only files ending in _".csv"_,

2. At the bottom of this page, you will see the outline of a class called `DataLoader` that you should copy to your main.py file. For that class:

    - Fill in the `__init__()` method so it takes a filepath to a CSV file and loads that CSV file into a Pandas DataFrame (it's fine to just load a single file at a time).

    - Fill in the `head()` method so it prints the head of the DataFrame.

    - Fill in the `add_index()` method so it creates an index column from concatenating a series of column values. The values should come from a list of column names passed in as a list.

    - Fill in the `sort()` method so it sorts the DataFrame by a specified column.

3. Outside the `DataLoader` class, fill in the `db_engine()` function to create a SQLAlchemy database engine. For this project, the values needed to configure it can be passed in as arguments, rather than using a `config` file.

4. Fill in the `db_create_tables()` function to create tables for the Spotify data. The schemas for the tables should reflect the column names and datatypes of the CSV files. You can inspect the column names and datatypes either by opening the CSV file, or by using the following code snippet:
      ```python
        import pandas as pd

        df = pd.read_csv('<PATH_TO_FILE>.csv', nrows=2)
        for dtype in df.dtypes.iteritems():
          print(dtype)
      ```
      In the output of the above snippet, `dtype('O')` means 'string'.

      The `db_create_tables()` function will need a SQLAlchemy engine as an argument; this is the engine you created in the `db_engine()` function above. That engine is bound to the SQLAlchemy MetaData object on line 82. The tables you define should be associated with the MetaData object, as seen in ch3/ep2.
      The `db_create_tables` function should also be able to drop and create tables if the `drop_first` parameter is set to 'True'.

4. In the `main()` function at the bottom of your `main.py` file, follow the guidelines in the docstring so that your code performs all the specified tasks when "`python3 main.py`" is run in your terminal.


5. Include a README and a _.gitignore_ in your repository, and at least 8 commits. Your code should be readable and well-commented.

<br>

Bonus Point: Add a method to your `DataLoader` class that can merge the DataFrames on `id` in `spotify_artist.csv` and `artist_id` in `spotify_albums.csv`, and use Pandas to show how many albums each artist has, limiting the output to the top 20 in descending order.



### Code Outline for main.py
```python
"""
Starter code. Finish implementing the methods in this code
"""
import pandas as pd
import sqlalchemy as sa


class DataLoader():

    def __init__(self, filepath:str) -> None:
        """
        Loads a CSV file path into a Dataframe

        Args:
            filepath (str): file path to the CSV file
        """
        pass

    def head(self) -> None:
        """
        prints the head of the dataframe to console
        """
        pass

    def add_index(self, index_name:str, colum_names:list) -> None:
        """
        Create a dataframe index column from concatenating a series of column values. Column values are concatenated by a dash "-".

        For example if you have three columns such as: artist="Metallica", song="Ride the Lighting"
        the index would be ""Metallica-Ride the Lighting"

        Args:
            index_name (str): the index column name
            colum_names (list): list of columns to concatenate into an index column
        """
        pass

    def sort(self, column_name:str) -> None:
        """
        Sorts the dataframe by a particular column

        Args:
            column_name (str): column name to sort by
        """

    def load_to_db(self, db_engine, db_table_name:str) -> None:
        """
        Loads the dataframe into a database table.

        Args:
            db_engine (SqlAlchemy Engine): SqlAlchemy engine (or connection) to use to insert into database
            db_table_name (str): name of database table to insert to
        """



def db_engine(db_host:str, db_user:str, db_pass:str, db_name:str="spotify") -> sa.engine.Engine:
    """Using SqlAlchemy, create a database engine and return it

    Args:
        db_host (str): datbase host and port settings
        db_user (str): database user
        db_pass (str): database password
        db_name (str): database name, defaults to "spotify"

    Returns:
        sa.engine.Engine: sqlalchemy engine
    """
    pass


def db_create_tables(db_engine, drop_first:bool = False) -> None:
    """
    Using SqlAlchemy Metadata class create two spotify tables (including their schema columns and types)
    for **artists** and **albums**.


    Args:
        db_engine (SqlAlchemy Engine): SqlAlchemy engine to bind the metadata to.
        drop_first (bool): Drop the tables before creating them again first. Default to False
    """
    meta = sa.MetaData(bind=db_engine)

    # your code to define tables go in here
    #   - Be careful, some of the columns like album.available_markets are very long. Make sure you give enough DB length for these. ie: 10240 (10kb)

    # your code to drop and create tables go here


def main():
    """
    Pipeline Orchestratation method.

    Performs the following:
    - Creates a DataLoader instance for artists and albums
    - prints the head for both instances
    - Sets artists index to id column
    - Sets albums index to artist_id, name, and release_date
    - Sorts artists by name
    - creates database engine
    - creates database metadata tables/columns
    - loads both artists and albums into database
    """
    pass


if __name__ == '__main__':
    main()
```
