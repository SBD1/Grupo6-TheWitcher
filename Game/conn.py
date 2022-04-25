import psycopg2

def criaConexao():
    conn = psycopg2.connect(
        host="localhost",
        database="thewitcher",
        user="postgres",
        password="postgres")
    return conn

