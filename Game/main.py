from conn import criaConexao
import sys
import os

conn = criaConexao()

cur = conn.cursor()


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
		print("Invalid command, please try again.")
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
	print('# Bem-vindo ao The Witcher #')
	print("#     Projeto SBD1 - 2021.2    #")
	print('#' * 45)
	print("                 .: Jogar :.                  ")
	print("                 .: Ajuda :.                  ")
	print("                 .: Sair :.                  ")
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
	print("                 .: Jogar :.                  ")
	print("                 .: Ajuda :.                  ")
	print("                 .: Sair :.                  ")
	title_screen_options()


def setup_game():
    os.system('clear')
    print("################################")
    print("# Aqui começa a sua aventura... #")
    print("################################\n")
    print("Você se encontra em Kaer Morhen, uma velha fortaleza onde os Witchers eram treinados...\n")

    


title_screen()

cur.close()
conn.close()