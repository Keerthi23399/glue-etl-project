from awsglue.context import GlueContext
from pyspark.context import SparkContext

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Example: ETL from S3 to S3
df = spark.read.csv("s3://dev-project-shivaya/Employee 1000x.csv", header=True)
df_cleaned = df.dropna()
df_cleaned.write.mode("overwrite").csv("s3://target-glue-job-etl/output/", header=True)
