FROM mysql:latest
WORKDIR  /app
COPY  . /app/

RUN ls /app

ENV MYSQL_ROOT_PASSWORD = Hamza#410
ADD user.sql /docker-entrypoint-initdb.d/

EXPOSE 3306

