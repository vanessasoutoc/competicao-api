# Dockerfile

# pull the official docker image
FROM python:3.11.0-slim

# set work directory
WORKDIR /src


# install dependencies
COPY requirements.txt ./
RUN apt-get update && apt-get install -y git
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .
