FROM python:3.9-slim-buster

RUN apt-get update && \
    apt-get upgrade -y && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir /opt/app/ && \
    useradd -m -r appuser && \
    chown appuser /opt/app

WORKDIR /opt/app

COPY requirements.txt .

COPY app/ .

RUN pip install -r requirements.txt

USER appuser

EXPOSE 5000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
