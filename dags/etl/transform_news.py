import pandas as pd


def transform(**kwargs):
    ti = kwargs["ti"]
    filename = ti.xcom_pull(task_ids="extract_task", key="extract_data")
    df = pd.read_parquet(filename)
    print(df.info())
    df["author"] = df["author"].str.lower()
    df["content"] = df["content"].str.lower()
    df["title"] = df["title"].str.lower()
    df["description"] = df["description"].str.lower()
    df.rename(
        columns={"author": "author_name", "publishedAt": "publish_datetime"},
        inplace=True,
    )
    df["publish_datetime"] = pd.to_datetime(df["publish_datetime"])
    filename = "transform"
    filepath = f"/tmp/{filename}.parquet"
    df.to_parquet(filepath, engine="pyarrow")
    ti.xcom_push("transform_data", filepath)
    return filepath
