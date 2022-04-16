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
create trigger trigger_vender_item after delete on mochila 
for each row execute procedure atualiza_gold();


-- Stored procedure para inserir item que o monstro dropa na mochila
create or replace function insere_drop() returns trigger as $insere_drop$
	begin 
		insert into mochila(id_personagem, item)
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