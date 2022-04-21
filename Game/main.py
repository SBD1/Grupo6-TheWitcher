from optparse import OptionConflictError
from click import option
from conn import criaConexao
import sys
import os

conn = criaConexao()

cur = conn.cursor()

Jogar = "                 .: Jogar :.                  "
Ajuda = "                 .: Ajuda :.                  "
Sair =  "                 .: Sair :.                  "

def title_screen_options():
	#Allows the player to select the menu options, case-insensitive.
	option = input("> ")
	if option.lower() == ("jogar"):
		setup_game()
	elif option.lower() == ("sair"):
		sys.exit()
	elif option.lower() == ("ajuda"):
		help_menu()		
	while option.lower() not in ['jogar', 'sair', 'ajuda']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("jogar"):
			setup_game()
		elif option.lower() == ("sair"):
			sys.exit()
		elif option.lower() == ("ajuda"):
			help_menu()

def title_screen():
	#Clears the terminal of prior code for a properly formatted title screen.
	os.system('clear')
	#Prints the pretty title.
	print('#' * 45)
	print('#   Bem-vindo ao The Witcher   #')
	print('#     Um divertido Game MUD    #')
	print("#     Projeto SBD1 - 2021.2    #")
	print('#' * 45)
	print(Jogar)
	print(Ajuda)
	print(Sair)
	title_screen_options()

def help_menu():
	print("")
	print('#' * 45)
	print("~" * 45)
	print("- Ao seguir no jogo, você receberá opções do que pode ser feito.")
	print("- A partir dessas opções, escreva o que deseja fazer.\n")
	print("- Digite sempre em letras minúsculas.\n")
	print('#' * 45)
	print("\n")
	print('#' * 45)
	print("    Selecione uma opção para continuar.     ")
	print('#' * 45)
	print(Jogar)
	print(Ajuda)
	print(Sair)
	title_screen_options()

def general_options_menu():
	print('#' * 45)
	print("  Menu Geral  ")
	print('#' * 45)
	print(" .: Personagem :. ")
	print(" .: Listar Contratos Ativos :. ")
	print(" .: Ir para Kaer Morhen :. ")
	print(" .: Ir para Crows Perch :. ")
	print(" .: Ir para Ard Skellig :. ")
	print(" .: Ir para Pomar Branco :. ")
	print(" .: Ajuda :. ")
	print(" .: Sair :. ")
	general_options()

def general_options():
	option = input("> ")
	if option.lower() == ("personagem"):
		get_personagem()
	elif option.lower() == ("listar contratos ativos"):
		listar_contratos_ativos()
	elif option.lower() == ("ir para kaer morhen"):
		listar_areas_kaer_morhen()
	elif option.lower() == ("ir para crows perch"):
		listar_areas_crows_perch()
	elif option.lower() == ("ir para ard skellig"):
		listar_areas_ard_skellig()
	elif option.lower() == ("ir para pomar branco"):
		listar_areas_pomar_branco()
	elif option.lower() == ("sair"):
		sys.exit()
	elif option.lower() == ("ajuda"):
		help_menu()

	while option.lower() not in ['personagem', 'listar contratos ativos', 'ir para kaer morhen', 'ir para crows perch', 'ir para ard skellig', 'ir para pomar branco','ajuda', 'sair']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("personagem"):
			setup_game()
		elif option.lower() == ("listar contratos ativos"):
			listar_contratos_ativos()
		elif option.lower() == ("ir para kaer morhen"):
			listar_areas_kaer_morhen()
		elif option.lower() == ("ir para crows perch"):
			listar_areas_crows_perch()
		elif option.lower() == ("ir para skellig"):
			listar_areas_ard_skellig()
		elif option.lower() == ("ir para pomar branco"):
			listar_areas_pomar_branco()	
		elif option.lower() == ("sair"):
			sys.exit()
		elif option.lower() == ("ajuda"):
			help_menu()

#Area de Kaer Morhen
def listar_areas_kaer_morhen():
	print("A fortaleza de Kaer Morhen possui algumas áreas interessantes como:\n")
	
	sql = "select descricao from area a where a.id_mapa = 1"
	cur.execute(sql)
	rows = cur.fetchall()

	for r in rows:
		print(r)

	general_options_menu()
	general_options()

def opcoes_kaer_morhen():
	option = input("> ")
	if option.lower() == ("conhecer kaer morhen"):
		listar_areas_kaer_morhen()
	elif option.lower() == ("menu geral"):
		general_options()
	while option.lower() not in ['conhecer kaer morhen', 'menu geral']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("conhecer kaer morhen"):
			listar_areas_kaer_morhen()
		elif option.lower() == ("menu geral"):
			general_options()

