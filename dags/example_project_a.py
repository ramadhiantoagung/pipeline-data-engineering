import pendulum
from datetime import datetime, timedelta
from textwrap import dedent
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from lib.project_a import fn_proc_01, fn_proc_02, fn_proc_03

with DAG(
    dag_id="PROJECT_A",
    description="Pipeline_Project_a",
    start_date=pendulum.datetime(2024, 11, 5, tz="Asia/Jakarta"),
    schedule="1 1 * * *",
    catchup=True,
    tags=["PROD"],
    max_active_runs=1
) as dag:

    task_000 = PythonOperator(
        task_id='task_holder_open',
        python_callable=fn_proc_00,
        op_kwargs={
            "RunDate_str":"{{ dag_run.logical_date.astimezone(dag.timezone) | ds }}",
            "snf_user":"{{ var.value.snf_u_athena }}",
            "snf_pass":"{{ var.value.snf_p_athena }}",
            "snf_account":"{{ var.value.snf_acc }}",
            "snf_keypath":"{{ var.value.snf_key_athena }}"
        }
    )

    task_001 = PythonOperator(
        task_id='task_01',
        python_callable=fn_proc_01,
        op_kwargs={
            "RunDate_str":"{{ dag_run.logical_date.astimezone(dag.timezone) | ds }}",
            "snf_user":"{{ var.value.snf_u_athena }}",
            "snf_pass":"{{ var.value.snf_p_athena }}",
            "snf_account":"{{ var.value.snf_acc }}",
            "snf_keypath":"{{ var.value.snf_key_athena }}"
        }
    )

    task_002 = PythonOperator(
        task_id='task_02',
        python_callable=fn_proc_02,
        op_kwargs={
            "RunDate_str":"{{ dag_run.logical_date.astimezone(dag.timezone) | ds }}",
            "snf_user":"{{ var.value.snf_u_athena }}",
            "snf_pass":"{{ var.value.snf_p_athena }}",
            "snf_account":"{{ var.value.snf_acc }}",
            "snf_keypath":"{{ var.value.snf_key_athena }}"
        }
    )

    task_003 = PythonOperator(
        task_id='task_03',
        python_callable=fn_proc_03,
        op_kwargs={
            "RunDate_str":"{{ dag_run.logical_date.astimezone(dag.timezone) | ds }}",
            "snf_user":"{{ var.value.snf_u_athena }}",
            "snf_pass":"{{ var.value.snf_p_athena }}",
            "snf_account":"{{ var.value.snf_acc }}",
            "snf_keypath":"{{ var.value.snf_key_athena }}"
        }
    )

    task_999 = PythonOperator(
        task_id='task_holder_close',
        python_callable=fn_proc_99,
        op_kwargs={
            "RunDate_str":"{{ dag_run.logical_date.astimezone(dag.timezone) | ds }}",
            "snf_user":"{{ var.value.snf_u_athena }}",
            "snf_pass":"{{ var.value.snf_p_athena }}",
            "snf_account":"{{ var.value.snf_acc }}",
            "snf_keypath":"{{ var.value.snf_key_athena }}"
        }
    )

    task_000 >> task_001 >> [task_002,task_003], task_999