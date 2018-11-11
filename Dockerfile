FROM python:3.6-alpine

EXPOSE 80

COPY . /app
WORKDIR /app
RUN apk add gcc musl-dev libffi-dev libressl-dev
RUN pip install pipenv
RUN pipenv run pip install pip==18.0  # bugfix for pipenv issue #2924
RUN pipenv install
CMD pipenv run prod
