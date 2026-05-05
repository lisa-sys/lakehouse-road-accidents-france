from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp, lit, input_file_name

from config import RAW_FILES, BRONZE_PATH, YEAR


def create_spark_session() -> SparkSession:
    """
    Create and return a local Spark session.
    """
    return (
        SparkSession.builder
        .appName("Lakehouse Road Accidents - Bronze Ingestion")
        .master("local[*]")
        .getOrCreate()
    )


def read_raw_csv(spark: SparkSession, file_path: str):
    """
    Read a raw CSV file using Spark.

    French road accident files are usually separated by semicolons.
    """
    return (
        spark.read
        .option("header", True)
        .option("sep", ";")
        .option("inferSchema", True)
        .option("encoding", "UTF-8")
        .csv(file_path)
    )


def write_bronze_table(df, table_name: str) -> None:
    """
    Write a DataFrame to the Bronze layer in Parquet format.
    """
    output_path = BRONZE_PATH / table_name

    (
        df.write
        .mode("overwrite")
        .parquet(str(output_path))
    )

    print(f"Bronze table written: {output_path}")


def ingest_table(spark: SparkSession, table_name: str, file_path) -> None:
    """
    Ingest one raw file into the Bronze layer.
    """
    print(f"Reading raw file for table: {table_name}")
    print(f"Source file: {file_path}")

    df = read_raw_csv(spark, str(file_path))

    df_bronze = (
        df
        .withColumn("ingestion_timestamp", current_timestamp())
        .withColumn("source_file", input_file_name())
        .withColumn("source_year", lit(YEAR))
    )

    print(f"Number of rows for {table_name}: {df_bronze.count()}")
    print(f"Number of columns for {table_name}: {len(df_bronze.columns)}")

    write_bronze_table(df_bronze, table_name)


def main() -> None:
    """
    Main function to ingest all raw files into the Bronze layer.
    """
    spark = create_spark_session()

    for table_name, file_path in RAW_FILES.items():
        ingest_table(spark, table_name, file_path)

    spark.stop()


if __name__ == "__main__":
    main()