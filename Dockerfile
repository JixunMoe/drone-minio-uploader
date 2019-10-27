FROM python:3.8-alpine3.10

RUN pip install -r requirements.txt

COPY uploader /usr/local/lib/python3.8/site-packages/uploader
COPY requirements.txt .
COPY upload /bin/upload

RUN chmod a+x /bin/upload
