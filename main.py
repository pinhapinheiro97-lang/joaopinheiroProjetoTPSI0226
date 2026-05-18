#Projeto Final Python - Sistema de Gestão de uma Agência Musical

    
from dados import carregar_dados, guardar_dados
from criar import criar_registo
from listar import listar_registo
from pesquisar import menu_pesquisa
from eliminar import menu_eliminar
from editar import menu_editar
from ordenar import menu_ordenar
from estatistica import menu_estatistica





#Menu principal 
def menu(bands, events, bookings):
    while True:
        print("\n--- SISTEMA DE GESTÃO DA AGÊNCIA MUSICAL --- ")
        print("1 - Criar novo registo.")
        print("2 - Listar registos")
        print("3 - Pesquisa avançada.")
        print("4 - Editar registo.")
        print("5 - Eliminar registos.")
        print("6 - Ordenar registos.")
        print("7 - Estatisticas e processamento.")
        print("8 - Guardar e sair")
        choice = input("Insere uma das opções (1 - 8): ")

        match choice:
            case "1":
                criar_registo(bands, events, bookings)
            case "2":
                listar_registo(bands, events, bookings)                 
            case "3":
                menu_pesquisa(bands, events, bookings)
            case "4":
                menu_editar(bands, events, bookings)
            case "5":
                menu_eliminar(bands, events, bookings)
            case "6":
                menu_ordenar(bands, events, bookings)
            case "7":
                menu_estatistica(bands, events, bookings)
            case "8":
                guardar_dados(bands, events, bookings)
                print("Fim de programa...")
                break
            case _:
                print("Insere uma das opções válidas.")



#Menu com carregamento de dados
def main():
    bands, events, bookings = carregar_dados()
    menu(bands, events, bookings)

if __name__ == "__main__":
    main()