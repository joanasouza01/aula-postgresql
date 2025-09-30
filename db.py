import psycopg2 as pg
#pip install psycopg2
#pip install dotenv
from dotenv import load_dotenv
import os

#carregar as variaveis do .env
load_dotenv()

params = {
    "db_name": os.getenv("db_name"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
}