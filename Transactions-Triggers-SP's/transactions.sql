-- Transaction de compra de item

begin;

insert into instancia_item (id_item) values (1);

savepoint adiciona_instancia;

update personagem set gold = gold - i.preco
from item i
where i.id = 1;

savepoint desconta_gold;

insert into mochila(id_personagem, capacidade,item)
values (1, 
		(select m.capacidade-1 from mochila m order by m.capacidade asc limit 1),
		(select ii.id from instancia_item ii order by ii.id desc limit 1 ));


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
