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