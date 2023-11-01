from datetime import timedelta
import random

from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago 
from airflow.operators.empty import EmptyOperator

default_args = {
    'start_date': days_ago(2), # The start date for DAG running. This function allows us to set the start date to two days ago
    'schedule_interval': timedelta(days=1), # How often our DAG will run. After the start_date, airflow waits for the schedule_interval to pass then triggers the DAG run
    'retries': 1, # How many times to retry in case of failure
    'retry_delay': timedelta(minutes=5), # How long to wait before retrying
}

APPLES = ["pink lady", "jazz", "orange pippin", "granny smith", "red delicious", "gala"]

def print_hello():
    with open("/opt/airflow/dags/username.txt") as f:
        uname = f.read()
    print(f"hello, {uname}!")

def print_apple(apple_name):
    print(f"{apple_name}")


with DAG(
    'code_review_ch6', 
    description='DAG to greet a user', 
    default_args=default_args, 
) as dag:

    get_name_task = BashOperator(
        task_id='get_name_task',
        bash_command='echo Alma > /opt/airflow/dags/username.txt'
    )

    greeting_task = PythonOperator(
        task_id="greeting_task",
        python_callable=print_hello
    )

    get_apples_task = BashOperator(
        task_id='get_apples_task',
        bash_command='echo "getting three random apples"'
    )

    picked_apples_tasks = []
    for i in range(3):
        apple = random.choice(APPLES)
        task = PythonOperator(
            task_id=f"apple_{i}",
            python_callable=print_apple,
            op_kwargs={'apple_name': apple}
        )
        picked_apples_tasks.append(task)

    done_task = EmptyOperator(
        task_id='done_task',
    )


    get_name_task >> greeting_task >> get_apples_task >> picked_apples_tasks >> done_task
