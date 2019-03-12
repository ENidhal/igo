FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev && \
    pip install flask

COPY ./myflaskapp ./myflask

WORKDIR /myflask

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
