FROM  python:3.8.13-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app/backend


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

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
