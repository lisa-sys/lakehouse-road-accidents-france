from pyspark.sql import SparkSession

from config import BRONZE_PATH


BRONZE_TABLES = [
    "caracteristiques",
    "lieux",
    "usagers",
    "vehicules",
]


def create_spark_session() -> SparkSession:
    """
    Create and return a local Spark session.
    """
    return (
        SparkSession.builder
        .appName("Lakehouse Road Accidents - Validate Bronze")
        .master("local[*]")
        .getOrCreate()
    )


def validate_bronze_table(spark: SparkSession, table_name: str) -> None:
    """
    Read a Bronze table and print basic validation information.
    """
    table_path = BRONZE_PATH / table_name

    print("=" * 80)
    print(f"Validating Bronze table: {table_name}")
    print(f"Path: {table_path}")

    df = spark.read.parquet(str(table_path))

    row_count = df.count()
    column_count = len(df.columns)

    print(f"Rows: {row_count}")
    print(f"Columns: {column_count}")
    print("Schema:")
    df.printSchema()

    print("Sample rows:")
    df.show(5, truncate=False)


def main() -> None:
    """
    Validate all Bronze tables.
    """
    spark = create_spark_session()

    for table_name in BRONZE_TABLES:
        validate_bronze_table(spark, table_name)

    spark.stop()


if __name__ == "__main__":
    main()