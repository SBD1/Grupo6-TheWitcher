from conn import criaConexao

conn = criaConexao()

cur = conn.cursor()

sql = "select * from monstro"

cur.execute(sql)

rows = cur.fetchall()

for r in rows:
    print(r)

cur.close()
conn.close()