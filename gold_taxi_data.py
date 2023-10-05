# Databricks notebook source
dbutils.widgets.text("Catalog", "dev_cs_demo_matt")

# COMMAND ----------

catalog = dbutils.widgets.get("Catalog")
schema = "taxi"
silver_table = "silver_taxi_data"

silver_taxi_df = spark.read.table(f"{catalog}.{schema}.{silver_table}")

# COMMAND ----------

gold_taxi_df = silver_taxi_df.filter("payment_type in (1,2) AND year(tpep_pickup_datetime) = 2023")


# COMMAND ----------

payment_types_df = spark.read.table(f"{catalog}.{schema}.lookup_payment_types")

# COMMAND ----------

gold_taxi_df = gold_taxi_df.join(payment_types_df, on="payment_type")


# COMMAND ----------

from pyspark.sql.functions import to_date

gold_taxi_df = ( gold_taxi_df
 .select(to_date("tpep_dropoff_datetime").alias("drop_off_date"), "payment_type", "name")
 .groupBy("drop_off_date", "name")
 .count()
)

# COMMAND ----------

gold_taxi_df.display()


# COMMAND ----------

gold_table = "gold_taxi_cash_vs_cc"
gold_taxi_df.write.mode("overwrite").saveAsTable(f"{catalog}.{schema}.{gold_table}")

# COMMAND ----------


