import sqlite3
from pathlib import Path


ROOT_DIR = Path(__file__).parent

DB_NAME = 'db.sqlite3'

DB_FILE = ROOT_DIR / DB_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

TABLE_NAME = 'customers'

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)

connection.commit()

cursor.close()
connection.close()
