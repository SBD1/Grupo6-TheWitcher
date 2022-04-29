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

    print(" .: Explorar uma casa abondonada  :. ")
    print(" .: Entrar em um seleiro   :. ")
    print(" .: Menu Geral :. ")



    
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
        print("Você entrou em uma casa abondonada e encontra um rapaz com suprimentos")
    
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

        print(" .: Voltar para Ard Skellig :. ")
        print(" .: Menu Geral :.")
        
        while True:
            if option.lower() == ("sair da casa de zakanon"):
                listar_areas_averum()
                break
            elif option.lower() == ("menu geral"):
                main.general_options_menu()
                main.general_options()
                break

