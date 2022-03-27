create domain tipo_item as VARCHAR(20) not null 
check (value in ('equipamento', 'arma', 'consumivel', 'flecha'));

CREATE TABLE monstro (
	id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	nome varchar NULL,
	ataque float8 NULL,
	defesa float8 NULL,
	vida float8 NULL,
	tipo varchar NULL,
	classe varchar NULL,
	CONSTRAINT monstro_pk PRIMARY KEY (id)
);

CREATE TABLE item (
	id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	nome varchar NULL,
	tipo tipo_item NULL,
	descricao varchar NULL,
	preco float8 NULL,
	efeito varchar NULL,
	peso float8 NULL,
	dano int4 NULL,
	alcance float8 NULL,
	ataque int4 NULL,
	defesa int4 NULL,
	vida float8 NULL,
	CONSTRAINT item_pk PRIMARY KEY (id)
);

CREATE TABLE personagem (
	id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	nome varchar NULL,
	gold float4 NULL,
	vida int4 NULL,
	ataque int4 NULL,
	defesa int4 NULL,
	CONSTRAINT id PRIMARY KEY (id)
);

CREATE TABLE instancia_item (
	id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	id_item int4 NULL,
	nivel int4 NULL,
	CONSTRAINT instancia_item_pk PRIMARY KEY (id),
	CONSTRAINT instancia_item_fk FOREIGN KEY (id) REFERENCES item(id) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE itens_equipados (
	id_personagem int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	id_instancia_item int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	CONSTRAINT fk_instancia_item FOREIGN KEY (id_instancia_item) REFERENCES instancia_item(id) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT fk_personagem FOREIGN KEY (id_personagem) REFERENCES personagem(id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE mochila (
	id_personagem int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	peso float8 NULL,
	capacidade int4 NULL,
	CONSTRAINT mochila_pk PRIMARY KEY (id_personagem),
	CONSTRAINT mochila_fk FOREIGN KEY (id_personagem) REFERENCES personagem(id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE instancia_monstro (
	id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	id_monstro int4 NULL,
	nivel int4 NULL,
	instancia_item int4 NULL,
	CONSTRAINT instancia_monstro_pk PRIMARY KEY (id),
	CONSTRAINT instancia_item_fk FOREIGN KEY (instancia_item) REFERENCES instancia_item(id),
	CONSTRAINT instancia_monstro_fk FOREIGN KEY (id) REFERENCES monstro(id)
);


CREATE TABLE monstro_dropa_item (
	id_instancia_monstro int4 NULL,
	id_instancia_item int4 NULL,
	CONSTRAINT instancia_item_fk FOREIGN KEY (id_instancia_item) REFERENCES instancia_item(id),
	CONSTRAINT instancia_monstro_fk FOREIGN KEY (id_instancia_monstro) REFERENCES instancia_monstro(id)
);

CREATE TABLE Habilidade ( 
  id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
  nome VARCHAR(60) NOT NULL,
  tipo VARCHAR(60) NOT NULL,
  CONSTRAINT pk_habilidade PRIMARY KEY(ID)
);

CREATE TABLE pontos_habilidade ( 
	pontos INTEGER NOT NULL,
	id_personagem int4 NULL,
	id_habilidade int4 NULL,
	CONSTRAINT fk_pontos_habilidades_personagem FOREIGN KEY (id_personagem) REFERENCES personagem(id) ON DELETE RESTRICT,
	CONSTRAINT fk_pontos_habilidades_habilidades FOREIGN KEY (id_habilidade) REFERENCES habilidade(id) ON DELETE RESTRICT
);

CREATE TABLE esta_com_condicao_especial (
  efeito VARCHAR(60) NOT NULL UNIQUE,
  tipo VARCHAR(60) NOT NULL UNIQUE,
  duracao INTEGER NOT NULL,
  id_personagem int4 NULL,
  CONSTRAINT pk_esta_com_condição_especial PRIMARY KEY(efeito, tipo),
  CONSTRAINT fk_esta_com_condição_especial_personagem FOREIGN KEY (id_personagem) REFERENCES personagem(id) ON DELETE RESTRICT
);

CREATE TABLE npc ( 
	id SERIAL PRIMARY KEY,
	nome VARCHAR(255) NOT NULL,
	raca VARCHAR(255) NOT NULL,
	classe VARCHAR(255) NOT NULL
);

CREATE TABLE Negocia ( 
	id_personagem int4 NULL,
	id_npc int4 NULL,
	id_item int4 NULL,
  CONSTRAINT pk_negocia PRIMARY KEY(id_personagem, id_npc, id_item),
  CONSTRAINT fk_negocia_personagem FOREIGN KEY (id_personagem) REFERENCES personagem(id) ON DELETE RESTRICT,
  CONSTRAINT fk_negocia_npc FOREIGN KEY (id_npc) REFERENCES NPC(id) ON DELETE RESTRICT,
  CONSTRAINT fk_negocia_item FOREIGN KEY (id_item) REFERENCES Item(id) ON DELETE RESTRICT
);

CREATE TABLE Item_drop (
	id_monstro int4 NULL,
	id_item int4 NULL,
	CONSTRAINT pk_item_drop PRIMARY KEY(id_monstro, id_item),
    CONSTRAINT fk_itens_drop_monstro FOREIGN KEY (id_monstro) REFERENCES monstro(id) ON DELETE RESTRICT,
    CONSTRAINT fk_itens_drop_item FOREIGN KEY (id_item) REFERENCES personagem(id) ON DELETE RESTRICT
);

CREATE TABLE  Classe_monstro (
	id_monstro int4 NULL,
    classe SERIAL primary key unique NOT NULL,
    descricao varchar(100),
    tipo varchar(20) NOT NULL,
    CONSTRAINT fk_classe_monstro_monstro FOREIGN KEY (id_monstro) REFERENCES monstro(id) ON DELETE RESTRICT
);

CREATE TABLE missao ( 
	id SERIAL PRIMARY KEY,
	titulo VARCHAR(255) NOT NULL,
	descricao TEXT NULL,
	tipo VARCHAR(255) NOT NULL
);

CREATE TABLE contrato ( 
	id SERIAL PRIMARY KEY,
	gold float4 NULL,
	npc INTEGER NOT NULL,
	missao INTEGER NOT NULL,
	FOREIGN KEY (npc) REFERENCES npc (id),
	FOREIGN KEY (missao) REFERENCES missao (id)
);

CREATE TABLE contratos_ativos (
	contrato INTEGER NOT NULL,
	personagem INTEGER NOT NULL,
	CONSTRAINT pk_contratos_ativos PRIMARY KEY(contrato, personagem),
	FOREIGN KEY (contrato) REFERENCES contrato (id),
	FOREIGN KEY (personagem) REFERENCES personagem (id)
);

CREATE TABLE Area(
    ID INTEGER NOT NULL GENERATED BY DEFAULT AS IDENTITY,
    descricao varchar NULL,
    CONSTRAINT area_pk PRIMARY KEY (ID)
);

CREATE TABLE Mapa(
    ID integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    nome varchar(100) NOT NULL,
    tipo varchar(60) NOT NULL,
    pais varchar(60) NOT NULL,
    regiao varchar(60) NOT NULL,
    cidade varchar(60) NOT NULL,
    CONSTRAINT mapa_pk PRIMARY KEY (ID)
);

CREATE TABLE mapa_contem_area(
    id_mapa integer NOT NULL,
    id_area integer NOT NULL,
    CONSTRAINT mapa_contem_area_pk PRIMARY KEY (id_mapa, id_area),
    CONSTRAINT id_area_fk FOREIGN KEY (id_area)
        REFERENCES Area(ID)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT id_mapa FOREIGN KEY (id_mapa)
        REFERENCES Mapa(ID)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE encontrado_em
(
    id_area integer NOT NULL,
    id_ncp integer NULL,
    id_instancia_monstro integer NULL,
    id_instancia_item integer NULL,
    CONSTRAINT id_mapa_fk FOREIGN KEY (id_area)
        REFERENCES Area (ID) MATCH SIMPLE
        ON UPDATE RESTRICT
        ON DELETE RESTRICT,
	CONSTRAINT id_ncp_fk FOREIGN KEY (id_ncp)
        REFERENCES npc(id)
        ON UPDATE RESTRICT
        ON DELETE RESTRICT,
	CONSTRAINT id_instancia_monstro_fk FOREIGN KEY (id_instancia_monstro)
        REFERENCES instancia_monstro(id)
        ON UPDATE RESTRICT
        ON DELETE RESTRICT,
	CONSTRAINT id_instancia_item_fk FOREIGN KEY (id_instancia_item)
        REFERENCES instancia_item(id)
        ON UPDATE RESTRICT
        ON DELETE RESTRICT	
);
