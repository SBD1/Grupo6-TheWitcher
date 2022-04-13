-- Listar missões ativas
select ca.id, m.titulo, m.descricao 
from contrato ca 
inner join missao m on m.id = ca.id
where is_ativo = True

-- Listar Itens Mochila
select count(m.item) as Quantidade, i.nome  
from mochila m
left join instancia_item ii on m.item = ii.id
left join item i on ii.id_item = i.id 
group by i.nome