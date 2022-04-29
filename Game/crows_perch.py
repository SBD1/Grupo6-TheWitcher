from conn import criaConexao
import main

conn = criaConexao()
cur = conn.cursor()

def listar_areas_crows_perch():
	print("A fortaleza de Crows Perch possui algumas áreas interessantes como:\n")
	
	sql = "select descricao from area a where a.id_mapa = 5 or a.id_mapa = 6"
	cur.execute(sql)
	rows = cur.fetchall()

	for r in rows:
		print(r)

	print("")
	print(" .: Subir a colina  :. ")
	print(" .: Entrar na cabine  :. ")
	print(" .: Menu Geral :. ")

	while True:
		option = input("> ")

		if option.lower() not in ['subir a colina', 'entrar na torre', 'menu geral', 'entrar na cabine']: 
			print("Comando Inválido, Tente Novamente.")
			continue
		
		if option.lower() == ("subir a colina"):
			ir_para_colina()
			break
		if option.lower() == ("entrar na cabine"):
			ir_para_cabine()
			break
		if option.lower() == ("entrar na torre"):
			entrar_na_serraria()
			break
		elif option.lower() == ("menu geral"):
			main.general_options_menu()
			main.general_options()
			break

def ir_para_colina():
	print("\n\nNa colina, você percebeu que:\n")
    # antes de mostrar o texto q existe itens, verificar se realmente existe

	# pega todos os itens
	sql = """select i.nome from encontrado_em ee
		left join instancia_item ii on ii.id = ee.id_instancia_item
		left join item i on i.id = ii.id_item 	
		where ee.id_area = 5 and i.nome is not null"""

	cur.execute(sql)

	items = cur.fetchall()

	sql = """select m.nome from encontrado_em ee 
		left join instancia_monstro im on im.id = ee.id_instancia_monstro
		left join monstro m on m.id = im.id_monstro	
		where ee.id_area = 5 and m.nome is not null"""

	cur.execute(sql)

	monstros = cur.fetchall()

	print('1 - Keira está na sua frente te esperando')
	if items: print("2 - Existe alguns itens na área:")

	i = 0
	for n in items:
		print(f'- {n[0]}')
		i += 1

	print('')
	print('#' * 45)



	if items: print(" .: Pegar Itens :.")
	print(" .: Falar com Keira :. ")
	print(" .: Ir para torre :. ")
	print(" .: Descer a colina :. ")
	print(" .: Menu Geral :. ")
	while True:
		option = input("> ")

		if option.lower() not in ['pegar itens', 'falar com keira', 'descer a colina', 'ir para torre', 'menu geral']: 
			print("Comando Inválido, Tente Novamente.")
			continue
		
		if items and option.lower() == ("pegar itens"):
			pegar_itens(5)
			ir_para_colina()
			break
		if option.lower() == ("falar com keira"):
			falar_com_keira()
			break
		if option.lower() == ("descer a colina"):
			listar_areas_crows_perch()
			break
		if option.lower() == ("ir para torre"):
			ir_para_torre_lobisomem()
			break
		elif option.lower() == ("menu geral"):
			main.general_options_menu()
			main.general_options()
			break

def ir_para_cabine():
	print("\n\nNa cabine, você percebeu que:\n")

	sql = """select i.nome from encontrado_em ee
		left join instancia_item ii on ii.id = ee.id_instancia_item
		left join item i on i.id = ii.id_item 	
		where ee.id_area = 6 and i.nome is not null"""

	cur.execute(sql)

	items = cur.fetchall()

	if items: 
		print("1 - Existe alguns itens na área:")

		i = 0
		for n in items:
			print(f'- {n[0]}')
			i += 1

	print('')
	print('#' * 45)



	if items: print(" .: Pegar Itens :.")
	print(" .: Sair da cabine :. ")
	print(" .: Menu Geral :. ")
	while True:
		option = input("> ")

		if option.lower() not in ['pegar itens', 'sair da cabine', 'menu geral']: 
			print("Comando Inválido, Tente Novamente.")
			continue
		
		if items and option.lower() == ("pegar itens"):
			pegar_itens(6)
			ir_para_cabine()
			break
		if option.lower() == ("sair da cabine"):
			listar_areas_crows_perch()
			break
		elif option.lower() == ("menu geral"):
			main.general_options_menu()
			main.general_options()
			break

def pegar_itens(id_area):
	# retirar os itens do local
	sql = f"""select instancia_item.id from encontrado_em 
		left join instancia_item on instancia_item.id = encontrado_em.id_instancia_item
		left join item on item.id = instancia_item.id_item 	
		where encontrado_em.id_area = {id_area} and encontrado_em.id_instancia_item is not null"""

	cur.execute(sql)
	items = cur.fetchall()
	
	tmp = []
	for n in items:
		tmp.append(n[0])

	deletar_instancia_item = f"""
		delete from encontrado_em where encontrado_em.id_instancia_item is not null and encontrado_em.id_area = {id_area}
	"""

	cur.execute(deletar_instancia_item)
	conn.commit()
	
	inserir_itens_na_mochila = f"""
		insert into mochila_guarda (mochila, item) 
		VALUES (1, unnest(array{tmp}));	
	"""

	cur.execute(inserir_itens_na_mochila)
	conn.commit()

	print("Os itens foram adicionados na mochila.")

