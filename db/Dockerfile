FROM mysql:latest

ADD user.sql /docker-entrypoint-initdb.d/user.sql
RUN chmod -R 775 /docker-entrypoint-initdb.d
ENV MYSQL_ROOT_PASSWORD = Hamza#410

