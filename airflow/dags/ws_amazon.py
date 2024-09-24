from airflow import DAG
from airflow.operators.docker_operator import DockerOperator
from datetime import datetime

with DAG(
    "ws_amazon_dag",
    default_args={
        "owner": "airflow",
        "start_date": datetime(2023, 9, 24),
        "retries": 1,
    },
    schedule_interval=None,
    catchup=False,
) as dag:

    run_docker = DockerOperator(
        task_id="run_docker_image",
        image="jnyjhow/app_amazon:latest",
        api_version="auto",
        auto_remove=True,
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        command="python app.py",
        environment={
            "EXAMPLE_VAR": "value"
        },
        mount_tmp_dir=False,
    )

    run_docker
