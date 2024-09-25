from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import (
    KubernetesPodOperator,
)
from airflow.utils.dates import days_ago

with DAG(
    "k8s_ws_amazon_dag",
    default_args={
        "owner": "airflow",
        "start_date": days_ago(1),
    },
    schedule_interval=None,
    catchup=False,
) as dag:

    run_kubernetes_pod = KubernetesPodOperator(
        namespace="default",
        image="jnyjhow/app_amazon:latest",
        # image='registry.localhost:5000/jnyjhow/app_amazon:latest',
        cmds=["python", "app.py"],
        name="k8s_ws_amazon_pod",
        task_id="k8s_ws_amazon_task",
        get_logs=True,
        in_cluster=False,
        #is_delete_operator_pod=True,
        cluster_context='k3d-mycluster',
        config_file='/opt/airflow/config/kubeconfig',
    )

    run_kubernetes_pod
