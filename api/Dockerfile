FROM python:3.8
ENV PYTHONUNBUFFERED 1

ADD ./src /src/
ADD requirements.txt /src/
WORKDIR /src
RUN pip install -r requirements.txt