#Deriving the latest base image
FROM python:3.7.9-slim-buster
LABEL Maintainer="mohsin996"
WORKDIR /usr/app/src
COPY requirements.txt ./
COPY app.py ./
RUN pip install --no-cache-dir -r requirements.txt
RUN sleep 3
CMD [ "python", "./app.py"]