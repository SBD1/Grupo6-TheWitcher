from conn import criaConexao
import main 

conn = criaConexao()
cur = conn.cursor()

# Area de Pomar Branco
def listar_areas_pomar_branco():
	print("Você se encontra em um pomar branco e vê que tem alguns lugares a serem explorados:\n")

	sql = "select descricao from area a where a.id_mapa = 3"

	cur.execute(sql)

	rows = cur.fetchall()

	for r in rows:
		print(r)

	print(" .: Ir até a forja de Pomar Branco :. ")
	print(" .: Entrar no cemitério  :. ")
	print(" .: Explorar Hovel  :. ")
	print(" .: Explorar Ruínas  :. ")
	print(" .: Menu Geral :. ")

	option = input("> ")
	if option.lower() == ("ir até a forja de pomar branco"):
		entrar_na_forja()
	elif option.lower() == ("entrar no cemitério"):
		entrar_no_cemitério()
	elif option.lower() == ("explorar hovel"):
		explorar_hovel()
	elif option.lower() == ("explorar ruínas"):
		ir_ate_ruinas()
	elif option.lower() == ("menu geral"):
		main.general_options_menu()
		main.general_options()
	while option.lower() not in ['ir até a forja de pomar branco','entrar no cemitério', 'explorar hovel', 'explorar ruínas', 'menu geral']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("ir até a forja de pomar branco"):
			entrar_na_forja()
		elif option.lower() == ("entrar no cemitério"):
			entrar_no_cemitério()
		elif option.lower() == ("explorar hovel"):
			explorar_hovel()
		elif option.lower() == ("explorar ruínas"):
			ir_ate_ruinas()
		elif option.lower() == ("menu geral"):
			main.general_options_menu()
			main.general_options()

def entrar_na_forja():
	print("Na entrada da forja, você avista um homem batendo um tipo de aço da bigorna com o martelo.")
	print(" .: Falar com ele :. ")
	print(" .: Voltar para Pomar Branco :. ")
	print(" .: Menu geral :. ")
	while True:
		option = input("> ")

		if option.lower() not in ['falar com ele', 'voltar para pomar branco', 'menu geral']:
			print("Comando Inválido, Tente Novamente.")
			continue

		if option.lower() == ("falar com ele"):
			falar_com_bram()
			break
		if option.lower() == ("voltar para pomar branco"):
			listar_areas_pomar_branco()
			break
		elif option.lower() == ("menu geral"):
			main.general_options_menu()
			main.general_options()
			break

def falar_com_bram():
	print(" - Bem-Vindo, Witcher. O que deseja hoje?!")
	print(" .: Ver produtos :. ")
	print(" .: Comprar produtos :. ")
	print(" .: Aprimorar equipamentos :. ")
	print(" .: Sair :. ")
	while True:
		option = input("> ")

		if option.lower() not in ['ver produtos', 'comprar produtos', 'aprimorar equipamentos','sair']:
			print("Comando Inválido, Tente Novamente.")
			continue

		if option.lower() == ("ver produtos"):
			ver_produtos()
			break
		if option.lower() == ("comprar produtos"):
			comprar_produtos()
			break
		if option.lower() == ("aprimorar equipamentos"):
			aprimorar_equipamentos()
			break
		elif option.lower() == ("sair"):
			print("Volte sempre!")
			main.general_options_menu()
			main.general_options()
			break

def ver_produtos():
	sql = """
			select i.nome, i.preco from npc_negocia_item nni
			left join item i on i.id = nni.id_item
			where id_npc = 10;
	"""

	cur.execute(sql)

	rows = cur.fetchall()

	for r in rows:
		print(f"Item: {r[0]}")		
		print(f"Preço: {r[1]}\n")

	falar_com_bram()

def comprar_produtos():
	print("Ainda não foi implementado!")
	falar_com_bram()

def aprimorar_equipamentos():
	print(" .: Aprimoramento básico :: 20 de gold :. ")
	print(" .: Aprimoramento intermediário :: 35 de gold:. ")
	print(" .: Aprimoramento superior :: 50 de gold :. ")
	while True:
		option = input("> ")

		if option.lower() not in ['aprimoramento básico', 'aprimoramento intermediário', 'aprimoramento superior','sair']:
			print("Comando Inválido, Tente Novamente.")
			continue

		if option.lower() == ("aprimoramento básico"):
			aprimorar_basico()
			break
		if option.lower() == ("aprimoramento intermediário"):
			aprimorar_intermed()
			break
		if option.lower() == ("aprimoramento superior"):
			aprimorar_superior()
			break
		elif option.lower() == ("sair"):
			falar_com_bram()
			break
	falar_com_bram()

def aprimorar_basico():
	aprimorar = """
	update itens_equipados set ataque_item = ataque_item+5, defesa_item  = defesa_item+7, vida_item = vida_item+10 
	from item i 
	where itens_equipados.id_instancia_item = i.id; 
	"""

	descontar_gold = """
	update personagem set gold = gold - 20;	
	"""

	cur.execute(aprimorar)
	cur.execute(descontar_gold)

	conn.commit()
	
	print("Seus aquipamentos foram aprimorados!")
	print('#' * 60)

	falar_com_bram()

