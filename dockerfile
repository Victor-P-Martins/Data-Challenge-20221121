FROM python:3.10-slim

COPY . /opt/app

RUN pip install -r /opt/app/requirements.txt

WORKDIR /opt/app/api

CMD [ "uvicorn", "main:app","--host","0.0.0.0","--port","8000" ]

