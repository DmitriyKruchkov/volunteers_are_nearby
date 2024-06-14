#!/bin/sh

# Запуск основного entrypoint для запуска веб-сервера
/entrypoint.sh &

# Ожидание 20 секунд
sleep 20

# Запуск скрипта qwe.py
venv/bin/python3 /tmp/db_adder.py