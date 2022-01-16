FROM haproxy:1.7

RUN apt-get update
RUN apt-get install certbot -y


COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
