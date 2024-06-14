import os
import time


def template_to_json(file_path):
    with open(file_path, 'r') as file:
        config_str = file.read()
    # Замена переменных среды
    for key, value in os.environ.items():
        config_str = config_str.replace(f"${key}", value)
    open("input_db.json", mode='w').write(config_str)


if __name__ == "__main__":
    template_to_json("input_db.json.template")
    time.sleep(10)
    os.system("/venv/bin/python3 /pgadmin4/setup.py load-servers input_db.json --user $PGADMIN_DEFAULT_EMAIL")
