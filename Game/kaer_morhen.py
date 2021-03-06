from conn import criaConexao
import main 

conn = criaConexao()
cur = conn.cursor()

# Area de Kaer Morhen
def listar_areas_kaer_morhen():
    print("A fortaleza de Kaer Morhen possui algumas áreas interessantes como:\n")

    sql = "select descricao from area a where a.id_mapa = 1"

    cur.execute(sql)

    rows = cur.fetchall()

    for r in rows:
        print(r)

    print(" .: Entrar em kaer morhen  :. ")
    print(" .: Menu Geral :. ")

    option = input("> ")
    if option.lower() == ("entrar em kaer morhen"):
        conhecer_kaer_morhen()
    elif option.lower() == ("menu geral"):
        main.general_options_menu()
        main.general_options()
    while option.lower() not in ['entrar em kaer morhen', 'menu geral']:
        print("Comando Inválido, Tente Novamente.")
        option = input("> ")
        if option.lower() == ("entrar em kaer morhen"):
            conhecer_kaer_morhen()
        elif option.lower() == ("menu geral"):
            main.general_options_menu()
            main.general_options()

def conhecer_kaer_morhen():

	sql = "select * from npc where npc.nome = 'Ciri';"

	cur.execute(sql)

	rows = cur.fetchall()

	for r in rows:
		print("Entrando na fortaleza Kaer Morhen, você encontra Ciri, uma Witcher treinando \n")
	print(" .: Falar com Ciri :.")
	print(" .: Menu Geral :. ")
	option = input("> ")
	if option.lower() == ("falar com ciri"):
		falar_com_ciri()
	elif option.lower() == ("menu geral"):
		main.general_options_menu()
		main.general_options()
	while option.lower() not in ['falar com ciri', 'menu geral']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("falar com ciri"):
			falar_com_ciri()
		elif option.lower() == ("menu geral"):
			main.general_options_menu()
			main.general_options() 
		
def falar_com_ciri():
    print("""Você se aproxima de Ciri enquanto a observa treinar. \n
    - Está atrasado. Vasemir disse que um witcher viria treinar comigo. só não imaginei que demoraria tanto. Se veio até Kaer Morhen veio para treinar ou descansar...
    O que faz parado ai ainda? Venha treinar combate comigo. Para isso, pegue essa Espada Iris emprestada.
    """)

    print('#' * 60)
    print(" .: Pegar espada :. ")
    print(" .: Menu Geral :. ")
    while True:
        option = input("> ")

        if option.lower() not in ['pegar espada', 'menu geral']:
            print("Comando Inválido, Tente Novamente.")
            continue
        if option.lower() == ("pegar espada"):
            pegar_espada()
            break    
        elif option.lower() == ("menu geral"):
            main.general_options_menu()
            main.general_options()
            break

def treinar_combate():
    print("Você se posiciona em frente a Ciri e se prepara para o combate contra a witcher de cabelos brancos")
    print("Você prepara sua espada")
    
    print('#' * 60)
    print(" .: Fazer um ataque rápido :. ")
    print(" .: Fazer um ataque forte :. ")
    print(" .: Ativar instinto de sobrevivência :. ")
    print(" .: Terminar combate :. ")
    print(" .: Menu Geral :. ")
    while True:
        option = input("> ")

        if option.lower() not in ['fazer um ataque rápido', 'fazer um ataque forte', 'ativar instinto de sobrevivência', 'terminar combate', 'menu geral']:
            print("Comando Inválido, Tente Novamente.")
            continue
        if option.lower() == ("fazer um ataque rápido"):
            golpear()
            break
        if option.lower() == ("fazer um ataque forte"):
            golpear()
            break
        if option.lower() == ("ativar instinto de sobrevivência"):
            golpear()
            break
        if option.lower() == ("terminar combate"):
            terminar_combate()
            break
        elif option.lower() == ("menu geral"):
            main.general_options_menu()
            main.general_options()
            break

def pegar_espada():
    inserir_itens_na_mochila = """
	insert into mochila_guarda (mochila, item) 
	VALUES (1, (select ii.id from instancia_item ii 
				left join item i on i.id = ii.id_item where i.nome = 'Espada Iris' limit 1));	
	"""

    cur.execute(inserir_itens_na_mochila)
    conn.commit()


    print("A espada foi adicionada na mochila.")
    
    deletar_instancia_item = """
	 	delete from encontrado_em where encontrado_em.id_instancia_item is not null and encontrado_em.id_npc = 8
	"""

    cur.execute(deletar_instancia_item)
    conn.commit()

    print(" .: Treinar Combate :. ")
    print(" .: Menu Geral :. ")
    option = input("> ")
    if option.lower() == ("treinar combate"):
        treinar_combate()
    elif option.lower() == ("menu geral"):
        main.general_options_menu()
        main.general_options()
    while option.lower() not in ['ver mochila', 'treinar combate', 'menu geral']:
        print("Comando Inválido, Tente Novamente.")
        option = input("> ")
        if option.lower() == ("treinar combate"):
            treinar_combate()
        elif option.lower() == ("menu geral"):
            main.general_options_menu()
            main.general_options()

