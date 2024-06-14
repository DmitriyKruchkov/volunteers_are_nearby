import os

# web_app connect settings
SECRET_KEY = os.getenv('SECRET_KEY')
HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))
DEBUG = os.getenv('DEBUG') == 'True'
USER_DATA_DIR = os.getenv('USER_DATA_DIR')
EVENT_DATA_DIR = os.getenv('EVENT_DATA_DIR')
NON_AVATAR_PATH = os.getenv('NON_AVATAR_PATH')

# redis connect settings
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = int(os.getenv('REDIS_PORT'))
REDIS_UPDATE_SECONDS = int(os.getenv('REDIS_UPDATE_SECONDS'))

# mailer connect settings
MAILER_HOST = os.getenv('MAILER_HOST')
MAILER_PORT = int(os.getenv('MAILER_PORT'))

# postgresql connect settings
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')