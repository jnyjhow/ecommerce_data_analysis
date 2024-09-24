from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from ws_mercado_livre.variables import *
from ws_mercado_livre.functions import *

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 9, 1),
    "email": ["jhonatan_yamane@hotmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    dag_id="ws_mercado_livre_dag",
    default_args=default_args,
    description="DAG para processar ofertas do Mercado Livre",
    schedule_interval=timedelta(days=1),
)


def check_directory(**kwargs):
    pfun_check_dir(VAR_PATH_RESULT_AUX)


def get_offers(**kwargs):
    lista_ofertas = pfun_ml_get_products()
    return lista_ofertas


def create_dataframe(**kwargs):
    ti = kwargs["ti"]
    lista_ofertas = ti.xcom_pull(task_ids="get_offers")
    df_ofertas = pfun_get_df(lista_ofertas)


with dag:
    task_check_directory = PythonOperator(
        task_id="check_directory",
        python_callable=check_directory,
        provide_context=True,
    )

    task_get_offers = PythonOperator(
        task_id="get_offers",
        python_callable=get_offers,
        provide_context=True,
    )

    task_create_dataframe = PythonOperator(
        task_id="create_dataframe",
        python_callable=create_dataframe,
        provide_context=True,
    )

    (
        task_check_directory
        >> task_get_offers
        >> task_create_dataframe
    )
