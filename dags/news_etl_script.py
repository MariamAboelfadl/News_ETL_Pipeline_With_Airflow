
import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator

from etl.extract_news import extract_api 
from etl.load_news import load
from etl.transform_news import transform


args = {"owner": "admin", "start_date": airflow.utils.dates.days_ago(2)}
dag = DAG(dag_id="news_etl_script", default_args=args, schedule_interval=None)
with dag:
    extract_task = PythonOperator(
        task_id="extract_task", python_callable=extract_api, dag=dag
    )
    transform_task = PythonOperator(
        task_id="transform_task", python_callable=transform, dag=dag
    )
    load_task = PythonOperator(
        task_id="load_task", python_callable=load, dag=dag
    )
    
    extract_task >> transform_task >> load_task 
