create or replace function insere_drop() returns trigger as $trigger_dropa_item$
	begin 
		insert into monstro_dropa_item(id_instancia_monstro, id_instancia_item)
		values (instancia_monstro.id, instancia_monstro.instancia_item);
		return new;
	end;
$trigger_dropa_item$ language plpgsql

create trigger dropa_item after delete on instancia_monstro 
for each row execute procedure insere_drop();