def golpear():
    
    print("Você realizou um golpe com sucesso")
    print("Ciri te golpeou com sucesso")
    
    print('#' * 60)
    print(" .: Fazer um ataque rápido :. ")
    print(" .: Fazer um ataque forte :. ")
    print(" .: Ativar instinto de sobrevivência :. ")
    print(" .: Terminar combate :. ")
    print(" .: Menu Geral :. ")
    while True:
        option = input("> ")

        if option.lower() not in ['fazer um ataque rápido', 'fazer um ataque forte', 'ativar instinto de sobrevivência', 'terminar combate', 'menu geral']:
            print("Comando Inválido, Tente Novamente.")
            continue
        if option.lower() == ("fazer um ataque rápido"):
            golpear()
            break
        if option.lower() == ("fazer um ataque forte"):
            golpear()
            break
        if option.lower() == ("ativar instinto de sobrevivência"):
            golpear()
            break
        if option.lower() == ("terminar combate"):
            terminar_combate()
            break
        elif option.lower() == ("menu geral"):
            main.general_options_menu()
            main.general_options()
            break

def terminar_combate():
    print("""Você e Ciri encerram o treino de combate \n
    - Isso foi divertido, até que você não é tão mal...
    - A espada que me deu me ajudou bastante.
    - É melhor pegar contratos para conseguir dinheiro para ter uma espada melhor, essa não vai ser suficiente. 
    Acho que Vasemir está em algumo lugar por aqui. Vá falar com ele, antes de deixar esse lugar para trás.
    """)

    print('#' * 60)
    print(" .: Explorar Forte :. ")
    print(" .: Explorar Torre :. ")
    print(" .: Menu Geral :. ")
    while True:
        option = input("> ")

        if option.lower() not in ['explorar forte', 'explorar torre', 'menu geral']:
            print("Comando Inválido, Tente Novamente.")
            continue
        if option.lower() == ("explorar forte"):
            explorar_forte()
            break
        if option.lower() == ("explorar torre"):
            explorar_torre()
            break      
        elif option.lower() == ("menu geral"):
            main.general_options_menu()
            main.general_options()
            break

def explorar_forte():
    print("Um forte abandonado que se tornou habitado por Witchers")
    print("Você ver alguns withchers bebendo e conversando alto")
    print("Alguns jogam cartas")
    print("Duas wicthers estão treinando conjuração de sinais")
    print("Mas não há sinais de Vesimir")

    print('#' * 60)
    print(" .: Comer pão :. ")
    print(" .: Sair do Forte :. ")
    print(" .: Menu Geral :. ")
    while True:
        option = input("> ")

        if option.lower() not in ['comer pão', 'sair do forte', 'menu geral']:
            print("Comando Inválido, Tente Novamente.")
            continue
        if option.lower() == ("comer pão"):
            consumir_item()
            break
        if option.lower() == ("sair do forte"):
            sair_do_local()
            break      
        elif option.lower() == ("menu geral"):
            main.general_options_menu()
            main.general_options()
            break

def consumir_item():	
    sql = "select * from item where item.nome = 'Pão';"

    cur.execute(sql)
    rows = cur.fetchall()

    print("O Witcher admira a animação dos outros witcher enquanto se alimenta e recupara suas energias depois do treinamento\n")
	
    print(" .: Sair do Forte :. ")
    print(" .: Menu Geral :. ")
    while True:
        option = input("> ")

        if option.lower() not in ['sair do forte', 'menu geral']:
            print("Comando Inválido, Tente Novamente.")
            continue
        if option.lower() == ("sair do forte"):
            sair_do_local()
            break      
        elif option.lower() == ("menu geral"):
            main.general_options_menu()
            main.general_options()
            break

def sair_do_local():
    print('#' * 60)
    print(" .: Explorar Forte :. ")
    print(" .: Explorar Torre :. ")
    print(" .: Menu Geral :. ")
    while True:
        option = input("> ")

        if option.lower() not in ['explorar forte', 'explorar torre', 'menu geral']:
            print("Comando Inválido, Tente Novamente.")
            continue
        if option.lower() == ("explorar forte"):
            explorar_forte()
            break
        if option.lower() == ("explorar torre"):
            explorar_torre()
            break      
        elif option.lower() == ("menu geral"):
            main.general_options_menu()
            main.general_options()
            break

