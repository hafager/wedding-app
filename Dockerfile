FROM python:3.8

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        apache2
#        postgresql-client \
#    && rm -rf /var/lib/apt/lists/*

COPY httpd.conf /etc/apache2/conf-enabled/

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./mainsite ./mainsite
COPY ./wedding_site ./wedding_site
COPY manage.py .

EXPOSE 9000
CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]
