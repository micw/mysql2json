FROM alpine:3.14

RUN apk add --update --no-cache python3 py3-pip && \
    pip install mysql-connector

ADD mysql2json.py /mysql2json.py

CMD /mysql2json.py