def aprimorar_intermed():
	aprimorar = """
	update itens_equipados set ataque_item = ataque_item+8, defesa_item  = defesa_item+13, vida_item = vida_item+15 
	from item i 
	where itens_equipados.id_instancia_item = i.id; 
	"""

	descontar_gold = """
	update personagem set gold = gold - 35;	
	"""

	cur.execute(aprimorar)
	cur.execute(descontar_gold)

	conn.commit()

	print("Seus aquipamentos foram aprimorados!")
	print('#' * 60)

	falar_com_bram()


def aprimorar_superior():
	aprimorar = """
	update itens_equipados set ataque_item = ataque_item+12, defesa_item  = defesa_item+16, vida_item = vida_item+20 
	from item i 
	where itens_equipados.id_instancia_item = i.id; 
	"""

	descontar_gold = """
	update personagem set gold = gold - 50;	
	"""

	cur.execute(aprimorar)
	cur.execute(descontar_gold)

	conn.commit()

	print("Seus aquipamentos foram aprimorados!")
	print('#' * 60)

	falar_com_bram()

def explorar_hovel():
	print("Entrando nas cinzas da vila antes conhecida como Hovel, você encontra: ")

	sql = """select npc.nome as npc, m.nome as monstro, i.nome as item from encontrado_em ee 
			left join npc on npc.id = ee.id_npc
			left join instancia_monstro im on im.id = ee.id_instancia_monstro
			left join monstro m on m.id = im.id_monstro
			left join instancia_item ii on ii.id = ee.id_instancia_item
			left join item i on i.id = ii.id_item 	
			where ee.id_area = 9
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
		main.general_options_menu()
		main.general_options()
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
			main.general_options_menu()
			main.general_options() 
		

def pegar_itens_hovel():
    # retirar os itens do local
    sql = """select item.id from encontrado_em 
		left join instancia_item on instancia_item.id = encontrado_em.id_instancia_item
		left join item on item.id = instancia_item.id_item 	
		where encontrado_em.id_area = 8 and encontrado_em.id_instancia_item is not null"""
    
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

    print("Os itens foram adicionados na mochila.")
    
    # deletar_instancia_item = """
	# 	delete from encontrado_em where encontrado_em.id_instancia_item is not null and encontrado_em.id_area = 8
	# """

    # cur.execute(deletar_instancia_item)
    # conn.commit()

    print(" .: Ver Mochila :. ")
    print(" .: Falar com Johnny :. ")
    print(" .: Sair de Hovel :. ")
    print(" .: Menu Geral :. ")
    option = input("> ")
    if option.lower() == ("ver mochila"):
        main.ver_mochila()
    elif option.lower() == ("falar com johnny"):
        falar_com_johnny()
    elif option.lower() == ("sair de hovel"):
        listar_areas_pomar_branco()
    elif option.lower() == ("menu geral"):
        main.general_options_menu()
        main.general_options()
    while option.lower() not in ['ver mochila','falar com johnny', 'sair de hovel', 'menu geral']:
        print("Comando Inválido, Tente Novamente.")
        option = input("> ")
        if option.lower() == ("ver mochila"):
            main.ver_mochila()
        elif option.lower() == ("falar com johnny"):
            falar_com_johnny()
        elif option.lower() == ("sair de hovel"):
            listar_areas_pomar_branco()
        elif option.lower() == ("menu geral"):
            main.general_options_menu()
            main.general_options() 

def falar_com_johnny():
    print("""Você chega perto de Johnny e vê que é uma criatura baixa, que parece uma criança, porém, têm uma pele azul e algumas cicatrizes no rosto.\n
    - Olá garoto, estou procurando uma moça de cabelo cinza. Viu alguém assim? 
    - Se vi. Lembro-me como se fosse ontem. Logo que despertei, fui evacuar - essa é a minha parte favorita do dia. Defecar ao nascer do sol é simplesmente maravilhoso...
    Quando, de repente, ouvi um barulho tão forte que não poderia ter vindo de mim. E a garota apareceu! Do nada.
    Uma jovem de cabelo acinzentado, como disseste. E ferida e ofegante, ainda por cima!
    Ela correu em direção às cabanas das crianças, nas ruínas. Rápida, como se as moiras estivessem atrás dela. EU gritei algumas coisas desagradáveis... Ela estragou a minha manhã.\n
    - Então ela foi até as ruínas...
    """)
    print('#' * 60)
    print(" .: Ir até as ruínas :. ")
    print(" .: Voltar para pomar branco:. ")
    print(" .: Menu Geral :. ")
    while True:
        option = input("> ")

        if option.lower() not in ['ir até as ruínas', 'voltar para pomar branco', 'menu geral']:
            print("Comando Inválido, Tente Novamente.")
            continue

        if option.lower() == ("ir até as ruínas"):
            ir_ate_ruinas()
            break
        if option.lower() == ("voltar para pomar branco"):
            listar_areas_pomar_branco()
            break
        elif option.lower() == ("menu geral"):
            main.general_options_menu()
            main.general_options()
            break


