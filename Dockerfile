FROM python:3.8

ADD requirements.txt /app/requirements.txt

RUN python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /app/requirements.txt

ADD manage.py /app/manage.py
ADD mainsite /app/mainsite
WORKDIR /app

EXPOSE 9000

ADD startup.sh .

CMD ["./startup.sh"]