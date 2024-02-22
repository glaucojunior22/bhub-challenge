# pull official base image
FROM python:3.11-slim AS base-stage

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN apt-get update && \
    apt-get install -y gcc git

RUN pip install --no-cache-dir --ignore-installed --upgrade pip && \
    pip install --no-cache-dir --ignore-installed wheel==0.41.2 && \
    pip install --no-cache-dir --ignore-installed setuptools==68.2.2

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

FROM base-stage as dev-stage

RUN pip install -r requirements_dev.txt

ENTRYPOINT [ "python", "manage.py" ]

FROM base-stage AS prod-stage

ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:80" ]