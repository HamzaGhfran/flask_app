FROM mysql:latest

WORKDIR /app
ADD  . /app/

ENV MYSQL_ROOT_PASSWORD = Hamza#410
COPY  user.sql /docker-entrypoint-initdb.d/
