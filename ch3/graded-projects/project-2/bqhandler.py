from google.cloud import storage
from google.cloud import bigquery as bq
from google.cloud.exceptions import NotFound


from file_loader import DataLoader



class BigQueryHandler():
    def __init__(self, project:str, dataset:str, creds:str) -> None:
        """
        Initializes the necessary objects to connect to BigQuery and GCS

        Args:
            project (str): the name of your GCS project
            dataset (str): the GCS dataset to be used for this project
            creds (str): the path to your GCS credentials JSON file
        """

        # assign creds to a variable called 'creds'
        # assign project to a variable called 'project'
        # assign dataset to a variable called 'dataset', to be passed to the following code:
        dataset = bq.DatasetReference(project, dataset)
        # create the client
        client = bq.Client(project=project, credentials=creds)
        storage_client = storage.Client(project=project, credentials=creds)
        # if dataset doesn't exist, create it
        try:
            client.get_dataset(dataset)
        except NotFound:
            client.create_dataset(dataset)
        # Store all our objects on our class
        # Make 'creds', 'client', 'storage_client', 'project', and 'dataset' attributes of the class using 'self'
 

    def create_schema(self) -> None:
        """Create a schema storage dict on our class for each table"""
        # make the storage an empty dict
        bq_schema = {}
        # define each schema as a list of bq.SchemaField objects
        # see the BigQuery subclass in ch3/ep8 for examples

        # add each schema as a value in the bq_schema dict, with its table name as the key
        # the table names should be 'artist' and 'album'
   
        # Save schemas on our class
        self.bq_schema = bq_schema

    
    def create_table(self, table_def, table_ref, drop_and_replace=False):
        """
        Create a table in our dataset

        Args:
            table_def (str): bq.Table, created in the init_storage() method below
            table_ref (str): bq.TableReference, created in the init_storage() method below
        """
        # We use a try get_table and except NotFound to check if our table is already present
        try:
            self.client.get_table(table_ref)
            if drop_and_replace:
                # if we want to start fresh we can drop the table and recreate it
                self.client.delete_table(table_ref)
                self.client.create_table(table_def)
        except NotFound:
            # Table isn't present so let's create it
            self.client.create_table(table_def)


    def init_storage(self, drop_and_replace=False) -> None:
        """
        Function to initialize our DB in BigQuery
        """
        # Call the create_schema() method
        self.create_schema()

        # Get the schema from the bq.schema dict created in the create_schema() method
        # Then use the dataset and table name to create a bq.TableReference
        artist_schema = self.bq_schema['artist']
        artist_table_ref = bq.TableReference(dataset_ref=self.dataset, 
            table_id = 'artists')
        artist_table = bq.Table(artist_table_ref, schema=artist_schema)
        # Once the bq.Table object is created, we can create it in BigQuery
        self.create_table(artist_table, artist_table_ref, drop_and_replace)

        album_schema = self.bq_schema['album']
        album_table_ref = bq.TableReference(dataset_ref=self.dataset,
            table_id = 'album')
        album_table = bq.Table(album_table_ref, schema=album_schema)
        self.create_table(album_table, album_table_ref, drop_and_replace)

        

    def load_bq(self, dataframe, table_name, truncate=False, reset_index=True) -> None:
        """
        Function to write a table to BigQuery

        Args:
            dataframe (str): 
        """
        # Load schema from self.bq_schema as created in the create_schema() method above
        schema = self.bq_schema[table_name]

        # Allows us to reset the index so the index column becomes a regular column
        if reset_index:
            dataframe.reset_index(inplace=True)

        table_ref = bq.TableReference(dataset_ref=self.dataset, table_id=table_name)

        # for a an internal table we define a JobConfig to specify write behavior and schema
        jc = bq.LoadJobConfig(
            schema=schema,
            autodetect=False,
            create_disposition='CREATE_NEVER',
            write_disposition='WRITE_TRUNCATE' if truncate else 'WRITE_APPEND',
        )
        # with the JobConfig and dataframe, we can simply use our client's load_table_from_dataframe method to populate BigQuery
        job = self.client.load_table_from_dataframe(dataframe, destination=table_ref, job_config=jc)
        job.result()


    def populate(self, artist_path, album_path) -> None:
        """
        Top level function to load all tables into our database
        """
 
        # load the data using the DataLoader
        artists = DataLoader(artist_path)
        # Load the data into BigQuery
        self.load_bq(artists.df, 'artists')

        albums = DataLoader(album_path)
        # Load the data into BigQuery
        self.load_bq(albums.df, 'albums')


