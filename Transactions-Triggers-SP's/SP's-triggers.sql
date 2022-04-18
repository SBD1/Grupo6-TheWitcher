-- Stored procedure para atualizar o gold do personagem após venda de item
create or replace function atualiza_gold() returns trigger as $atualiza_gold$
	begin 
		update personagem set gold = gold + i.preco
		from item i
		inner join instancia_item ii
		on i.id = ii.id_item 
		where ii.id =  old.item;
		return new;
	end;
$atualiza_gold$ 
language plpgsql;


-- Trigger para atualizar o gold depois de tirar item da mochila
create trigger trigger_vender_item after delete on mochila_guarda 
for each row execute procedure atualiza_gold();


-- Stored procedure para inserir item que o monstro dropa na mochila
create or replace function insere_drop() returns trigger as $insere_drop$
	begin 
		insert into mochila_guarda(mochila, item)
		values (1, (select old.instancia_item from instancia_monstro)); 
		return new;
	end;
$insere_drop$ 
language plpgsql;


-- Trigger para chamar a função sempre que uma instância de monstro for exluída
create trigger trigger_dropa_item after delete on instancia_monstro 
for each row execute procedure insere_drop();


-- Stored procedure para inserir contrato
create or replace function ativar_contrato() returns trigger as $ativar_contrato$
	begin 
		insert into contrato(gold, npc, missao)
		values ((select old.gold from contrato), (select old.npc from npc), (select old.missao from missao)); 
		return new;
	end;
$ativar_contrato$ 
language plpgsql;

-- Trigger para inserir contrato
create trigger trigger_ativar_contrato after update on contrato 
for each row execute procedure ativar_contrato();

-- Stored procedure para atualizar contrato
create or replace function desativar_contrato() returns trigger as $desativar_contrato$
	begin 
		update contrato set missao = missao - 1
		where gold = old.gold and npc = old.npc; 
		return null;
	end;
$desativar_contrato$ 
language plpgsql;

-- Trigger para atualizar contrato
create trigger trigger_desativar_contrato after delete on contrato 
for each row execute procedure desativar_contrato();


-- Stored procedure remover item da mochila, verifica antes se o item existe
CREATE OR REPLACE FUNCTION removerItemMochila(_mochila integer, _instancia_item integer)
RETURNS void AS $remove_item_mochila$
declare
BEGIN
	IF exists(select 1 from mochila_guarda WHERE mochila_guarda.item = _instancia_item) = false THEN
	    RAISE 'Item não existe na mochila';
	END IF;

	DELETE FROM mochila_guarda WHERE item = _instancia_item and mochila = _mochila;
	DELETE FROM instancia_item WHERE id = _instancia_item;
END;
$remove_item_mochila$ LANGUAGE plpgsql;

-- Trigger para verificar se o peso dos items dentro da mochila é maior que a capacidade limite da mochila
CREATE OR REPLACE FUNCTION checkCapacidadeMochila() RETURNS trigger AS $check_capacidade_mochila$
DECLARE
	capacidade_mochila INTEGER;
	peso_total float8;
BEGIN
	SELECT capacidade INTO capacidade_mochila FROM mochila;
	
	SELECT 
		SUM(item.peso)
	INTO peso_total
	FROM item 
	JOIN instancia_item
		ON (instancia_item.id_item = item.id)
	JOIN mochila_guarda
		ON (instancia_item.id = mochila_guarda.item);

	-- RAISE NOTICE 'Peso: %', peso_total;
	-- RAISE NOTICE 'Capacidade: %', capacidade_mochila;

	IF peso_total > capacidade_mochila THEN
		RAISE EXCEPTION 'Item não cabe na mochila';
	END IF;

	RETURN NEW;
END;
$check_capacidade_mochila$ LANGUAGE plpgsql;

DROP TRIGGER check_capacidade_mochila ON mochila_guarda;

CREATE TRIGGER check_capacidade_mochila
AFTER INSERT ON mochila_guarda
EXECUTE PROCEDURE checkCapacidadeMochila();

