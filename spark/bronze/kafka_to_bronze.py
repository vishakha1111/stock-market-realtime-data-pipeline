from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from schemas.stock_schema import stock_schema


spark = (
    SparkSession.builder
    .appName("KafkaToBronze")
    .config("spark.hadoop.io.native.lib.available", "false")
    .config("spark.sql.streaming.forceDeleteTempCheckpointLocation", "true")
    .getOrCreate()
)


spark.sparkContext.setLogLevel("WARN")

kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "stock-events") \
    .option("startingOffsets", "latest") \
    .load()

parsed_df = kafka_df.select(
    from_json(col("value").cast("string"), stock_schema).alias("data")
).select("data.*")

query = parsed_df.writeStream \
    .format("parquet") \
    .option("path", "s3a://stock-market-bronze/stock_events/") \
    .option("checkpointLocation", "s3a://stock-market-bronze/checkpoints/") \
    .outputMode("append") \
    .start()

query.awaitTermination()