#Area de Crows Perch
def listar_areas_crows_perch():
	print("A fortaleza de Crows Perch possui algumas áreas interessantes como:\n")
	
	sql = "select descricao from area a where a.id_mapa = 2"
	cur.execute(sql)
	rows = cur.fetchall()

	for r in rows:
		print(r)

	general_options_menu()
	general_options()

def opcoes_crows_perch():
	option = input("> ")
	if option.lower() == ("conhecer crows perch"):
		listar_areas_crows_perch()
	elif option.lower() == ("menu geral"):
		general_options()
	while option.lower() not in ['conhecer crows perch', 'menu geral']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("conhecer crows perch"):
			listar_areas_crows_perch()
		elif option.lower() == ("menu geral"):
			general_options()

# Area de Ard Skellig
def listar_areas_ard_skellig():
	print("A Cidade de Ard Skellig possui algumas áreas interessantes como:\n")
	
	sql = "select descricao from area a where a.id_mapa = 3"
	cur.execute(sql)
	rows = cur.fetchall()

	for r in rows:
		print(r)

	# general_options_menu()
	# general_options()

	print(" .: entrar na serraria  :. ")
	print(" .: Menu Geral :. ")

	option = input("> ")
	if option.lower() == ("entrar na serraria"):
		entrar_na_serraria()
	elif option.lower() == ("menu geral"):
		general_options_menu()
		general_options()
	while option.lower() not in ['entrar na serraria', 'menu geral']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("entrar na serraria"):
			entrar_na_serraria()
		elif option.lower() == ("menu geral"):
			general_options_menu()
			general_options()


def entrar_na_serraria():
	print("Na frente de uma serraria abandonada você se depara com um civil ferido")
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
		matar_berseker()
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
	#inserir as asas do vampiro
	print("as asas de Katakan foram arrancadas brutalmente")


def listar_contratos_ativos():
	print("Esses são os contratos que estão ativos: \n")

	contratos_ativos = f"""
						select ca.id, m.titulo, m.descricao 
						from contrato ca 
						inner join missao m on m.id = ca.id
						where is_ativo = {True}
						"""
	cur.execute(contratos_ativos)
	rows = cur.fetchall()
	for r in rows:
		print(f"Número da missão: {r[0]}")
		print(f"Título da missão: {r[1]}")
		print(f"Descrição: {r[2]} \n")
	print("\n")
	print('#' * 45)
	general_options_menu()
	general_options()



def opcoes_ard_skellig():
	option = input("> ")
	if option.lower() == ("conhecer ard skellig"):
		listar_areas_ard_skellig()
	elif option.lower() == ("menu geral"):
		general_options_menu()
		general_options()
	while option.lower() not in ['conhecer kaer morhen', 'menu geral']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("conhecer kaer morhen"):
			listar_areas_kaer_morhen()
		elif option.lower() == ("menu geral"):
			general_options_menu()
			general_options()




# Area de Pomar Branco
def listar_areas_pomar_branco():
	print("Você se encontra em um pomar branco e vê que tem alguns lugares a serem explorados:\n")
	
	sql = "select descricao from area a where a.id_mapa = 3"

	cur.execute(sql)

	rows = cur.fetchall()

	for r in rows:
		print(r)

	print(" .: Entrar no cemitério  :. ")
	print(" .: Explorar Hovel  :. ")
	print(" .: Explorar Ruinas  :. ")
	print(" .: Menu Geral :. ")

	option = input("> ")
	if option.lower() == ("entrar no cemitério"):
		entrar_no_cemitério()
	elif option.lower() == ("explorar hovel"):
		explorar_hovel()
	elif option.lower() == ("menu geral"):
		general_options_menu()
		general_options()
	while option.lower() not in ['entrar no cemitério', 'explorar hovel','menu geral']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("entrar no cemitério"):
			entrar_no_cemitério()
		elif option.lower() == ("explorar hovel"):
			explorar_hovel()
		elif option.lower() == ("menu geral"):
			general_options_menu()
			general_options()


