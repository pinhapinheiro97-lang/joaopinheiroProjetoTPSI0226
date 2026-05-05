from listar import mostrar_banda, mostrar_evento, mostrar_agendamento


def pesquisar_por_campo(lista, campo, valor):
    for item in lista:
        if campo == "id" or campo == "band_id" or campo == "event_id":
            if item.get(campo) == valor:
                return item
        else:
            if str(item.get(campo, "")).lower() == str(valor).lower():
                return item
    return None


def ler_id(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("O ID tem de ser um número.")


def menu_pesquisa(bands, events, bookings):
    while True:
        print("\n--- PESQUISA ---")
        print("1 - Pesquisar bandas")
        print("2 - Pesquisar eventos")
        print("3 - Pesquisar agendamentos")
        print("4 - Voltar")

        choice = input("Escolha uma opção: ")

        match choice:
            case "1":
                menu_pesquisa_bandas(bands)
            case "2":
                menu_pesquisa_eventos(events)
            case "3":
                menu_pesquisa_agendamentos(bookings)
            case "4":
                break
            case _:
                print("Opção inválida.")


def menu_pesquisa_bandas(bands):
    while True:
        print("\n--- PESQUISAR BANDAS ---")
        print("1 - Por ID")
        print("2 - Por Nome")
        print("3 - Por Género")
        print("4 - Por Email")
        print("5 - Voltar")

        choice = input("Escolha uma opção: ")

        match choice:
            case "1":
                valor = ler_id("ID: ")
                resultado = pesquisar_por_campo(bands, "id", valor)
            case "2":
                valor = input("Nome: ")
                resultado = pesquisar_por_campo(bands, "nome", valor)
            case "3":
                valor = input("Género: ")
                resultado = pesquisar_por_campo(bands, "genero", valor)
            case "4":
                valor = input("Email: ")
                resultado = pesquisar_por_campo(bands, "email", valor)
            case "5":
                break
            case _:
                print("Opção inválida.")
                continue

        if choice != "5":
            if resultado:
                mostrar_banda(resultado)
            else:
                print("Registo não encontrado.")


def menu_pesquisa_eventos(events):
    while True:
        print("\n--- PESQUISAR EVENTOS ---")
        print("1 - Por ID")
        print("2 - Por Nome do Evento")
        print("3 - Por Local")
        print("4 - Voltar")

        choice = input("Escolha uma opção: ")

        match choice:
            case "1":
                valor = ler_id("ID: ")
                resultado = pesquisar_por_campo(events, "id", valor)
            case "2":
                valor = input("Nome do evento: ")
                resultado = pesquisar_por_campo(events, "nome_evento", valor)
            case "3":
                valor = input("Local: ")
                resultado = pesquisar_por_campo(events, "local", valor)
            case "4":
                break
            case _:
                print("Opção inválida.")
                continue

        if choice != "4":
            if resultado:
                mostrar_evento(resultado)
            else:
                print("Registo não encontrado.")


def menu_pesquisa_agendamentos(bookings):
    while True:
        print("\n--- PESQUISAR AGENDAMENTOS ---")
        print("1 - Por ID")
        print("2 - Por ID da Banda")
        print("3 - Por ID do Evento")
        print("4 - Por Data")
        print("5 - Voltar")

        choice = input("Escolha uma opção: ")

        match choice:
            case "1":
                valor = ler_id("ID: ")
                resultado = pesquisar_por_campo(bookings, "id", valor)
            case "2":
                valor = ler_id("ID da banda: ")
                resultado = pesquisar_por_campo(bookings, "band_id", valor)
            case "3":
                valor = ler_id("ID do evento: ")
                resultado = pesquisar_por_campo(bookings, "event_id", valor)
            case "4":
                valor = input("Data: ")
                resultado = pesquisar_por_campo(bookings, "data_marcacao", valor)
            case "5":
                break
            case _:
                print("Opção inválida.")
                continue

        if choice != "5":
            if resultado:
                mostrar_agendamento(resultado)
            else:
                print("Registo não encontrado.")
