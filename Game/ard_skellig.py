from conn import criaConexao
import main 

conn = criaConexao()
cur = conn.cursor()


# Area de Ard Skellig
def listar_areas_ard_skellig():
	print("A Cidade de Ard Skellig possui algumas áreas interessantes como:\n")
	
	sql = "select descricao from area a where a.id_mapa = 4"
	cur.execute(sql)
	rows = cur.fetchall()

	for r in rows:
		print(r)

	print(" .: Entrar na serraria  :. ")
	print(" .: Explorar torre antiga :. ")
	print(" .: Caminhar por de baixo da grande ponte :. ")
	print(" .: Menu Geral :. ")

	option = input("> ")
	if option.lower() == ("entrar na serraria"):
		entrar_na_serraria()
	elif option.lower() == ("explorar torre antiga"):
		explorar_torre_antiga()
	elif option.lower() == ("caminhar por de baixo da grande ponte"):
		caminha_grande_ponte()
	elif option.lower() == ("menu geral"):
		general_options_menu()
		general_options()
	while option.lower() not in ['entrar na serraria', 'explorar torre antiga', 'caminhar por de baixo da grande ponte', 'menu geral']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("entrar na serraria"):
			entrar_na_serraria()
		elif option.lower() == ("explorar torre antiga"):
			explorar_torre_antiga()
		elif option.lower() == ("caminhar por de baixo da grande ponte"):
			caminha_grande_ponte()
		elif option.lower() == ("menu geral"):
			general_options_menu()
			general_options()



def explorar_torre_antiga():

	sql = "select * from item where item.nome = 'Armadura Thyssen';"

	cur.execute(sql)
	rows = cur.fetchall()

	for r in rows:
		print("Entrando torre antiga abandonada a muitos anos, o witcher você se depara com", r[1], "\n")
	print(" .: Pegar Item :.")
	print(" .: Sair da Torre Antiga :. ")
	print(" .: Menu Geral :. ")
	option = input("> ")
	if option.lower() == ("pegar item"):
		pegar_item_torre_antiga()
	elif option.lower() == ("sair da torre antiga"):
		listar_areas_ard_skellig()
	elif option.lower() == ("menu geral"):
		general_options_menu()
		general_options()
	while option.lower() not in ['pegar item', 'sair da torre antiga', 'menu geral']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("pegar item"):
			pegar_item_torre_antiga()
		elif option.lower() == ("sair da torre antiga"):
			listar_areas_ard_skellig()
		elif option.lower() == ("menu geral"):
			general_options_menu()
			general_options() 

def pegar_item_torre_antiga():

	sql = """
		select item.id from encontrado_em 
		left join instancia_item on instancia_item.id = encontrado_em.id_instancia_item
		left join item on item.id = instancia_item.id_item 	
		where encontrado_em.id_area = 4 and encontrado_em.id_instancia_item is not null
				"""

	cur.execute(sql)
	items = cur.fetchall()

	deletar_instancia_item = "delete from encontrado_em where encontrado_em.id_instancia_item is not null and encontrado_em.id_area = 4"

	cur.execute(deletar_instancia_item)
	conn.commit()
	
	inserir_item_na_mochila = f"""
		insert into mochila_guarda (mochila, item) 
		VALUES (1, (select ii.id from instancia_item ii 
				left join item i on i.id = ii.id_item where i.nome = 'Armadura Thyssen' limit 1));	
	"""

	cur.execute(inserir_item_na_mochila)
	conn.commit()

	print("O item foi adicionado na mochila.")

	print(" .: Voltar para Ard Skellig :. ")
	print(" .: Menu Geral :.")
	option = input("> ")
	if option.lower() == ("voltar para ard skellig"):
		listar_areas_ard_skellig()
	elif option.lower() == ("menu geral"):
		general_options_menu()
		general_options()
	while option.lower() not in ['voltar para ard skellig', 'menu geral']:
		option = input("> ")
		if option.lower() == ("voltar para ard skellig"):
			listar_areas_ard_skellig()
		elif option.lower() == ("menu geral"):
			general_options_menu()
			general_options()



def caminha_grande_ponte():
	
	sql = "select * from item where item.nome = 'Cerveja';"

	cur.execute(sql)
	rows = cur.fetchall()

	for r in rows:
		print("O Witcher caminha na beira do pequeno rio e o admira, enquanto toma uma", r[1], "\n")
	print(" .: Voltar a ard skellig :.")
	option = input("> ")
	if option.lower() == ("voltar a ard skellig"):
		listar_areas_ard_skellig()
	elif option.lower() == ("menu geral"):
		general_options_menu()
		general_options()
	while option.lower() not in ['menu geral']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("voltar a ard skellig"):
			listar_areas_ard_skellig()
		elif option.lower() == ("menu geral"):
			general_options_menu()
			general_options()



def entrar_na_serraria():

	sql = "select * from npc where npc.nome = 'Hendrik';"

	cur.execute(sql)
	rows = cur.fetchall()

	for r in rows:
		print("Na frente de uma serraria abandonada você se depara com", r[1], "um civil ferido \n")
	print(" .: Falar com ele :.")
	print(" .: Voltar a ard skellig :.")
	option = input("> ")
	if option.lower() == ("falar com ele"):
		missoes_serraria()
	elif option.lower() == ("voltar a ard skellig"):
		listar_areas_ard_skellig()
	elif option.lower() == ("menu geral"):
		general_options_menu()
		general_options()
	while option.lower() not in ['entrar na serraria', 'menu geral']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("falar com ele"):
			missoes_serraria()
		elif option.lower() == ("voltar a ard skellig"):
			listar_areas_ard_skellig()
		elif option.lower() == ("menu geral"):
			general_options_menu()
			general_options()


