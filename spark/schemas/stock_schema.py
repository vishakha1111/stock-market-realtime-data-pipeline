from pyspark.sql.types import *

stock_schema = StructType([
    StructField("symbol", StringType(), True),
    StructField("name", StringType(), True),
    StructField("exchange", StringType(), True),
    StructField("assetType", StringType(), True),
    StructField("ipoDate", StringType(), True),
    StructField("delistingDate", StringType(), True),
    StructField("status", StringType(), True),
    StructField("event_time", TimestampType(), True)
])