-- Stored procedure remover monstro, verifica antes se o monstro está no local descrito
CREATE OR REPLACE FUNCTION matarMonstro(_instancia_monstro integer)
RETURNS void AS $$
declare
BEGIN
    IF exists(select 1 from encontrado_em WHERE encontrado_em.id_instancia_monstro = _instancia_monstro) = false THEN
        RAISE 'Não foi encontrado um monstro no local especificado';
    END IF;

    UPDATE encontrado_em SET id_instancia_monstro = NULL WHERE id_instancia_monstro = _instancia_monstro;
    DELETE FROM instancia_monstro WHERE id = _instancia_monstro;
END;
$$ LANGUAGE plpgsql;

-- Trigger para adicionar localidade de item, ncp e monstro
CREATE OR REPLACE FUNCTION encontrar_em() RETURNS trigger AS $encontrar_em$
BEGIN
	INSERT INTO encontrado_em(id_area, id_ncp, id_instancia_monstro, id_instancia_item)
	VALUES ((select old.area from area), (select old.npc from npc), (select old.instancia_monstro from instancia_monstro), (select old.instancia_item from instancia_item))
	RETURN new;
END;
$encontrar_em$
language plpgsql;

-- Trigger para adicionar localidade de npc quando um for criado
CREATE OR REPLACE FUNCTION encontrar_npc_em() RETURNS trigger AS $encontrar_npc_em$
BEGIN
	INSERT INTO encontrado_em(id_area, id_ncp, id_instancia_monstro, id_instancia_item)
	VALUES ((select old.area from area), (select old.npc from npc), NULL, NULL)
	RETURN new;
END;
$encontrar_npc_em$
language plpgsql;

-- Trigger para adicionar localidade de monstro quando um for criado
CREATE OR REPLACE FUNCTION encontrar_monstro_em() RETURNS trigger AS $encontrar_monstro_em$
BEGIN
	INSERT INTO encontrado_em(id_area, id_ncp, id_instancia_monstro, id_instancia_item)
	VALUES ((select old.area from area), NULL, (select old.instancia_monstro from instancia_monstro), NULL)
	RETURN new;
END;
$encontrar_monstro_em$
language plpgsql;

-- Stored procedure terminar uma missão e receber a recompensa
CREATE OR REPLACE FUNCTION entregarItemMissao(_mochila_id integer, _contrato_id integer, _instancia_item_id integer)
RETURNS void AS $$
declare
    _instancia_item instancia_item; 
BEGIN
    IF exists(
        SELECT 1
        FROM contrato 
        WHERE is_ativo = true AND contrato.id = _contrato_id
    ) = false THEN
        RAISE 'A missão não está com o contrato ativo';
    END IF;

    IF exists(
        SELECT 1 FROM missao      
        INNER JOIN contrato 
        ON contrato.id = _contrato_id
        INNER JOIN instancia_item
        ON instancia_item.id = _instancia_item_id
        WHERE missao.item = instancia_item.id_item
    ) = false THEN
        RAISE 'O item recebido não é mesmo da missão';
    END IF;

    select removerItemMochila(_mochila_id, _instancia_item_id);

    -- entrega o gold para o usuario
    UPDATE personagem 
    SET gold = personagem.gold + contrato.gold
    FROM contrato
    WHERE contrato.id = _contrato_id;

    -- inativa o contrato
    select desativar_contrato(_contrato_id);
END;
$$ LANGUAGE plpgsql;

-- Stored procedure para evoluir habilidade do personagem
create or replace function evoluir_habilidade(_pontos_habilidade integer) returns trigger as $evoluir_habilidade$
	begin
		IF exists(SELECT 1 FROM habilidade WHERE habilidade.id = _pontos_habilidade_id) = false THEN
        RAISE 'A habilidade não foi encontrada';
    	END IF;

		update pontos_habilidade set pontos = pontos + 10
		from habilidade i
		where i.id_habilidade = old.id_habilidade;
		return new;
	end;
$evoluir_habilidade$ 
language plpgsql;