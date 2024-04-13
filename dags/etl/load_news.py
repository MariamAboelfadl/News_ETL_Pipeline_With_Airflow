import sqlite3

import pandas as pd


def load(**kwargs):
    ti = kwargs["ti"]
    file = ti.xcom_pull(task_ids="transform_task", key="transform_data")
    df_news = pd.read_parquet(file)

    
    conn = sqlite3.connect("sqlite:////home/mariam/Desktop/Airflow_project/sqlite3/news_data.db")

    df_news.to_sql("news_db", conn, if_exists="replace", index=False)

    conn.close()
