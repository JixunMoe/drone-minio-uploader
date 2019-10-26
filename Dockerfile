FROM python3:3.8-alpine3.10

COPY uploader /uploader
COPY requirements.txt .
COPY upload /bin/upload

RUN chmod a+x /bin/upload
RUN pip -r requirements.txt
