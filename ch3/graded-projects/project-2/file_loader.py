import pandas as pd


# Creating our base data loading class
class DataLoader():
    def __init__(self, filepath, index=None, multi_file_load=False) -> None:
        df = pd.read_csv(filepath, header=0)
        # Set index of our data if specified.
        if index is not None:
            df =df.set_index(index)
        self.df = df
    
        
    def add_index(self, col_list, index_name="index") -> None:
        """
        Create an index column by concatonating a list of columns into a str
        """
        df = self.df
        # Concatonate the columns in col_list into an index column to serve as our primary key
        df[index_name] = df[col_list].apply(lambda row: "-".join(row.values.astype(str)), axis=1)
        df.set_index(index_name, inplace=True)
        self.df = df
    







        
