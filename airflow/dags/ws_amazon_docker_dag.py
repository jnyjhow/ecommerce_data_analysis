from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "start_date": datetime(2023, 10, 1),
}

with DAG(
    "ws_amazon_docker_dag",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:

    executar_imagem_docker = DockerOperator(
        task_id="ws_amazon_docker_task",
        image="jnyjhow/app_amazon:latest",
        command=["python", "app.py"],
        # auto_remove=True,
        auto_remove='success',
        docker_url="unix://var/run/docker.sock",
        network_mode="ecommerce_data_analysis_default",
    )
