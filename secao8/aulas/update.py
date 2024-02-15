import sqlite3
from main import DB_FILE, TABLE_NAME


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'UPDATE {TABLE_NAME} '
    'SET name= "QUALQUER" '
    'WHERE id = '
)
connection.commit()
cursor.close()
connection.close()