def explorar_torre():
    print("A torre de pedra foi parcialmente durante a guerra")
    print("Hoje suas ruínas são usadas como local de descanso")
    print("É exatamente por isso que você encontra Vesimir cochilando em um canto escuro")

    print('#' * 60)
    print(" .: Falar com Vesimir :. ")
    print(" .: Sair da Torre :. ")
    print(" .: Menu Geral :. ")
    while True:
        option = input("> ")

        if option.lower() not in ['falar com vesimir', 'sair da torre', 'menu geral']:
            print("Comando Inválido, Tente Novamente.")
            continue
        if option.lower() == ("falar com vesimir"):
            falar_com_vesimir()
            break
        if option.lower() == ("sair da torre"):
            sair_do_local()
            break      
        elif option.lower() == ("menu geral"):
            main.general_options_menu()
            main.general_options()
            break

def falar_com_vesimir():
	print("Olá Witcher, tem um forktail maldito fazendo estrago na entrada de Kaer Morhen. Por favor, o mate para mim. Não precisa me trazer nada, só acabe com esse dragão")
	print(" .: Pegar Contrato :.")
	print(" .: Deixar Contrato :.")
	option = input("> ")
	if option.lower() == ("pegar contrato"):
		contrato_amardilha_forktail()
	elif option.lower() == ("deixar contrato"):
		print("Tudo bem, Witcher. Se mudar de ideia, estarei aqui!")
		main.general_options_menu()
		main.general_options()
	while option.lower() not in ['pegar contrato', 'deixar contrato']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("pegar contrato"):
			contrato_amardilha_forktail()
		elif option.lower() == ("deixar contrato"):
			main.general_options_menu()
			main.general_options()

def contrato_amardilha_forktail():
	contrato_ativo = f"update contrato set is_ativo = {True} where id = 9"
	cur.execute(contrato_ativo)
	conn.commit()
	print("O contrato foi adicionado à lista de contratos ativos!")
	print(" .: Explorar entrada :. ")
	option = input("> ")
	if option.lower() == ("explorar entrada"):
		missao_armadilha_forktail()
	elif option.lower() == ("voltar para kaer morhen"):
		sair_do_local()
	while option.lower() not in ['explorar entrada', 'voltar para kaer morhen ']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("explorar entrada"):
			missao_armadilha_forktail()
		elif option.lower() == ("voltar para kaer morhen"):
			sair_do_local()

def missao_armadilha_forktail():
	print("Você vai para a entrada de Kaer Morhen quando, de repente, encontra o Forktail que está causando problemas")
	print(" .: Matar Forktail :.")
	print(" .: Retornar a Kaer Morhen :. ")
	print(" .: Menu Geral :. ")
	option = input("> ")
	if option.lower() == ("matar forktail"):
		print("Você mata o forktail ao atravessar sua espada na garganta dele\n")
		matar_forktail()
	elif option.lower() == ("retornar a kaer morhen"):
		print("Você retorna a Kaer Korhen")
		sair_do_local()
	elif option.lower() == ("menu geral"):
		main.general_options_menu()
		main.general_options()
	while option.lower() not in ['matar forktail', 'retornar a kaer morhen', 'menu geral']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("matar forktail"):
			matar_forktail()
			sair_do_local()
		elif option.lower() == ("retornar a kaer morhen"):
			print("Você retorna a Kaer Korhen")
			sair_do_local()
		elif option.lower() == ("menu geral"):
			main.general_options_menu()
			main.general_options()

def matar_forktail():

    deletar_instancia_forktail = "delete from encontrado_em where id_instancia_monstro = 4"

    cur.execute(deletar_instancia_forktail)
    conn.commit()

    coletar_recompensa = """
		update personagem set gold = personagem.gold + c.gold from contrato c where c.id =  9
	"""

    cur.execute(coletar_recompensa)
    print("Você recebeu 50 de ouro de Vesimir.\n")
    print('#' * 60)

    desativar_contrato = """
		update contrato set is_ativo = False where id = 9
	"""

    cur.execute(desativar_contrato)

    print(" .: Ir para Kaer Morhen :. ")
    print(" .: Menu Geral :. ")
    while True:
        option = input("> ")

        if option.lower() not in ['ir para kaer morhen', 'menu geral']:
            print("Comando Inválido, Tente Novamente.")
            continue
        if option.lower() == ("ir para kaer morhen"):
            sair_do_local()
            break      
        elif option.lower() == ("menu geral"):
            main.general_options_menu()
            main.general_options()
            break 