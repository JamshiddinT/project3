#base image
FROM python:3.9.18-alpine3.18

#environment vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /project3

COPY requirements.txt /project3/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /project3/



