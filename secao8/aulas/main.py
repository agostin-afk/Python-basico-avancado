import sqlite3
from pathlib import Path


ROOT_DIR = Path(__file__).parent

DB_NAME = 'db.sqlite3'

DB_FILE = ROOT_DIR / DB_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

TABLE_NAME = 'customers'

# CUIDADO: sql injection
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)

connection.commit()

cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id, name, weight)'
    'VALUES (NULL, "Agostinho Ferreira", 9.9 )'
)

connection.commit()

# deleta a tabela:
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

connection.commit()

# deleta os id's:
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)

connection.commit()

# melhor jeito de inserir valor:
sql = (
    f'INSERT INTO {TABLE_NAME}'
    '(name, weight)'
    'VALUES'
    '(?, ?)'
)
cursor.execute(sql, ['Joana', 4])
# print(sql)
# passando mais de um valor:
cursor.executemany(
    sql,
    [
        ['Agosto', 13], ['Lucas', 22], ['Pedro', 17]
    ]
)

connection.commit()

if __name__ == '__main__':
    cursor.close()
    connection.close()
