from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from src.repeat_prescription_run import run
from datetime import datetime, timedelta


dag_args ={
            "owner": "airflow",
            "retries": 1,
            "retry_delay": timedelta(minutes=5),
            "start_date": datetime(2021, 1, 1),
        }

dag = DAG (
    dag_id="repeat_prescription",
    schedule_interval="@monthly",
    default_args=dag_args,
    catchup=False,
    description="repeat_prescription"
)

task = PythonOperator(
        task_id="gather_user_data",
        python_callable=run,
        dag=dag
    )

task