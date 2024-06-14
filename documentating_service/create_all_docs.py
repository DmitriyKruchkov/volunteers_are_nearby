import os
import click


@click.command()
@click.option("--path", default="../flaskr",
              help="Зath to the directory you want to document")
def create_all_docs(path):
    ignore_dirs = ["__pycache__", "db", "templates", "static"]
    directories = []
    for elem in os.listdir(path):
        if os.path.isdir(os.path.join(path, elem)) and elem not in ignore_dirs:
            directories.append(elem)
    for i in directories:
        os.system(f"sphinx-apidoc -f -o ../docs/source {os.path.join(path, i)}")
    os.system("make html")


if __name__ == "__main__":
    create_all_docs()
