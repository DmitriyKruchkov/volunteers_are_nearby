import os
import time


def template_to_json(file_path):
    with open(file_path, 'r') as file:
        config_str = file.read()
    # Замена переменных среды
    for key, value in os.environ.items():
        if key == "DB_PORT":
            config_str = config_str.replace(f"${key}", value)
        else:
            config_str = config_str.replace(f"${key}", f'"{value}"')
    open("input_db.json", mode='w').write(config_str)


if __name__ == "__main__":
    template_to_json("input_db.json.template")
    time.sleep(60)
    user = os.getenv("PGADMIN_DEFAULT_EMAIL")
    os.system(f"python3 /pgadmin4/setup.py load-servers input_db.json --user {user}")