def missoes_serraria():
	print("Olá Witcher, entrei nessa serraria para me proteger da chuva e fui atacado por um vampiro, traga as asas dele e lhe recompensarei de acordo.")
	print(" .: Pegar Contrato :.")
	print(" .: Deixar Contrato :.")
	option = input("> ")
	if option.lower() == ("pegar contrato"):
		contrato_serraria()
	elif option.lower() == ("deixar contrato"):
		print("Tudo bem, Witcher. Se mudar de ideia, estarei aqui!")
		general_options_menu()
		general_options()
	while option.lower() not in ['pegar contrato', 'deixar contrato']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("pegar contrato"):
			contrato_serraria()
		elif option.lower() == ("deixar contrato"):
			general_options_menu()
			general_options()


def contrato_serraria():
	contrato_ativo = f"update contrato set is_ativo = {True} where id = 2"
	cur.execute(contrato_ativo)
	conn.commit()
	print("O contrato foi adicionado à lista de contratos ativos!")
	print(" .: Explorar Serraria :. ")
	option = input("> ")
	if option.lower() == ("explorar serraria"):
		missao_serraria()
	elif option.lower() == ("voltar para ard skellig"):
		listar_areas_ard_skellig()
	while option.lower() not in ['explorar serraria', 'voltar para ard skellig']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("pegar contrato"):
			contrato_serraria()
		elif option.lower() == ("voltar para ard skellig"):
			listar_areas_ard_skellig()


def missao_serraria():
	print("Você entra na serraria abandonada, e ao fundo vê Katakan, um morcego monstruoso vasculhando alguns destroços")
	print(" .: Matar Katakan :.")
	print(" .: Sair do Serraria :. ")
	print(" .: Menu Geral :. ")
	option = input("> ")
	if option.lower() == ("matar katakan"):
		matar_katakan()
		print("Você mata o vampiro, arranca suas asas e leva até o civil")
		print("Você pega sua recompensa e volta a ard skellig")
		listar_areas_ard_skellig()
	elif option.lower() == ("sair da serraria"):
		print("Você sai da serraria e retorna a ard skellig")
		listar_areas_ard_skellig()
	elif option.lower() == ("menu geral"):
		general_options_menu()
		general_options()
	while option.lower() not in ['matar katakan', 'sair da serraria', 'menu geral']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("matar katakan"):
			matar_katakan()
			print("Você mata o vampiro, arranca suas asas e leva até o civil")
			print("Você pega sua recompensa e volta a ard skellig")
			listar_areas_ard_skellig()
		elif option.lower() == ("sair da serraria"):
			print("Você sai da serraria e retorna a ard skellig")
			listar_areas_ard_skellig()
		elif option.lower() == ("menu geral"):
			general_options_menu()
			general_options()


def matar_katakan():

	inserir_asas_na_mochila = """
	insert into mochila_guarda (mochila, item) 
	VALUES (1, (select ii.id from instancia_item ii 
				left join item i on i.id = ii.id_item where i.nome = 'Asas de Katakan' limit 1));	
	"""

	deletar_instancia_katakan = "delete from encontrado_em where id_instancia_monstro = 15"

	cur.execute(inserir_asas_na_mochila)

	print("As asas de Katakan foram arrancadas brutalmente\n")

	cur.execute(deletar_instancia_katakan)
	conn.commit()

	print(" .: Levar as asas de Katakan até o civil :. ")
	option = input("> ")
	if option.lower() == ("levar as asas de katakan até o civil"):
		levar_asas()
	while option.lower() not in ['levar as asas de katakan até o civil']:
		option = input("> ")
		if option.lower() == ("levar as asas de katakan até o civil"):
			levar_asas()


def levar_asas():
	print("Você vai até o civil e entrega as asas de katakan.\n")
	print('#' * 60)
	print("Obrigado, Witcher. Como prometido, tome aqui a sua recompensa!\n")

	coletar_recompensa = """
		update personagem set gold = personagem.gold + c.gold from contrato c where c.id =  2
	"""

	entregar_asas = """
		delete from mochila_guarda mg
		using instancia_item as ii,
		      item as i 
		where mg.item = ii.id 
		and ii.id_item = i.id
		and	i.nome = 'Asas de Katakan'
	"""

	desativar_contrato_katakan = """
		update contrato set is_ativo = False where id = 2
	"""

	cur.execute(coletar_recompensa)
	print("Você recebeu 55 de ouro do civil.\n")
	print('#' * 60)
	cur.execute(entregar_asas)
	cur.execute(desativar_contrato_katakan)

	conn.commit()

	print(" .: Voltar para Ard Skellig :. ")
	print(" .: Menu Geral :.")
	option = input("> ")
	if option.lower() == ("voltar para ard skellig"):
		listar_areas_ard_skellig()
	elif option.lower() == ("menu geral"):
		general_options_menu()
		general_options()
	while option.lower() not in ['voltar para ard skellig', 'menu geral']:
		option = input("> ")
		if option.lower() == ("voltar para ard skellig"):
			listar_areas_ard_skellig()
		elif option.lower() == ("menu geral"):
			general_options_menu()
			general_options()
