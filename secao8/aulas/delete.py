import sqlite3
from main import DB_FILE, TABLE_NAME


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
# Delete perigoso:
cursor.execute(f'DELETE FORM {TABLE_NAME}')

# Melhor Delete:
cursor.execute(f'DELETE FROM sqlite_sequence WHERE name={TABLE_NAME}')

cursor.close()
connection.close()
