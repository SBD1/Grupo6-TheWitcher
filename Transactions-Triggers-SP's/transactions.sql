-- Transaction de compra de item

begin;

insert into instancia_item (id_item) values (1);

savepoint adiciona_instancia;

update personagem set gold = gold - i.preco
from item i
where i.id = 1;

savepoint desconta_gold;

update mochila set capacidade = capacidade-1; 
 
delete from mochila_guarda where item = 1;


commit;


-- update básico de itens
begin;

update itens_equipados set ataque_item = ataque_item+5, defesa_item  = defesa_item+7, vida_item = vida_item+10 
from item i 
where itens_equipados.id_item = i.id; 

update personagem set gold = gold - 20;
	
commit;


-- update intermediário de itens
begin;

update itens_equipados set ataque_item = ataque_item+8, defesa_item  = defesa_item+13, vida_item = vida_item+15 
from item i 
where itens_equipados.id_item = i.id; 

update personagem set gold = gold - 35;
	
commit;


-- update superior de itens
begin;

update itens_equipados set ataque_item = ataque_item+12, defesa_item  = defesa_item+16, vida_item = vida_item+20 
from item i 
where itens_equipados.id_item = i.id; 

update personagem set gold = gold - 50;
	
commit;

-- remove item da mochila
begin;

select removerItemMochila(1,1);

commit;


-- matar monstro
begin;

select matarMonstro(3);

commit;


-- update encontrado em uma área com npc, monstro e item
begin;

insert into encontrado_em(id_area) values (1);
savepoint adiciona_area;

select encontrar_item();

commit;

-- entrega item da mochila para a missão ser concluida e o usuário receber o gold
begin;

select entregarItemMissao(1, 1, 1);

commit;

-- evolui habilidade do personagem

begin;

select evoluir_habilidade(1);

commit;


-- Transaction de negociar itens

begin;

insert into npc_negocia_item(id_npc, id_item) VALUES (1, 9);

savepoint negociar_itens;

update personagem set gold = gold - i.preco
from item i
where i.id = 9;

savepoint descontar_gold;

update mochila set capacidade = capacidade-1; 

savepoint nova_capacidade;

insert into mochila_guarda(mochila, item)
values (1, 9); 
return new;

commit;