def explorar_hovel():
	print("Entrando nas cinzas da vila antes conhecida como Hovel, você encontra: ")

	sql = """select npc.nome as npc, m.nome as monstro, i.nome as item from encontrado_em ee 
			left join npc on npc.id = ee.id_npc
			left join instancia_monstro im on im.id = ee.id_instancia_monstro
			left join monstro m on m.id = im.id_monstro
			left join instancia_item ii on ii.id = ee.id_instancia_item
			left join item i on i.id = ii.id_item 	
			where ee.id_area = 8
			group by npc.nome, m.nome, i.nome 
	"""

	cur.execute(sql)

	rows = cur.fetchall()

	for r in rows:
		print(f"Npc: {r[0]}")		
		print(f"Monstro: {r[1]}")		
		print(f"Item: {r[2]} \n")

	print('#' * 45)

	print(" .: Pegar Itens :.")
	print(" .: Falar com Johnny :. ")
	print(" .: Sair de Hovel :. ")
	print(" .: Menu Geral :. ")
	option = input("> ")
	if option.lower() == ("pegar itens"):
		pegar_itens_hovel()
	elif option.lower() == ("falar com johnny"):
		falar_com_johnny()
	elif option.lower() == ("sair de hovel"):
		listar_areas_pomar_branco()
	elif option.lower() == ("menu geral"):
		general_options_menu()
		general_options()
	while option.lower() not in ['pegar itens', 'falar com johnny', 'sair de hovel', 'menu geral']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("pegar itens"):
			listar_areas_pomar_branco()
		elif option.lower() == ("falar com johnny"):
			falar_com_johnny()
		elif option.lower() == ("sair de hovel"):
			listar_areas_pomar_branco()
		elif option.lower() == ("menu geral"):
			general_options_menu()
			general_options() 
		

def pegar_itens_hovel():
	pass

def falar_com_johnny():
	pass

def opcoes_pomar_branco():
	option = input("> ")
	if option.lower() == ("conhecer pomar branco"):
		listar_areas_pomar_branco()
	elif option.lower() == ("menu geral"):
		general_options_menu()
		general_options()
	while option.lower() not in ['conhecer pomar branco', 'menu geral']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("conhecer pomar branco"):
			listar_areas_pomar_branco()
		elif option.lower() == ("menu geral"):
			general_options_menu()
			general_options()


def entrar_no_cemitério():
	print("Você dá de cara com uma pessoa pequena e, ao chegar mais perto, percebe que é um anão com uma cara fechada e um ar sombrio")
	print(" .: Falar com ele :.")
	print(" .: Voltar a pomar branco :.")
	option = input("> ")
	if option.lower() == ("falar com ele"):
		missoes_cemitério()
	elif option.lower() == ("voltar a pomar branco"):
		listar_areas_pomar_branco()
	elif option.lower() == ("menu geral"):
		general_options_menu()
		general_options()
	while option.lower() not in ['entrar no cemitério', 'menu geral']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("falar com ele"):
			missoes_cemitério()
		elif option.lower() == ("voltar a pomar branco"):
			listar_areas_pomar_branco()
		elif option.lower() == ("menu geral"):
			general_options_menu()
			general_options()


def missoes_cemitério():
	print("Olá Witcher, neste cemitério existe uma besta que está bagunçando os túmulos, traga a cabeça dela e lhe recompensarei de acordo.")
	print(" .: Pegar Contrato :.")
	print(" .: Deixar Contrato :.")
	option = input("> ")
	if option.lower() == ("pegar contrato"):
		contrato_besta_pomar_branco()
	elif option.lower() == ("deixar contrato"):
		print("Tudo bem, Witcher. Se mudar de ideia, estarei aqui!")
		general_options_menu()
		general_options()
	while option.lower() not in ['pegar contrato', 'deixar contrato']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("pegar contrato"):
			contrato_besta_pomar_branco()
		elif option.lower() == ("deixar contrato"):
			general_options_menu()
			general_options()

def contrato_besta_pomar_branco():
	contrato_ativo = f"update contrato set is_ativo = {True} where id = 3"
	cur.execute(contrato_ativo)
	conn.commit()
	print("O contrato foi adicionado à lista de contratos ativos!")
	print(" .: Explorar Cemitério :. ")
	option = input("> ")
	if option.lower() == ("explorar cemitério"):
		missao_besta_pomar_branco()
	elif option.lower() == ("voltar para pomar branco"):
		listar_areas_pomar_branco()
	while option.lower() not in ['explorar cemitério', 'voltar para pormar branco']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("explorar cemitério"):
			contrato_besta_pomar_branco()
		elif option.lower() == ("voltar para pomar branco"):
			listar_areas_pomar_branco()


def missao_besta_pomar_branco():
	print("Você está andando pelo cemitério quando, de repente, vê um Berseker cavando um túmulo embaixo de uma grande estátua de mármore")
	print(" .: Matar Besta :.")
	print(" .: Sair do Cemitério :. ")
	print(" .: Menu Geral :. ")
	option = input("> ")
	if option.lower() == ("matar besta"):
		print("Você mata a besta e arranca sua cabeça\n")
		matar_berseker()
	elif option.lower() == ("sair do cemitério"):
		print("Você sai do cemitério e retorna a pomar branco")
		listar_areas_pomar_branco()
	elif option.lower() == ("menu geral"):
		general_options_menu()
		general_options()
	while option.lower() not in ['matar besta', 'sair do cemitério', 'menu geral']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("matar besta"):
			matar_berseker()
			print("Você mata a besta, arranca sua cabeça e leva até o anão")
			print("Você pega sua recompensa e volta a pomar branco")
			listar_areas_pomar_branco()
		elif option.lower() == ("sair do cemitério"):
			print("Você sai do cemitério e retorna a pomar branco")
			listar_areas_pomar_branco()
		elif option.lower() == ("menu geral"):
			general_options_menu()
			general_options()


