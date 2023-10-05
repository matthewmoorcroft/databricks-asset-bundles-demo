from os import path

import dlt
from pyspark.sql import DataFrame
from pyspark.sql.functions import regexp_replace


file_location = "/FileStore/tables/yellow_tripdata_2023_01.parquet"
file_type = "parquet"

df =  spark.read.format(file_type).load(file_location)


df.write.saveAsTable(f"")

@dlt.table
def medium_clean():
    df: DataFrame = dlt.read("medium_raw")
    df = df.filter(df.link != 'null')
    df = df.withColumn("author", regexp_replace("author", "\\([^()]*\\)", ""))
    return df
