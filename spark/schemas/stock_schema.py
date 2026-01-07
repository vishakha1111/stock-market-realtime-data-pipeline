from pyspark.sql.types import StructType, StringType

stock_schema = StructType() \
    .add("Symbol", StringType()) \
    .add("Security Name", StringType()) \
    .add("Exchange", StringType()) \
    .add("ETF", StringType()) \
    .add("event_ts", StringType())