def matar_berseker():
	inserir_cabeca_na_mochila = """
	insert into mochila_guarda (mochila, item) 
	VALUES (1, (select ii.id from instancia_item ii 
				left join item i on i.id = ii.id_item where i.nome = 'Cabeça de Berseker' limit 1));	
	"""

	deletar_instancia_berseker = "delete from encontrado_em where id_instancia_monstro = 1"

	cur.execute(inserir_cabeca_na_mochila)
	print("Cabeça de Berseker obtida!\n")

	cur.execute(deletar_instancia_berseker)
	conn.commit()

	print(" .: Levar a cabeça do berseker até o anão :. ")
	option = input("> ")
	if option.lower() == ("levar a cabeça do berseker até o anão"):
		levar_cabeca()
	while option.lower() not in ['levar a cabeça do berseker até o anão']:
		option = input("> ")
		if option.lower() == ("levar a cabeça do berseker até o anão"):
			levar_cabeca()
			
def levar_cabeca():
	print("Você vai até o anão e entrega a cabeça do beseker à ele.\n")
	print('#' * 60)
	print("Obrigado, Witcher. Como prometido, tome aqui a sua recompensa!\n")

	coletar_recompensa = """
		update personagem set gold = personagem.gold + c.gold from contrato c where c.id =  1
	"""

	entregar_cabeca = """
		delete from mochila_guarda mg
		using instancia_item as ii,
		      item as i 
		where mg.item = ii.id 
		and ii.id_item = i.id
		and	i.nome = 'Cabeça de Berseker'
	"""

	desativar_contrato = """
		update contrato set is_ativo = False where id = 3
	"""

	cur.execute(coletar_recompensa)
	print("Você recebeu 50 de ouro do anão.\n")
	print('#' * 60)
	cur.execute(entregar_cabeca)
	cur.execute(desativar_contrato)



	conn.commit()

	print(" .: Voltar para Pomar Branco :. ")
	print(" .: Menu Geral :.")
	option = input("> ")
	if option.lower() == ("voltar para pomar branco"):
		listar_areas_pomar_branco()
	elif option.lower() == ("menu geral"):
		general_options_menu()
		general_options()
	while option.lower() not in ['voltar para pomar branco', 'menu geral']:
		option = input("> ")
		if option.lower() == ("voltar para pomar branco"):
			listar_areas_pomar_branco()
		elif option.lower() == ("menu geral"):
			general_options_menu()
			general_options()


def listar_contratos_ativos():
	print("Esses são os contratos que estão ativos: \n")

	contratos_ativos = f"""
						select ca.id, m.titulo, m.descricao 
						from contrato ca 
						inner join missao m on m.id = ca.id
						where is_ativo = {True}
						"""
	cur.execute(contratos_ativos)
	rows = cur.fetchall()
	for r in rows:
		print(f"Número da missão: {r[0]}")
		print(f"Título da missão: {r[1]}")
		print(f"Descrição: {r[2]} \n")
	print("\n")
	print('#' * 45)
	general_options_menu()
	general_options()


def get_personagem():
	sql = "select * from personagem"
	cur.execute(sql)
	rows = cur.fetchall()
	for r in rows:
		print(f"Nome: {r[1]}")
		print(f"Gold: {r[2]}")
		print(f"Vida: {r[3]}")
		print(f"Ataque: {r[4]}")
		print(f"Defesa: {r[5]}")
	print('#' * 45)
	general_options_menu()
	general_options()


def setup_game():
	os.system('clear')
	print("#################################")
	print("# Aqui começa a sua aventura... #")
	print("#################################\n")
	print("Você se encontra em Kaer Morhen, uma velha fortaleza onde os Witchers eram treinados...\n")
	print("Escolha uma das opções abaixo:")
	print(" .: Conhecer Kaer Morhen :. ")
	print(" .: Menu Geral :. ")
	option = input("> ")
	if option.lower() == ("conhecer kaer morhen"):
		opcoes_kaer_morhen()
	elif option.lower() == ("menu geral"):
		general_options_menu()
		general_options()
	while option.lower() not in ['conhecer kaer morhen', 'menu geral']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("conhecer kaer morhen"):
			listar_areas_kaer_morhen()
		elif option.lower() == ("menu geral"):
			general_options_menu()
			general_options()

title_screen()

cur.close()
conn.close()
