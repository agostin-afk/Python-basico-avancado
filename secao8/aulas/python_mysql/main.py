import pymysql
import dotenv
import os
from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent / 'docker/.env'
dotenv.load_dotenv(ROOT_PATH)
TABLE_NAME = 'customers'

connection = pymysql.Connection(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    port=int(os.environ['MYSQL_PORT']),
)

"""
cursor = connection.cursor()


cursor.close()
connection.close()
"""
with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ( '
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id) '
            ') '
        )
#       apaga os dados da tabela:
        cursor.execute(
            f'TRUNCATE TABLE {TABLE_NAME}'
        )
        connection.commit()
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(nome)s, %(idade)s)'
        )
        data = {
            "nome": "Pedro",
            "idade": 34
        }
#        cursor.execute(sql, ('agosto', 45))
        cursor.execute(sql, data)
        connection.commit()
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(nome)s, %(idade)s)'
        )
        data2 = (
            {"nome": "Lucas", "idade": 21},
            {"nome": "Maria", "idade": 24},
            {"nome": "Agostinho", "idade": 25},
            {"nome": "Lucas", "idade": 26},
            {"nome": "Pedro", "idade": 19},
            {"nome": "jose", "idade": 18},
            {"nome": "will", "idade": 17},
        )
#        cursor.execute(sql, ('agosto', 45))
        cursor.executemany(sql, data2)
        connection.commit()
        '''
    with connection.cursor() as cursor:
        menor_id = int(input('informe o menor id: '))
        maior_id = int(input('informe o maior id: '))
        coluna = 'id'
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            f'WHERE id BETWEEN %s AND %s '
        )
        cursor.execute(sql, (menor_id, maior_id))
        print(cursor.mogrify(sql, (menor_id, maior_id)))
        data3 = cursor.fetchall()
        for row in data3:
            print(row)
        '''
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {TABLE_NAME} ")
        row = cursor.fetchall()
        print(*row, sep='\n')
        sql = (
            f'DELETE FROM {TABLE_NAME} WHERE id = "4" '
        )
        cursor.execute(sql)
        connection.commit()
        cursor.execute(
            f'SELECT * FROM {TABLE_NAME} '
        )
        data4 = cursor.fetchall()
        for row in data4:
            print(row)
