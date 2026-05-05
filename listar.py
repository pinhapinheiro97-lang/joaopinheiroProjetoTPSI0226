def listar_registo(bands, events, bookings):
    while True:
        print("1 - Listar bandas.")
        print("2 - Listar eventos.")
        print("3 - Listar agendamentos.")
        print("4 - Voltar atrás")

        choice = input("Escolha uma das opções: ")

        match choice:
            case "1":
                listar_bandas(bands)
            case "2":
                listar_eventos(events)
            case "3":
                listar_agendamentos(bookings)
            case "4":
                break
            case _:
                print("Insere uma das opções válidas.")


# Funções auxilares de mostrar os registos de maneira clean
def mostrar_banda(band):
    print(
        f"ID: {band['id']} | "
        f"Nome: {band['nome']} | "
        f"Membros: {band['numeros_membros']} | "
        f"Género: {band['genero']} | "
        f"Contacto: {band['contacto']} | "
        f"Email: {band['email']} | "
        f"Disponível: {band['disponivel']}"
    )


def mostrar_evento(event):
    print(
        f"ID: {event['id']} | "
        f"Nome do Evento: {event['nome_evento']} | "
        f"Local: {event['local']} | "
        f"Data: {event['data']} | "
        f"Cachet: {event['cachet']} | "
        f"Tipo de evento: {event['tipo_evento']} | "
        f"Estado: {event['estado_evento']}"
    )


def mostrar_agendamento(booking):
    print(
        f"ID: {booking['id']} | "
        f"ID da Banda: {booking['band_id']} | "
        f"ID do Evento: {booking['event_id']} | "
        f"Data Marcação: {booking['data_marcacao']} | "
        f"Estado confirmação: {booking['estado_confirmacao']} | "
        f"Observações: {booking['observacoes']}"
    )


def listar_bandas(bands: list, page_size=10):
    if len(bands) == 0:
        print("Não existem bandas registadas.")
        return

# dar 10 resultados à vez

    total_pages = (len(bands) + page_size - 1) // page_size
    page = 1

    while True:
        start = (page - 1) * page_size
        end = start + page_size
        page_items = bands[start:end]

        print(f"\n--- Página {page}/{total_pages} ---")
        for band in page_items:
            mostrar_banda(band)

        print("\n[n] próxima página | [p] página anterior | [s] sair")
        choice = input("Opção: ").lower()

        if choice == "n":
            if page < total_pages:
                page += 1
            else:
                print("Já estás na última página.")
        elif choice == "p":
            if page > 1:
                page -= 1
            else:
                print("Já estás na primeira página.")
        elif choice == "s":
            break
        else:
            print("Opção inválida.")




def listar_eventos(events:list, page_size=10):
    if len(events) == 0:
        print("Não existem eventos registados.")
        return
    
    total_pages = (len(events) + page_size - 1) // page_size
    page = 1

    while True:
        start = (page - 1) * page_size
        end = start + page_size
        page_items = events[start:end]

        print(f"\n--- Página {page}/{total_pages} ---")

        for event in page_items:
            mostrar_evento(event)
        
        print("\n[n] próxima página | [p] página anterior | [s] sair")
        choice = input("Opção: ").lower()

        if choice == "n":
            if page < total_pages:
                page += 1
            else:
                print("Já estás na última página.")
        elif choice == "p":
            if page > 1:
                page -= 1
            else:
                print("Já estás na primeira página.")
        elif choice == "s":
            break
        else:
            print("Opção inválida.")

def listar_agendamentos(bookings: list, page_size=10):
    if len(bookings) == 0:
        print("Não existem agendamentos registados.")
        return

    total_pages = (len(bookings) + page_size - 1) // page_size
    page = 1

    while True:
        start = (page - 1) * page_size
        end = start + page_size
        page_items = bookings[start:end]

        print(f"\n--- Página {page}/{total_pages} ---")

        for booking in page_items:
            mostrar_agendamento(booking)
            
        print("\n[n] próxima página | [p] página anterior | [s] sair")
        choice = input("Opção: ").lower()

        if choice == "n":
            if page < total_pages:
                page += 1
            else:
                print("Já estás na última página.")
        elif choice == "p":
            if page > 1:
                page -= 1
            else:
                print("Já estás na primeira página.")
        elif choice == "s":
            break
        else:
            print("Opção inválida.")
