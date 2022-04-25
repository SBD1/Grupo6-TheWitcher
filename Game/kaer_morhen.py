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

    print(" .: Conhecer kaer morhen  :. ")
    print(" .: Menu Geral :. ")

    option = input("> ")
    if option.lower() == ("conhecer kaer morhen"):
        conhecer_kaer_morhen()
    elif option.lower() == ("menu geral"):
        main.general_options_menu()
        main.general_options()
    while option.lower() not in ['conhecer kaer morhen', 'menu geral']:
        print("Comando Inválido, Tente Novamente.")
        option = input("> ")
        if option.lower() == ("conhecer kaer morhen"):
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
            evoluir_pontos_habilidade(1)
            break
        if option.lower() == ("fazer um ataque forte"):
            evoluir_pontos_habilidade(2)
            break
        if option.lower() == ("ativar instinto de sobrevivência"):
            evoluir_pontos_habilidade(2)
            break
        if option.lower() == ("ativar instinto de sobrevivência"):
            terminar_combate(2)
            break
        elif option.lower() == ("menu geral"):
            main.general_options_menu()
            main.general_options()
            break

def pegar_espada():
    # retirar os itens do local
    sql = """select item.id from encontrado_em 
		left join instancia_item on instancia_item.id = encontrado_em.id_instancia_item
		left join item on item.id = instancia_item.id_item 	
		where encontrado_em.id_area = 1 and encontrado_em.id_instancia_item is not null"""
    
    cur.execute(sql)
    items = cur.fetchall()

    tmp = []
    for n in items:
        tmp.append(n[0])

    inserir_itens_na_mochila = f"""
		insert into mochila_guarda (mochila, item) 
		VALUES (1, unnest(array{tmp}));	
	"""

    cur.execute(inserir_itens_na_mochila)
    conn.commit()

    print("A espada foi adicionada na mochila.")
    
    deletar_instancia_item = """
	 	delete from encontrado_em where encontrado_em.id_instancia_item is not null and encontrado_em.id_area = 8
	"""

    cur.execute(deletar_instancia_item)
    conn.commit()

    print(" .: Ver Mochila :. ")
    print(" .: Treinar Combate :. ")
    print(" .: Menu Geral :. ")
    option = input("> ")
    if option.lower() == ("ver mochila"):
        main.ver_mochila()
    elif option.lower() == ("treinar combate"):
        treinar_combate()
    elif option.lower() == ("menu geral"):
        main.general_options_menu()
        main.general_options()
    while option.lower() not in ['ver mochila', 'treinar combate', 'menu geral']:
        print("Comando Inválido, Tente Novamente.")
        option = input("> ")
        if option.lower() == ("ver mochila"):
            main.ver_mochila()
        elif option.lower() == ("treinar combate"):
            treinar_combate()
        elif option.lower() == ("menu geral"):
            main.general_options_menu()
            main.general_options() 