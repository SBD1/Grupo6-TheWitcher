from conn import criaConexao
import main 

conn = criaConexao()
cur = conn.cursor()

#Area de Averum
def listar_areas_averum():
    print("Você está em Averum, tem alguns lugares a serem explorados:\n")

    sql = "select descricao from area a where a.id_mapa = 6"

    cur.execute(sql)

    rows = cur.fetchall()

    for r in rows:
        print(r)

    print("Explorar uma casa abondonada  :")
    print("Entrar em um seleiro   :")
    print("Menu Geral :")



    
    while True:
        option = input("> ")

        if option.lower() not in ['explorar uma casa abondonada', 'entrar em um seleiro', 'menu geral']:
            print ("Comando inválido, escolha outra opção!!")
            continue
        if option.lower() == ("explorar uma casa abondonada"):
            casa_abondonada()
            break
        if option.lower() == ("entrar em um seleiro"):
            seleiro()
            break
        elif option.lower() == ("menu geral"):
            main.general_options_menu()
            main.general_options()
            break



    #Casa abondonada
    def casa_abondonada():
        print("Você entrou em uma casa abondonada e encontra um rapaz com suprimentos")
        print("Pedir Suprimentos")
        print("Voltar para Averum")
        print("Menu Geral")

    while True:
        option = input("> ")

        if option.lower() not in ['pedir suprimentos', 'voltar para averum', 'menu geral']:
            print("Comando inválido, escolha outra opção!!")
            continue
        if option.lower() == ("pedir suprimentos"):
            pedir_suprimentos()
            break
        if option.lower() == ("voltar para averum"):
            listar_areas_averum()
            break
        elif option.lower() == ("menu geral"):
            main.general_options_menu()
            main.general_options()
            break





    def seleiro():
        print("Você entrou no seleiro e em cima da mesa acha um pergaminho, você tem a opção de escolher se quer fazer o contrato, ou não \n")
        print("Aceitar Contrato")
        print ("Rejeitar contrato")

        while True:
            option = input("> ")

            if option.lower() not in ['aceitar contrato', 'rejeitar contrato']:
                print("Comando inválido, escolha outra opção!!")
                continue
            if option.lower() == ("aceitar contrato"):
                contrato_aceito()
                break
            if option.lower() == ("rejeitar contrato"):
                listar_areas_averum()
                break
            elif option.lower() == ("menu geral"):
                main.general_options_menu()
                main.general_options()
                break






    def contrato_aceito():
        print("Você aceitou o contrato e terá que ir à uma caverna atrás de um tesouro escondido no fundo desta caverna")

        contrato_ativo = f"update contrato set is_ativo = {True} where id = 10"
        cur.execute(contrato_ativo)
        conn.commit()

        print("Entrar na Caverna")
        print("Voltar para Averum")
        print("Menu Geral")

        while True:
            option = input("> ")

            if option.lower() not in ['entrar na caverna', 'voltar para averum', 'menu geral']:
                print("Comando inválido, escolha outra opção!!")
                continue
            if option.lower() == ("entrar na caverna"):
                caverna()
                break
            if option.lower() == ("voltar para averum"):
                listar_areas_averum()
                break
            elif option.lower() == ("menu geral"):
                main.general_options_menu()
                main.general_options()
                break






    def caverna():
        print("Você agora tem um contrato ativo \n")
        print("Quando já está na caverna, você encontra um monstro.")
        print("Matar o monstro :")
        print("Sair da Caverna :")
        print("Menu Geral :")

        while True:

            option = input("> ")

            
            if option.lower() not in ['matar o monstro', 'sair da caverna', 'menu geral']:
                print("Comando inválido, escolha outra opção!!")
                continue
            if option.lower() == ("matar o monstro"):
                matar_monstro()
                break
            if option.lower() == ("sair da caverna"):
                listar_areas_averum()
                break
            elif option.lower() == ("menu geral"):
                main.general_options_menu()
                main.general_options()
                break





    def matar_monstro():
        print("a")

        recompensa_mochila = """
        insert into mochila_guarda (mochila, item) 
        VALUES (1, (select ii.id from instancia_item ii 
                    left join item i on i.id = ii.id_item where i.nome = 'Recompensa da Caverna' limit 1));	
        """

        recompensa = """
		update personagem set gold = personagem.gold + c.gold from contrato c where c.id =  2
	"""

        cur.execute(recompensa_mochila)
        cur.execute(recompensa)

        print("A recompensa foi adicionada a sua mochila")

        desativar_contrato = """
		update contrato set is_ativo = False where id = 2
	    """

        cur.execute(desativar_contrato)

        conn.commit()

        print("Voltar para Averum :")
        print("Menu Geral")

        while True:

            option = input("> ")

            if option.lower() not in ['voltar para averum', 'menugeral']:
                print("Comando inválido, escolha outra opção!!")
                continue
            if option.lower() == ("voltar para averum"):
                listar_areas_averum()
                break
            elif option.lower() == ("menu geral"):
                main.general_options_menu()
                main.general_options()
                break


        
    
    def pedir_suprimentos():

        print("Você entrou em uma casa abondonada e encontra um rapaz com suprimentos \n" )
        print("Este rapaz é Zakanon, um witcher que ficou na cidade. \n ")
        print("Ele tem alguns itens que podem te ajudar a sobreviver, pois no caminho você pode encontrar monstros!! \n")
        
        while True:
            print("Pegar os itens de Zakanon:")
            print("Sair da casa de Zakanon")
            print("Menu Geral")

            option = input("> ")

            if option.lower() not in ['pegar os itens de zakanon', 'sair da casa de zakanon', 'menu geral']:
                print("Comando inválido, escolha outra opção!!")
                continue
            if option.lower() == ("pegar os itens de zakanon"):
                itens_zakanon()
                break
            if option.lower() == ("sair da casa de zakanon"):
                listar_areas_averum()
                break
            elif option.lower() == ("menu geral"):
                main.general_options_menu()
                main.general_options()
                break

    def itens_zakanon():
        
        print("Pegar os itens de Zakanon:")

        sql = """
		select item.id from encontrado_em 
		left join instancia_item on instancia_item.id = encontrado_em.id_instancia_item
		left join item on item.id = instancia_item.id_item 	
		where encontrado_em.id_area = 6 and encontrado_em.id_instancia_item is not null
				"""

        cur.execute(sql)

        deletar_instancia_item = "delete from encontrado_em where encontrado_em.id_instancia_item is not null and encontrado_em.id_area = 6"

        cur.execute(deletar_instancia_item)
        conn.commit()
        
        inserir_item_na_mochila = f"""
            insert into mochila_guarda (mochila, item) 
            VALUES (1, (select ii.id from instancia_item ii 
                    left join item i on i.id = ii.id_item where i.nome = 'Espada do Himmeska' limit 1));	
        """

        cur.execute(inserir_item_na_mochila)
        conn.commit()

        print("O item foi adicionado na mochila.")

        print("Sair da casa de Zakanon :")
        print("Menu Geral :")
        
        while True:
            option = input("> ")

            if option.lower() == ("sair da casa de zakanon"):
                listar_areas_averum()
                break
            elif option.lower() == ("menu geral"):
                main.general_options_menu()
                main.general_options()
                break

