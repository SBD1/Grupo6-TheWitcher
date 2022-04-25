from optparse import OptionConflictError
from click import option
from conn import criaConexao
import crows_perch
import pomar_branco as pb
import ard_skellig as ask
import sys
import os
from create_tables import create_tables
from populate_tables import populate_tables

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
	print(" .: Ver Mochila :. ")
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
	elif option.lower() == ("ver mochila"):
		ver_mochila()
	elif option.lower() == ("listar contratos ativos"):
		listar_contratos_ativos()
	elif option.lower() == ("ir para kaer morhen"):
		listar_areas_kaer_morhen()
	elif option.lower() == ("ir para crows perch"):
		crows_perch.listar_areas_crows_perch()
	elif option.lower() == ("ir para ard skellig"):
		ask.listar_areas_ard_skellig()
	elif option.lower() == ("ir para pomar branco"):
		pb.listar_areas_pomar_branco()
	elif option.lower() == ("sair"):
		sys.exit()
	elif option.lower() == ("ajuda"):
		help_menu()

	while option.lower() not in ['personagem', 'ver mochila', 'listar contratos ativos', 'ir para kaer morhen', 'ir para crows perch', 'ir para ard skellig', 'ir para pomar branco','ajuda', 'sair']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("personagem"):
			setup_game()
		elif option.lower() == ("ver mochila"):
			ver_mochila()
		elif option.lower() == ("listar contratos ativos"):
			listar_contratos_ativos()
		elif option.lower() == ("ir para kaer morhen"):
			listar_areas_kaer_morhen()
		elif option.lower() == ("ir para crows perch"):
			crows_perch.listar_areas_crows_perch()
		elif option.lower() == ("ir para skellig"):
			ask.listar_areas_ard_skellig()
		elif option.lower() == ("ir para pomar branco"):
			pb.listar_areas_pomar_branco()	
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

def ver_mochila():
	ver_mochila = f"""select count(m.item) as Quantidade, i.nome  
						from mochila_guarda m
						left join instancia_item ii on m.item = ii.id
						left join item i on ii.id_item = i.id 
						group by i.nome"""
	mochila = cur.execute(ver_mochila)
	rows = cur.fetchall()
	if (mochila == None):
		print("Sua mochila está vazia")
	else:
		for r in rows:
			print(f"Quantidade: {r[0]}")
			print(f"Item: {r[1]}")
	general_options_menu()
	general_options()

def setup_game():
	#os.system('clear')
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

if __name__ == '__main__':
	create_tables()
	populate_tables()
	title_screen()

	cur.close()
	conn.close()
