import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()
def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_host"),
        user=os.getenv("DB_user"),
        password=os.getenv("DB_password"),
        database=os.getenv("DB_database")
    )