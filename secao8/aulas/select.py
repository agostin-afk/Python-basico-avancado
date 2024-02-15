import sqlite3
from main import DB_FILE, TABLE_NAME


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')
for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)
# para pegar um unico valor:
cursor.execute(
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id = "3"')
row = cursor.fetchone()
_id, name, weight = row
print(*row)
cursor.close()
connection.close()
