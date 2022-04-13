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