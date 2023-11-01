from pyspark.sql import SparkSession
import pandas as pd

spark = SparkSession.builder.getOrCreate()

pandas_df = pd.read_csv("../project-1/data/spotify_artists.csv")

spark_df = spark.createDataFrame(pandas_df)

spark_df.describe().show()