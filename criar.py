
from validadores import ler_email, ler_contacto, ler_float, ler_inteiro, ler_data
from dados import guardar_bandas, guardar_eventos, guardar_agendamentos

# Sub menu de criação de registos 
def criar_registo(bands, events, bookings):
    while True:
        print("1 - Criar nova banda.")
        print("2 - Criar novo evento.")
        print("3 - Criar novo agendamento.")
        print("4 - Voltar atrás")

        choice = input("Escolha uma das opções: ")

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
                
                

# criar banda
def criar_bandas(bands:list):
    nome_banda = input("Nome da banda: ").strip()
    numeros_membros = ler_inteiro("Número de membros: ")
    genero = input("Género musical: ").strip()    
    contacto = ler_contacto("Contacto telefónico: ")        
    email = ler_email("Email de contacto: ")
        
    while True:
        resposta_disponibilidade = input("Está disponível? (s/n): ").strip().lower()
        if resposta_disponibilidade == "s":
            disponivel = True
            break
        elif resposta_disponibilidade == "n":
            disponivel = False
            break
        else:
            print("Resposta inválida. Escreve (s) ou (n).")


    # evitar IDs repetidos quando se eliminam registos. Validar todos os ids e adicionar +1 ao ultimo
    ids_bandas = [band["id"] for band in bands]
    id_banda = max(ids_bandas, default=0) + 1

    band = {
        "id": id_banda,
        "nome": nome_banda,
        "numeros_membros": numeros_membros,
        "genero": genero,
        "contacto": contacto,
        "email": email,
        "disponivel": disponivel
    }

    bands.append(band)
    print("Banda criada com sucesso.")

# criar evento
def criar_evento(events:list):
    nome_evento=input("Nome do evento: ").strip()
    local=input("Local: ").strip()
    
    data=ler_data("Data do evento (YYYY-MM-DD): ")

    cachet = ler_float("Valor de cachet: ")    

    tipo_evento=input("Tipo de evento: ").strip()
    while True:
        estado_evento=input("Estado do evento (pago/não pago): ").strip().lower() # pago/não pago
        if estado_evento in ("pago", "não pago"):
            break
        print("Estado inválido. Escreve: pago ou não pago.")
        
    
    ids_eventos = [event["id"] for event in events]
    id_evento = max(ids_eventos, default=0) + 1

    event = {
        "id": id_evento,
        "nome_evento": nome_evento,
        "local": local,
        "data": data,
        "cachet": cachet,
        "tipo_evento": tipo_evento,
        "estado_evento": estado_evento
    }

    events.append(event)
    print("Evento criado com sucesso.")

# criar agendamento
def criar_agendamento(bookings: list, bands: list, events: list):
    if len(bands) == 0:
        print("Não existem bandas registadas.")
        return

    if len(events) == 0:
        print("Não existem eventos registados.")
        return

    print("\nBandas disponíveis:")
    for band in bands:
        print(f"ID: {band['id']} | Nome: {band['nome']}")

    id_band = ler_inteiro("Escolhe o ID da banda: ")
    banda_encontrada = False

    for band in bands:
        if band["id"] == id_band:
            banda_encontrada = True
            break

    if not banda_encontrada:
        print("ID da banda inválido.")
        return

    print("\nEventos disponíveis:")
    for event in events:
        print(f"ID: {event['id']} | Nome: {event['nome_evento']}")

    id_event = ler_inteiro("Escolhe o ID do evento: ")
    evento_encontrado = False

    for event in events:
        if event["id"] == id_event:
            evento_encontrado = True
            break

    if not evento_encontrado:
        print("ID do evento inválido.")
        return

    data_marcacao = ler_data("Data da marcação (YYYY-MM-DD): ")

    while True:
        estado_confirmacao = input("Estado da confirmação (pendente/confirmado/cancelado): ").strip().lower()
        if estado_confirmacao in ("pendente", "confirmado", "cancelado"):
            break
        print("Estado inválido. Escreve: pendente, confirmado ou cancelado.")
    
    observacoes = input("Observações: ")

    ids_bookings = [booking["id"] for booking in bookings]
    id_booking = max(ids_bookings, default=0) + 1

    booking = {
        "id": id_booking,
        "band_id": id_band,
        "event_id": id_event,
        "data_marcacao": data_marcacao,
        "estado_confirmacao": estado_confirmacao,
        "observacoes": observacoes
    }

    bookings.append(booking)
    print("Agendamento criado com sucesso.")


