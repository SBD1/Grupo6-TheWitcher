import psycopg2
from conn import criaConexao

conn = criaConexao()
cur = conn.cursor()

def truncate_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        
        """
        TRUNCATE TABLE monstro RESTART IDENTITY CASCADE;

        """,

        """
        TRUNCATE TABLE mapa RESTART IDENTITY CASCADE;
        """,

        """
        TRUNCATE TABLE item RESTART IDENTITY CASCADE;
        """,

        """
        TRUNCATE TABLE personagem RESTART IDENTITY CASCADE;
        """,
        """
        TRUNCATE TABLE instancia_item RESTART IDENTITY CASCADE;
        """,

        """
         TRUNCATE TABLE mochila RESTART IDENTITY CASCADE;
        
        """,


        """
        TRUNCATE TABLE instancia_monstro RESTART IDENTITY CASCADE;
        """,

        """
        TRUNCATE TABLE Habilidade RESTART IDENTITY CASCADE;

        """,

        """
        TRUNCATE TABLE npc RESTART IDENTITY CASCADE;
        """,

        """
        TRUNCATE TABLE missao RESTART IDENTITY CASCADE;
        """,
        """
         TRUNCATE TABLE contrato RESTART IDENTITY CASCADE;
        """,
        """
         TRUNCATE TABLE area RESTART IDENTITY CASCADE;
        """
        )
    try:
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        print("Tabelas Resetadas")

if __name__ == '__main__':
    truncate_tables()