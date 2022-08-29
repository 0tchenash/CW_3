FROM python:3.10-alpine

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD python3 create_tables.py && python3 load_fixtures.py && export FLASK_APP=server.py && flask run -h 0.0.0.0 -p 80