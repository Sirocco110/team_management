FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y
WORKDIR /team_management
COPY requirements.txt /team_management/
RUN pip install -r requirements.txt
ADD . /team_management/