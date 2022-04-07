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
		print("Comando Invalido, Tente Novamente.")
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
	print(" .: Ir para Kaer Morhen :. ")
	print(" .: Ir para Crows Perch :. ")
	print(" .: Ir para Ard Skellig :. ")
	print(" .: Ajuda :. ")
	print(" .: Sair :. ")
	general_options()

def general_options():
	option = input("> ")
	if option.lower() == ("personagem"):
		get_personagem()
	elif option.lower() == ("ir para kaer morhen"):
		listar_areas_kaer_morhen()
	elif option.lower() == ("ir para crows perch"):
		listar_areas_crows_perch()
	elif option.lower() == ("ir para ard skellig"):
		listar_areas_ard_skellig()
	elif option.lower() == ("sair"):
		sys.exit()
	elif option.lower() == ("ajuda"):
		help_menu()

	while option.lower() not in ['personagem', 'ir para Kaer Morhen', 'ir para Crows Perch', 'ir para Ard Skellig', 'ajuda', 'sair']:
		print("Comando Invalido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("personagem"):
			setup_game()
		elif option.lower() == ("ir para Kaer Morhen"):
			listar_areas_kaer_morhen()
		elif option.lower() == ("ir para Crows Perch"):
			listar_areas_crows_perch()	
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
		print("Comando Invalido, Tente Novamente.")
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
		print("Comando Invalido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("conhecer crows perch"):
			listar_areas_crows_perch()
		elif option.lower() == ("menu geral"):
			general_options()

# Area de Ard Skellig
def listar_areas_ard_skellig():
	print("A Cidade de Ard Skellig possui algumas áreas interessantes como:\n")
	
	sql = "select descricao from area a where a.id_mapa = 4"
	cur.execute(sql)
	rows = cur.fetchall()

	for r in rows:
		print(r)

	general_options_menu()
	general_options()

def opcoes_ard_skellig():
	option = input("> ")
	if option.lower() == ("conhecer ard skellig"):
		listar_areas_ard_skellig()
	elif option.lower() == ("menu geral"):
		general_options()
	while option.lower() not in ['conhecer ard skellig', 'menu geral']:
		print("Comando Invalido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("conhecer ard skellig"):
			listar_areas_ard_skellig()
		elif option.lower() == ("menu geral"):
			general_options()



def get_personagem():
	sql = "select * from personagem"
	cur.execute(sql)
	rows = cur.fetchall()
	for r in rows:
		print(r)

def setup_game():
	os.system('clear')
	print("################################")
	print("# Aqui começa a sua aventura... #")
	print("################################\n")
	print("Você se encontra em Kaer Morhen, uma velha fortaleza onde os Witchers eram treinados...\n")
	print("Escolha uma das opções abaixo:")
	print(" .: Conhecer Kaer Morhen :. ")
	opcoes_kaer_morhen()
	print(" .: Conhecer Crows Perch :. ")
	opcoes_crows_perch()
	print(" .: Conhecer Ard Skellig :. ")
	opcoes_ard_skellig()

title_screen()

cur.close()
conn.close()
