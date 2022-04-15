-- Função para atualizar o gold do personagem após venda de item
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


-- Função para inserir os itens na tabela de monstro_dropa_item
create or replace function insere_drop() returns trigger as $insere_drop$
	begin 
		insert into monstro_dropa_item(id_instancia_monstro, id_instancia_item)
		values ((select old.id from instancia_monstro where id = old.id), 
				(select old.instancia_item from instancia_monstro where instancia_item = old.instancia_item)); 
		return new;
	end;
$insere_drop$ 
language plpgsql;


-- Trigger para chamar a função sempre que uma instância de monstro for exluída
create trigger trigger_dropa_item after delete on instancia_monstro 
for each row execute function insere_drop();