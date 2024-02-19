import sqlite3
from main import DB_FILE, TABLE_NAME


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
# Delete perigoso:
cursor.execute(f'DELETE FORM {TABLE_NAME}')
connection.commit()

# Melhor Delete:
cursor.execute(f'DELETE FROM sqlite_sequence WHERE name={TABLE_NAME}')
connection.commit()

# Deletar dados pelo id:
cursor.execute(
    f'DELETE FROM {TABLE_NAME} '
    'WHERE id = "1"'
)
connection.commit()

cursor.close()
connection.close()