def falar_com_keira():
	sql = f"select * from contrato where missao = 8 and is_ativo = {True}"
	cur.execute(sql)
	contrato_ativo = cur.fetchall()

	if contrato_ativo:
		sql = f"""
			select *
			from item
			inner join instancia_item ii on ii.id_item = item.id
			inner join mochila_guarda on mochila_guarda.item = ii.id
			inner join missao on missao.item = item.id
			where item.nome = 'Cabeça de Nithral';
		"""

		cur.execute(sql)
		item = cur.fetchall()

		print("\n\nOlá Witcher, você trouxe a cabeça do monstro?")
		if item: 
			print(" .: Sim, entregar cabeca. :.")
			finalizar_contrato(8)
			ir_para_colina()
		else:
			print(" .: Ainda nao :.")
			option = input("> ")
			ir_para_colina()

		return

	sql = f"select * from contrato where missao = 8 and is_ativo = {False}"
	cur.execute(sql)
	contrato_nao_ativo = cur.fetchall()

	if not contrato_nao_ativo: 
		print('O guerreiro foi derrotado, obrigada witcher.')
		ir_para_colina()
		return

	print("Olá Witcher, na torre foi invadida por um guerreido da wild hunt, traga a cabeça dele e lhe recompensarei de acordo.")
	print(" .: Pegar Contrato :.")
	print(" .: Deixar Contrato :.")

	option = input("> ")
	
	if option.lower() == ("pegar contrato"):
		pegar_contrato()
	elif option.lower() == ("deixar contrato"):
		print("Tudo bem, Witcher. Se mudar de ideia, estarei aqui!")
	else:
		print("Comando inválido.")

	ir_para_colina()


def pegar_contrato():
	contrato_ativo = f"update contrato set is_ativo = {True} where id = 8"
	cur.execute(contrato_ativo)
	conn.commit()

	print("O contrato foi adicionado à sua lista de contratos ativos!")

def finalizar_contrato(id_contrato):
	sql = f"select gold from contrato where is_ativo = {True} and id = 8"
	cur.execute(sql)
	gold = cur.fetchall()[0]

	delete_contrato = f"delete from contrato where is_ativo = {True} and id = 8"
	cur.execute(delete_contrato)
	conn.commit()

	add_gold(gold[0])
	print("Missão concluida com sucesso, parabens witcher!")
	print(f"Você recebeu {gold[0]} golds")

def add_gold(gold):
	inserir_gold_personagem = f"""
	update personagem 
	set gold = {gold}
	where personagem.id = 1	
	"""

	cur.execute(inserir_gold_personagem)
	conn.commit()

def ir_para_torre_lobisomem():
	sql = "select from encontrado_em where id_instancia_monstro = 2"
	cur.execute(sql)
	lobisomem = cur.fetchall()
	if not lobisomem: 
		ir_para_torre()
		return

	print("Você está indo em direção a torre, quando surge no caminho um lobisomem\n\n")
	
	print(" .: Atacar o lobisomem :.")
	print(" .: Fugir :. ")
	print(" .: Menu Geral :. ")
	while True:
		option = input("> ")

		if option.lower() not in ['atacar o lobisomem', 'fugir', 'menu geral']: 
			print("Comando Inválido, Tente Novamente.")
			continue
		
		if option.lower() == ("atacar o lobisomem"):
			atacar_lobo()

			print("Agora, você continuou seguindo o caminho e conseguiu chegar na torre\n\n")
			ir_para_torre()
			break
		if option.lower() == ("fugir"):
			ir_para_colina()
			break
		elif option.lower() == ("menu geral"):
			main.general_options_menu()
			main.general_options()
			break

def atacar_lobo():
	inserir_cabeca_na_mochila = """
	insert into mochila_guarda (mochila, item) 
	VALUES (1, (select ii.id from instancia_item ii 
				left join item i on i.id = ii.id_item where i.nome = 'Carne' limit 1));	
	"""

	deletar_instancia_lobisomem = "delete from encontrado_em where id_instancia_monstro = 2"

	cur.execute(inserir_cabeca_na_mochila)
	conn.commit()

	print("Carne obtida!\n")

	cur.execute(deletar_instancia_lobisomem)
	conn.commit()


def ir_para_torre():
	sql = "select from encontrado_em where id_instancia_monstro = 3"
	cur.execute(sql)
	nithral = cur.fetchall()
	if not nithral: 
		print("A torre está vazia e você decida retornar para a colina.")
		ir_para_colina()
		return

	if not nithral: 
		print("Você entra na torre na qual Nithral foi derrotado e decide voltar para a colina\n\n")
		ir_para_colina()

	print("Você entra na torre e percebe que existe um guerreiro com armadura escura (Nithral) indo em sua direção te atacar")

	print(" .: Atacar o Nithral :.")
	print(" .: Fugir :. ")
	print(" .: Menu Geral :. ")
	while True:
		option = input("> ")

		if option.lower() not in ['atacar o nithral', 'fugir', 'menu geral']: 
			print("Comando Inválido, Tente Novamente.")
			continue
		
		if option.lower() == ("atacar o nithral"):
			atacar_nithral()

			print("Agora que Nithral foi derrotado você decide voltar para colina")
			ir_para_colina()
			break
		if option.lower() == ("fugir"):
			ir_para_colina()
			break
		elif option.lower() == ("menu geral"):
			main.general_options_menu()
			main.general_options()
			break


def atacar_nithral():
	inserir_cabeca_na_mochila = """
	insert into mochila_guarda (mochila, item) 
	VALUES (1, (select ii.id from instancia_item ii 
				left join item i on i.id = ii.id_item where i.nome = 'Cabeça de Nithral' limit 1));	
	"""

	deletar_instancia_nithral = "delete from encontrado_em where id_instancia_monstro = 3"

	cur.execute(inserir_cabeca_na_mochila)
	conn.commit()

	cur.execute(deletar_instancia_nithral)
	conn.commit()

	print("Cabeça de Nithral obtida!\n")
