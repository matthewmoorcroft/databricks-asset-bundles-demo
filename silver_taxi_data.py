# Databricks notebook source
dbutils.widgets.text("catalog", "dev_cs_demo_matt")

# COMMAND ----------

catalog = dbutils.widgets.get("Catalog")
schema = "taxi"
bronze_table = "bronze_taxi_data"

bronze_taxi_df = spark.read.table(f"{catalog}.{schema}.{bronze_table}")

# COMMAND ----------

silver_taxi_df = bronze_taxi_df.filter("passenger_count > 0 AND trip_distance > 0 AND total_amount > 0")

# COMMAND ----------

silver_table = "silver_taxi_data"
silver_taxi_df.write.mode("overwrite").saveAsTable(f"{catalog}.{schema}.{silver_table}")

# COMMAND ----------

"""
Create lookup table for payment type
1= Credit card; 
2= Cash; 
3= No charge; 
4= Dispute
"""

payment_types = [(1, "Credit card"),
                 (2, "Cash"),
                 (3, "No charge"),
                 (4, "Dispute")
                 ]

payment_types_df = spark.createDataFrame(payment_types, ["payment_type", "name"])
payment_types_df.write.mode("overwrite").saveAsTable(f"{catalog}.{schema}.lookup_payment_types")

# COMMAND ----------



# COMMAND ----------


