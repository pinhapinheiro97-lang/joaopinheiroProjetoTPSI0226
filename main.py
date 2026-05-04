#Projeto Final Python - Sistema de Gestão de uma Agência Musical

    
from dados import carregar_dados, guardar_bandas, guardar_eventos, guardar_agendamentos, guardar_dados
from criar import criar_bandas, criar_evento, criar_agendamento


# Criar registos é um sub-menu que terá funções adicionais para cada tipo de lista 
def criar_registo(bands, events, bookings):
    while True:
        print("1 - Criar nova banda.")
        print("2 - Criar novo evento.")
        print("3 - Criar novo agendamento.")
        print("4 - Voltar atrás")

        choice = input("Escolha uma das opções.")

        match choice:
            case "1":
                criar_bandas(bands) 
                guardar_bandas(bands)                
            case "2":
                criar_evento(events)
                guardar_eventos(events)
            case "3":
                criar_agendamento(bookings, bands, events)
                guardar_agendamentos(bookings)
            case "4":
                break
            case _:
                print("Insere uma das opções válidas.")


#Menu esqueleto do mesmo
def menu(bands, events, bookings):
    while True:
        print("***Sistema de gestão da Agência***")
        print("1 - Criar novo registo.")
        print("2 - Listar registos")
        print("3 - Pesquisa avançada.")
        print("4 - Editar registo.")
        print("5 - Eliminar registos.")
        print("6 - Ordenar registos.")
        print("7 - Guardar e sair")
        choice = input("Insere uma das opções (1 - 7): ")

        match choice:
            case "1":
                criar_registo(bands, events, bookings)
            case "2":
                pass                 
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                guardar_dados(bands, events, bookings)
                print("Fim de programa...")
                break
            case _:
                print("Insere uma das opções válidas.")



#Iniciar menu

bands, events, bookings = carregar_dados()
menu(bands, events, bookings)