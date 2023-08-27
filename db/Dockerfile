FROM mysql:latest
WORKDIR  /app
ADD  . /app/
ENV MYSQL_ROOT_PASSWORD = Hamza#410
RUN ls /app
ADD user.sql /docker-entrypoint-initdb.d/

EXPOSE 3306

