#!/bin/bash

# Ожидание старта сервиса
sleep 30

# Авторизация в панель pgadmin
curl -X POST "http://$DB_USER:$DB_PASS@localhost:80/login?next=%2F" -H "Content-Type: application/json" -d '{"email": $PGADMIN_DEFAULT_EMAIL, "password": $PGADMIN_DEFAULT_PASSWORD}'

# Автоматическое подключение базы данных
curl -X POST "http://$DB_USER:$DB_PASS@localhost:80/servers" -H "Content-Type: application/json" -d '{
  "name": "volunteerium",
  "group": "Servers",
  "host": $DB_HOST,
  "port": $DB_PORT,
  "maintenance_db": $DB_NAME,
  "username": $DB_USER,
  "password": $DB_PASS,
  "sslmode": "prefer"
}'