def ir_ate_ruinas():
    print("Você se encontra em um local que parecia ser uma pequena vila, que agora está em ruínas, mas nota que ainda existem algumas cabanas ocupadas...")
    print("Você vê algumas crianças brincando na entrada de uma floresta que têm por perto. Mas nota que uma senhora se aproxima.")
    print(" - O que quer aqui, forasteiro? Não quero ninguém perturbando as minhas crianças.")
    print(" - Não tenho a intenção de pertubar ninguém, senhora... Estou a procura de uma moça de cabelos cinza. Johnny me disse que ela estava vindo nesta direção.")
    print(" - Ela estava aqui sim, apareceu muito machucada, então eu deixei ela ficar um pouco e com a ajuda das minhas crianças, tratei seus ferimentos.")
    print("Mas a alguns dias, quando acordei para vê-la, ela já tinha ido embora, sem falar para onde ia. Acho que já estava melhor!")
    print(" - Entendo. Agradeço a informação!")

    print('#' * 60)
    print(" .: Voltar para pomar branco:. ")
    print(" .: Menu Geral :. ")
    while True:
        option = input("> ")

        if option.lower() not in ['voltar para pomar branco', 'menu geral']:
            print("Comando Inválido, Tente Novamente.")
            continue
        if option.lower() == ("voltar para pomar branco"):
            listar_areas_pomar_branco()
            break
        elif option.lower() == ("menu geral"):
            main.general_options_menu()
            main.general_options()
            break




def opcoes_pomar_branco():
	option = input("> ")
	if option.lower() == ("conhecer pomar branco"):
		listar_areas_pomar_branco()
	elif option.lower() == ("menu geral"):
		main.general_options_menu()
		main.general_options()
	while option.lower() not in ['conhecer pomar branco', 'menu geral']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("conhecer pomar branco"):
			listar_areas_pomar_branco()
		elif option.lower() == ("menu geral"):
			main.general_options_menu()
			main.general_options()


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
		main.general_options_menu()
		main.general_options()
	while option.lower() not in ['entrar no cemitério', 'menu geral']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("falar com ele"):
			missoes_cemitério()
		elif option.lower() == ("voltar a pomar branco"):
			listar_areas_pomar_branco()
		elif option.lower() == ("menu geral"):
			main.general_options_menu()
			main.general_options()


def missoes_cemitério():
	print("Olá Witcher, me chamo Brouver Hoog e sou coveiro aqui. Neste cemitério existe uma besta que está bagunçando os túmulos, traga a cabeça dela e lhe recompensarei de acordo.")
	print(" .: Pegar Contrato :.")
	print(" .: Deixar Contrato :.")
	option = input("> ")
	if option.lower() == ("pegar contrato"):
		contrato_besta_pomar_branco()
	elif option.lower() == ("deixar contrato"):
		print("Tudo bem, Witcher. Se mudar de ideia, estarei aqui!")
		main.general_options_menu()
		main.general_options()
	while option.lower() not in ['pegar contrato', 'deixar contrato']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("pegar contrato"):
			contrato_besta_pomar_branco()
		elif option.lower() == ("deixar contrato"):
			main.general_options_menu()
			main.general_options()

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
			missao_besta_pomar_branco()
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
		main.general_options_menu()
		main.general_options()
	while option.lower() not in ['matar besta', 'sair do cemitério', 'menu geral']:
		print("Comando Inválido, Tente Novamente.")
		option = input("> ")
		if option.lower() == ("matar besta"):
			matar_berseker()
			print("Você mata a besta, arranca sua cabeça e leva até Brouver")
			print("Você pega sua recompensa e volta a pomar branco")
			listar_areas_pomar_branco()
		elif option.lower() == ("sair do cemitério"):
			print("Você sai do cemitério e retorna a pomar branco")
			listar_areas_pomar_branco()
		elif option.lower() == ("menu geral"):
			main.general_options_menu()
			main.general_options()


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

    print(" .: Levar a cabeça do berseker até Brouver :. ")
    option = input("> ")
    if option.lower() == ("levar a cabeça do berseker até brouver"):
        levar_cabeca()
    while option.lower() not in ['levar a cabeça do berseker até brouver']:
        print("Comando Inválido, Tente Novamente.")
        option = input("> ")
        if option.lower() == ("levar a cabeça do berseker até brouver"):
            levar_cabeca()
			
def levar_cabeca():
	print("Você vai até Brouver e entrega a cabeça do beseker à ele.\n")
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
	print("Você recebeu 50 de ouro de Brouver.\n")
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
		main.general_options_menu()
		main.general_options()
	while option.lower() not in ['voltar para pomar branco', 'menu geral']:
		option = input("> ")
		if option.lower() == ("voltar para pomar branco"):
			listar_areas_pomar_branco()
		elif option.lower() == ("menu geral"):
			main.general_options_menu()
			main.general_options()