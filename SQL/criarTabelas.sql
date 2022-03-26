create domain tipo_item as VARCHAR(20) not null 
check (value in ('equipamento', 'consumivel', 'flecha'));

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
	CONSTRAINT fk_instancia_item FOREIGN KEY (id_instancia_item) REFERENCES instancia_item(id) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT fk_personagem FOREIGN KEY (id_personagem) REFERENCES personagem(id) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE mochila (
	id_personagem int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	peso float8 NULL,
	capacidade int4 NULL,
	CONSTRAINT mochila_pk PRIMARY KEY (id_personagem),
	CONSTRAINT mochila_fk FOREIGN KEY (id_personagem) REFERENCES personagem(id) ON DELETE CASCADE ON UPDATE CASCADE
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


CREATE TABLE instancia_monstro (
	id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	id_monstro int4 NULL,
	nivel int4 NULL,
	CONSTRAINT instancia_monstro_pk PRIMARY KEY (id),
	CONSTRAINT instancia_monstro_fk FOREIGN KEY (id) REFERENCES monstro(id)
);


CREATE TABLE monstro_dropa_item (
	id_instancia_monstro int4 NULL,
	id_instancia_item int4 NULL,
	CONSTRAINT instancia_item_fk FOREIGN KEY (id_instancia_monstro) REFERENCES instancia_item(id),
	CONSTRAINT instancia_monstro_fk FOREIGN KEY (id_instancia_monstro) REFERENCES instancia_monstro(id)
);