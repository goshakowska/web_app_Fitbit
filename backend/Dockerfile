FROM  python:3.8.13-bullseye

# Instalacja Oracle Instant Client
RUN apt-get update && apt-get install -y libaio1 wget unzip \
    && mkdir -p /opt/oracle \
    && wget https://download.oracle.com/otn_software/linux/instantclient/1919000/instantclient-basic-linux.x64-19.19.0.0.0dbru.el9.zip -O /opt/oracle/instantclient-basic-linux.x64.zip \
    && unzip /opt/oracle/instantclient-basic-linux.x64.zip -d /opt/oracle \
    && rm /opt/oracle/instantclient-basic-linux.x64.zip \
    && echo "/opt/oracle/instantclient_19_19" > /etc/ld.so.conf.d/oracle-instantclient.conf \
    && ldconfig

# Ustawienie zmiennej środowiskowej LD_LIBRARY_PATH
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_19_19:$LD_LIBRARY_PATH

ENV PYTHONUNBUFFERED=1

WORKDIR /django_backend

RUN pip install django django-cors-headers cx_Oracle

COPY . .

EXPOSE 8000
