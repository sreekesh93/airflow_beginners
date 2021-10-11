from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

def print_hello(name):
    return 'Hello '+name+' !' 

dag = DAG('greeting', description='Greeting DAG',
          start_date=datetime(2021, 9, 6), catchup=False)

hello_bob_operator = PythonOperator(task_id='hello_bob', python_callable=print_hello, op_kwargs={'name':'Bob'}, dag=dag)

hello_alice_operator = PythonOperator(task_id='hello_alice', python_callable=print_hello, op_kwargs={'name':'Alice'}, dag=dag)

alice_question = BashOperator(task_id='question', bash_command='echo "what is the datetime"', dag=dag)

bob_answer = BashOperator(task_id='answer', bash_command='date', dag=dag)

hello_bob_operator > hello_alice_operator > alice_question > bob_answer

#view output of this in each stage log