
# criar banda
def criar_bandas(bands:list):
    nome_banda = input("Nome da banda: ")
    numeros_membros = int(input("Número de membros: "))
    genero = input("Género musical: ")
    contacto = input("Contacto telefónico: ")
    email = input("Email de contacto: ")

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


    id_banda=len(bands) + 1
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
    nome_evento=input("Nome do evento: ")
    local=input("Local: ")
    data=input("Data do evento (YYYY-MM-DD): ")
    cachet=float(input("Valor de cachet: "))
    tipo_evento=input("Tipo de evento: ")
    estado_evento=input("Estado do evento: ") # verificar se aplico booleano nesta questão
    
    id_evento=len(events) + 1
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

    id_band = int(input("Escolhe o ID da banda: "))
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

    id_event = int(input("Escolhe o ID do evento: "))
    evento_encontrado = False

    for event in events:
        if event["id"] == id_event:
            evento_encontrado = True
            break

    if not evento_encontrado:
        print("ID do evento inválido.")
        return

    data_marcacao = input("Data da marcação (YYYY-MM-DD): ")
    estado_confirmacao = input("Estado da confirmação: ")
    observacoes = input("Observações: ")

    id_booking = len(bookings) + 1

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


