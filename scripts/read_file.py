import pyarrow.parquet as pq


def read_parquet_file(filepath: str, filename: str = None):
    if filename is not None:
        filepath += filename

    # Specify the path to your Parquet file
    parquet_file_path = filepath

    # Read the Parquet file
    table = pq.read_table(parquet_file_path)

    # Convert the table to a Pandas DataFrame
    df = table.to_pandas()

    # Now, you can work with the DataFrame 'df'
    return df


if __name__ == "__main__":
    df = read_parquet_file("2023/December/yellow_tripdata_2023-12.parquet")
    print(df.head())
    print(df.columns)
