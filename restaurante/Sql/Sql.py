import sqlite3

DATABASE = 'restaurante_banco.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Retorna os resultados como dicionario
    return conn

def close_db(conn):
    if conn:
        conn.close()


def getAllUsers(cursor):
        consulta=cursor.execute("SELECT nome,endereco,telefone FROM user ").fetchall()
        return consulta


def getCardapio(cursor):
        consulta=cursor.execute("SELECT * FROM cardapio").fetchall()
        return [dict(row) for row in consulta]