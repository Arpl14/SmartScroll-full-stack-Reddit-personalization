FROM apache/airflow:2.7.1-python3.9

USER airflow

COPY requirements.txt /requirements.txt
COPY config.ini /opt/airflow/config.ini

RUN pip install --no-cache-dir -r /requirements.txt