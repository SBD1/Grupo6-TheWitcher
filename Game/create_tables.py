import psycopg2
from conn import criaConexao

conn = criaConexao()
cur = conn.cursor()

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        create domain tipo_item as VARCHAR(20) not null 
        check (value in ('equipamento', 'arma', 'consumivel', 'flecha', 'item_missao'));
        """,

        """
        create domain tipo_habilidade as VARCHAR(20) NOT NULL
        check (value in ('Combate', 'Sinais', 'Alquimia'));
        """,

        """

        CREATE TABLE monstro (
            id SERIAL NOT NULL,
            nome varchar NULL,
            ataque float8 NULL,
            defesa float8 NULL,
            vida float8 NULL,
            classe varchar NULL,
            descricao varchar NULL,
            CONSTRAINT monstro_pk PRIMARY KEY (id)
        );
        """,

        """
        CREATE TABLE mapa (
            id SERIAL NOT NULL,
            nome varchar NOT NULL,
            tipo varchar NOT NULL,
            pais varchar NOT NULL,
            regiao varchar NULL,
            CONSTRAINT mapa_pk PRIMARY KEY (id)
        );
        """,

        """
        CREATE TABLE item (
            id SERIAL NOT NULL,
            nome varchar NULL,
            tipo tipo_item NULL,
            descricao varchar NULL,
            preco float8 NULL,
            efeito varchar NULL,
            peso float8 NULL,
            alcance float8 NULL,
            ataque int4 NULL,
            defesa int4 NULL,
            vida float8 NULL,
            CONSTRAINT item_pk PRIMARY KEY (id)
        );
        """,

        """
        CREATE TABLE personagem (
            id SERIAL NOT NULL,
            nome varchar NULL,
            gold float4 NULL,
            vida int4 NULL,
            ataque int4 NULL,
            defesa int4 NULL,
            CONSTRAINT id PRIMARY KEY (id)
        );
        """,
        """
        CREATE TABLE instancia_item (
            id SERIAL NOT NULL,
            id_item int4 NULL,
            nivel int4 NULL,
            CONSTRAINT instancia_item_pk PRIMARY KEY (id),
            CONSTRAINT instancia_item_fk FOREIGN KEY (id_item) REFERENCES item(id) ON DELETE CASCADE ON UPDATE CASCADE
        );
        """,

        """
        CREATE TABLE itens_equipados (
            id_personagem int4 NOT NULL,
            id_instancia_item int4 NULL,
            ataque_item int4 NULL,
            defesa_item int4 NULL,
            vida_item int4 NULL,
            CONSTRAINT fk_instancia_item FOREIGN KEY (id_instancia_item) REFERENCES instancia_item(id) ON UPDATE CASCADE ON DELETE CASCADE,
            CONSTRAINT fk_personagem FOREIGN KEY (id_personagem) REFERENCES personagem(id) ON UPDATE CASCADE ON DELETE CASCADE
        );
        """,
        """
        CREATE TABLE mochila (
            id SERIAL NOT NULL,
            id_personagem int4 NOT NULL,
            capacidade int4 NULL,
            CONSTRAINT mochila_pk PRIMARY KEY (id),
            CONSTRAINT personagem_fk FOREIGN KEY (id_personagem) REFERENCES personagem(id) ON DELETE CASCADE ON UPDATE CASCADE
        );
        """,

        """
        CREATE TABLE mochila_guarda (
            mochila int4 NULL,
            item int4 NULL,
            CONSTRAINT instancia_item_fk FOREIGN KEY (item) REFERENCES instancia_item(id),
            CONSTRAINT mochila_fk FOREIGN KEY (mochila) REFERENCES mochila(id)
        );
        """,

        """
        CREATE TABLE instancia_monstro (
            id SERIAL NOT NULL,
            id_monstro int4 NULL,
            nivel int4 NULL,
            instancia_item int4 NULL,
            CONSTRAINT instancia_monstro_pk PRIMARY KEY (id),
            CONSTRAINT instancia_item_fk FOREIGN KEY (instancia_item) REFERENCES instancia_item(id),
            CONSTRAINT instancia_monstro_fk FOREIGN KEY (id_monstro) REFERENCES monstro(id)
        );
        """,

        """
        CREATE TABLE monstro_dropa_item (
            id_instancia_monstro int4 NULL,
            id_instancia_item int4 NULL,
            CONSTRAINT instancia_item_fk FOREIGN KEY (id_instancia_item) REFERENCES instancia_item(id),
            CONSTRAINT instancia_monstro_fk FOREIGN KEY (id_instancia_monstro) REFERENCES instancia_monstro(id)
        );
        """,

        """
        CREATE TABLE Habilidade ( 
        id SERIAL NOT NULL,
        nome VARCHAR(60) NOT NULL,
        tipo tipo_habilidade NOT NULL,
        CONSTRAINT pk_habilidade PRIMARY KEY(id)
        );
        """,

        """
        CREATE TABLE pontos_habilidade ( 
            pontos INTEGER NOT NULL,
            id_personagem int4 NULL,
            id_habilidade int4 NULL,
            CONSTRAINT fk_pontos_habilidades_personagem FOREIGN KEY (id_personagem) REFERENCES personagem(id) ON DELETE RESTRICT,
            CONSTRAINT fk_pontos_habilidades_habilidades FOREIGN KEY (id_habilidade) REFERENCES habilidade(id) ON DELETE RESTRICT
        );
        """,

        """
        CREATE TABLE esta_com_condicao_especial (
        efeito VARCHAR(60) NOT NULL UNIQUE,
        tipo VARCHAR(60) NOT NULL UNIQUE,
        duracao INTEGER NOT NULL,
        id_personagem int4 NULL,
        CONSTRAINT pk_esta_com_condi????o_especial PRIMARY KEY(efeito, tipo),
        CONSTRAINT fk_esta_com_condi????o_especial_personagem FOREIGN KEY (id_personagem) REFERENCES personagem(id) ON DELETE RESTRICT
        );
        """,

        """
        CREATE TABLE npc ( 
            id SERIAL PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            raca VARCHAR(255) NOT NULL,
            classe VARCHAR(255) NOT NULL
        );
        """,

        """
        CREATE TABLE npc_negocia_item ( 
            id_npc int4 NULL,
            id_item int4 NULL,
        CONSTRAINT fk_negocia_npc FOREIGN KEY (id_npc) REFERENCES NPC(id) ON DELETE RESTRICT,
        CONSTRAINT fk_negocia_item FOREIGN KEY (id_item) REFERENCES item(id) ON DELETE RESTRICT
        );
        """,

        """
        CREATE TABLE missao ( 
            id SERIAL PRIMARY KEY,
            titulo VARCHAR(255) NOT NULL,
            descricao TEXT NULL,
            tipo VARCHAR(255) NOT NULL,
            item int4 NULL,
            CONSTRAINT item_fk FOREIGN KEY (item) REFERENCES item(id)
        );
        """,
        """
        CREATE TABLE contrato ( 
            id SERIAL PRIMARY KEY,
            gold float4 NULL,
            npc INTEGER NOT NULL,
            missao INTEGER NOT NULL,
            FOREIGN KEY (npc) REFERENCES npc (id),
            FOREIGN KEY (missao) REFERENCES missao (id)
        );
        """,
        """
        CREATE TABLE area (
            id SERIAL NOT NULL,
            descricao varchar NOT NULL,
            id_mapa int4 NULL,
            CONSTRAINT area_pk PRIMARY KEY (id),
            CONSTRAINT mapa_fk FOREIGN KEY (id_mapa) REFERENCES public.mapa(id) ON DELETE CASCADE ON UPDATE CASCADE
        );
        """,

        """
        CREATE TABLE encontrado_em
        (
            id_area integer NULL,
            id_npc integer NULL,
            id_instancia_monstro integer NULL,
            id_instancia_item integer NULL,
            CONSTRAINT id_mapa_fk FOREIGN KEY (id_area)
                REFERENCES area (id) MATCH SIMPLE,
            CONSTRAINT id_npc_fk FOREIGN KEY (id_npc)
                REFERENCES npc(id),
            CONSTRAINT id_instancia_monstro_fk FOREIGN KEY (id_instancia_monstro)
                REFERENCES instancia_monstro(id),
            CONSTRAINT id_instancia_item_fk FOREIGN KEY (id_instancia_item)
                REFERENCES instancia_item(id)
                ON UPDATE CASCADE
                ON DELETE CASCADE	
        );
        """,

        """
        ALTER TABLE contrato ADD is_ativo bool NULL;
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
        print("Tabelas Criadas")

if __name__ == '__main__':
    create_tables()