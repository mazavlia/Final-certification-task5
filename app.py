from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("PostgresAndClickHouseSpark") \
    .config("spark.jars.packages", "org.postgresql:postgresql:42.5.1,ru.yandex.clickhouse:clickhouse-jdbc:0.3.2") \
    .getOrCreate()

# Configuration for connecting to PostgreSQL
jdbc_url_postgres = "jdbc:postgresql://localhost:5432/testdb"
properties_postgres = {
    "user": "user",
    "password": "password",
    "driver": "org.postgresql.Driver"
}

# Read data from PostgreSQL
df_postgres = spark.read.jdbc(url=jdbc_url_postgres, table="users", properties=properties_postgres)
print("PostgreSQL DataFrame:")
df_postgres.show()

# Configuration for connecting to ClickHouse
jdbc_url_clickhouse = "jdbc:clickhouse://localhost:8125/default"
properties_clickhouse = {
    "driver": "ru.yandex.clickhouse.ClickHouseDriver"
}

# Read data from ClickHouse
df_clickhouse = spark.read.jdbc(url=jdbc_url_clickhouse, table="users", properties=properties_clickhouse)
print("ClickHouse DataFrame:")
df_clickhouse.show()

# Stop the SparkSession
spark.stop()
