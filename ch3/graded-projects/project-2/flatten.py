import pandas as pd
from google.cloud import bigquery as bq
from google.cloud.exceptions import NotFound


class DataLoader():
    def __init__(self, filepath) -> None:
        """
        Loads a CSV file path into a Dataframe

        Args:
            filepath (str): file path to the CSV file
        """
        # read the filepath into a dataframe
        # and assign the df to self
        df = pd.read_csv(filepath, header=0)
        self.df = df    
        
    def name_index(self) -> None:
        """
        Rename column in DataFrame
        """
        df = self.df
        df.rename(columns={'Unnamed: 0': 'index_num'}, inplace=True)
        

def make_bq_client(project_name, dataset_name):
    """
    Connect to BigQuery on a given project, check for a dataset, and create the dataset if it doesn't exist

    Args:
        project (str): name of the BigQuery project that will contain this data
        dataset (str): dataset that will hold these tables
    """
    # create a bigquery client
    client = bq.Client(project_name)
    # create the bigquery dataset if it doesn't exists (we can't get it!)
    try:
        client.get_dataset(dataset_name)
    except NotFound:
        client.create_dataset(dataset_name)
    # return the client
    return client


def create_schema_and_table(bq_client, artist_ref, album_ref) -> None:
    """
    Define schemas for the tables and create the tables

    Args:
        bq_client (str): Client object created by make_bq_client()
        artist_ref (str): table ID for artist table
        album_ref (str): table ID for album table
    """
    # Define table schemas
    album_schema = [
        bq.SchemaField('index_num', 'INTEGER', mode='REQUIRED'),
        bq.SchemaField('album_type', 'STRING', mode='NULLABLE'),
        bq.SchemaField('artist_id', 'STRING', mode='NULLABLE'),
        bq.SchemaField('available_markets', 'STRING', mode='NULLABLE'),
        bq.SchemaField('external_urls', 'STRING', mode='NULLABLE'),
        bq.SchemaField('href', 'STRING', mode='NULLABLE'),
        bq.SchemaField('id', 'STRING', mode='NULLABLE'),
        bq.SchemaField('images', 'STRING', mode='NULLABLE'),
        bq.SchemaField('name', 'STRING', mode='NULLABLE'),
        bq.SchemaField('release_date', 'STRING', mode='NULLABLE'),
        bq.SchemaField('release_date_precision', 'STRING', mode='NULLABLE'),
        bq.SchemaField('total_tracks', 'INTEGER', mode='NULLABLE'),
        bq.SchemaField('track_id', 'STRING', mode='NULLABLE'),
        bq.SchemaField('track_name_prev', 'STRING', mode='NULLABLE'),
        bq.SchemaField('uri', 'STRING', mode='NULLABLE'),
        bq.SchemaField('type', 'STRING', mode='NULLABLE')
    ]

    artist_schema = [
        bq.SchemaField('index_num', 'INTEGER', mode='REQUIRED'),
        bq.SchemaField('artist_popularity', 'INTEGER', mode='NULLABLE'),
        bq.SchemaField('followers', 'INTEGER', mode='NULLABLE'),
        bq.SchemaField('genres', 'STRING', mode='NULLABLE'),
        bq.SchemaField('id', 'STRING', mode='NULLABLE'),
        bq.SchemaField('name', 'STRING', mode='NULLABLE'),
        bq.SchemaField('track_id', 'STRING', mode='NULLABLE'),
        bq.SchemaField('track_name_prev', 'STRING', mode='NULLABLE'),
        bq.SchemaField('type', 'STRING', mode='NULLABLE') 
    ]

    # Create the tables, or drop and replace existing tables
    artist_table = bq.Table(artist_ref, schema=artist_schema)
    try:
        # try getting the table reference if it exists 
        #   >> delete and re-create it if it does
        bq_client.get_table(artist_ref)
        bq_client.delete_table(artist_ref)
        bq_client.create_table(artist_table)
    except NotFound:
        bq_client.create_table(artist_table)

    album_table = bq.Table(album_ref, schema=album_schema)
    try:
        bq_client.get_table(album_ref)
        bq_client.delete_table(album_ref)
        bq_client.create_table(album_table)
    except NotFound:
        bq_client.create_table(album_table)

def populate(client, dataframe, table_ref, truncate=False) -> None:
    """
    Write data from DataFrames to BigQuery

    Args:
        client (str): instance of BigQuery Client object
        dataframe (str): Pandas DataFrame from CSV
        table_ref (str): table ID, as '<your-project.your_dataset.your_table_name>'
    """
    jc = bq.LoadJobConfig(
        autodetect=False,
        create_disposition='CREATE_NEVER',
        write_disposition='WRITE_TRUNCATE' if truncate else 'WRITE_APPEND',
    )
    # Make an API request
    # use the bigquery client `load_table_from_dataframe()` to load data into bq table
    job = client.load_table_from_dataframe(dataframe, destination=table_ref, job_config=jc)
     # Wait for the job to complete
    job.result() 

def run(project, dataset) -> None:
    """
    Pipeline piecing together the above code

    Args:
        project (str): name of the BigQuery project that will contain this data
        dataset (str): the BigQuery dataset that will hold these tables
    """
    # Use DataLoader to load a CSV file path into a Dataframe
    # For each DataFrame, use the name_index() method to rename the column 'Unnamed: 0' to 'index_num'
    album_loader = DataLoader('./data/spotify_albums.csv')
    album_loader.name_index()
    albumdf = album_loader.df
    artist_loader = DataLoader('./data/spotify_artists.csv')
    artist_loader.name_index()
    artistdf = artist_loader.df

    # Create the bq client to connect to the project and, if needed, create the dataset
    client = make_bq_client(project, dataset)
    
    # Make table references for creating the tables
    album_ref = f"{project}.{dataset}.albums"
    artist_ref = f"{project}.{dataset}.artists"

    # Create the tables and schemas
    create_schema_and_table(client, artist_ref, album_ref)

    # Populate the tables with data from the DataFrames
    populate(client, albumdf, album_ref)
    populate(client, artistdf, artist_ref)



if __name__ == '__main__':
    run('data-sandbox-frankenstein', 'spotify')