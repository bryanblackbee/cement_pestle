# Pull base image
FROM python:3.7-slim
# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /ctpe_project
# Install dependencies
# COPY Pipfile Pipfile.lock /ctpe_project/
# RUN pip install pipenv && pipenv install --system
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# Copy project
COPY . /ctpe_project/