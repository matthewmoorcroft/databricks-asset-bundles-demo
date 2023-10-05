# Databricks notebook source
dbutils.widgets.text("catalog", "dev_cs_demo_matt")

# COMMAND ----------

file_location = "/FileStore/tables/yellow_tripdata_2023_01.parquet"
file_type = "parquet"

raw_daxi_df = spark.read.format(file_type).load(file_location)

# COMMAND ----------

catalog = dbutils.widgets.get("Catalog")
schema = "taxi"
table_name = "bronze_taxi_data"

raw_daxi_df.write.mode("overwrite").saveAsTable(f"{catalog}.{schema}.{table_name}")

# COMMAND ----------


