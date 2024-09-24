import requests
import time

DBT_CLOUD_API_TOKEN = "dbtu_f2KpY1wp2wqDTunJSYJihGmzNWp6rVzV2tUceNR4BcDYdhxEYA"
ACCOUNT_ID = "259115"
PROJECT_ID = "380538"
JOB_ID = "722218"

headers = {
    "Authorization": f"Token {DBT_CLOUD_API_TOKEN}",
    "Content-Type": "application/json",
}

data = {"cause": "Triggered via API"}

trigger_job_url = (
    f"https://cloud.getdbt.com/api/v2/accounts/{ACCOUNT_ID}/jobs/{JOB_ID}/run/"
)

response = requests.post(trigger_job_url, headers=headers, json=data)

if response.status_code == 200:
    run_data = response.json()["data"]
    run_id = run_data["id"]
    print(f"Job iniciada com sucesso! Run ID: {run_id}")

    check_run_url = (
        f"https://cloud.getdbt.com/api/v2/accounts/{ACCOUNT_ID}/runs/{run_id}/"
    )

    run_status = "Running"
    while run_status not in ["Success", "Error", "Cancelled"]:
        time.sleep(10)
        status_response = requests.get(check_run_url, headers=headers)
        run_status = status_response.json()["data"]["status_humanized"]
        print(f"Status atual da Job: {run_status}")

    print(f"Job finalizada com status: {run_status}")
else:
    print(f"Erro ao iniciar a Job: {response.status_code}, {response.text}")
