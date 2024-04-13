import datetime

import pandas as pd
import requests


def extract_api(**kwargs):
    ti = kwargs["ti"]
    api_key = ""
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=1)
    base_url = (
        "https://newsapi.org/v2/everything?q={}&from={}&to={}&sortBy=popularity&apiKey={}&language=en"
    )
    url_extractor = base_url.format("Covid", start_date, end_date, api_key)
    print(url_extractor)
    response = requests.get(url_extractor)
    data = response.json()
    df = pd.DataFrame()
    for i in data["articles"]:
        df["source"] = i["source"]
        df["author"] = i["author"]
        df["title"] = i["title"]
        df["description"] = i["description"]
        df["publishedAt"] = i["publishedAt"]
        df["content"] = i["content"]
    filename = "extract_api"
    filepath = f"/tmp/{filename}.parquet"
    df.to_parquet(filepath, engine="pyarrow")
    ti.xcom_push("extract_data", filepath)
    return filepath
