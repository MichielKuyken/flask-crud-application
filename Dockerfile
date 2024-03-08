FROM python:3.11.0-slim
WORKDIR /code
EXPOSE 5000
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN export FLASK_APP=crudapp.py
RUN flask db init
RUN flask db migrate -m "entries table"
RUN flask db upgrade
COPY ./app /code
COPY ./migrations /code
RUN mkdir -p /code/sqlitedb
RUN flask run