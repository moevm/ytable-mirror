ARG BASE_IMAGE="python:3.10"
FROM ${BASE_IMAGE}
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y python3

WORKDIR /
COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]