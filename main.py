#Projeto Final Python - Sistema de Gestão de uma Agência Musical


'''
#Guarda apenas dados das bandas
bands = [
    {
        "id": 1,
        "nome": "Xutos e Pontapés",
        "numeros_membros": 5,
        "genero": "Rock",
        "contacto": "912654789",
        "email": "xutosepontapes@gmail.com",
        "disponivel": True
    }
]
#Guarda apenas dados dos eventos
events=[
    {
        "id": 1,
        "nome_evento": "Festas do Barreiro",
        "local": "Barreiro",
        "data": "2026-05-05",
        "cachet": 2500.50,
        "tipo_evento": "Festas Populares",
        "estado_evento": "planeado"
    }
]

#ligação entre as bandas e eventos geridos
bookings = [
    {
        "id": 1,
        "band_id": 1,
        "event_id": 1,
        "data_marcacao": "2026-04-27",
        "estado_confirmacao": "pendente",
        "observacoes": "A aguardar resposta da banda"
    }
]
'''

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


# JSON
import os as fsos
import json

filename_bandas="./data/bandas.json"
filename_eventos="./data/eventos.json"
filename_agendamentos="./data/agendamentos.json"

def carregar_dados():
    fsos.makedirs("./data", exist_ok=True)

    if fsos.path.exists("./data/bandas.json"):
        with open("./data/bandas.json", "r", encoding="utf-8") as f:
            bands = json.load(f)
    else:
        bands = []

    if fsos.path.exists("./data/eventos.json"):
        with open("./data/eventos.json", "r", encoding="utf-8") as f:
            events = json.load(f)
    else:
        events = []

    if fsos.path.exists("./data/agendamentos.json"):
        with open("./data/agendamentos.json", "r", encoding="utf-8") as f:
            bookings = json.load(f)
    else:
        bookings = []

    return bands, events, bookings

# função com apenas um parametro 
def guardar_bandas(bands):
    fsos.makedirs("./data", exist_ok=True)
    with open("./data/bandas.json", "w", encoding="utf-8") as f:
        json.dump(bands, f, ensure_ascii=False, indent=4)

def guardar_eventos(events):
    fsos.makedirs("./data", exist_ok=True)
    with open("./data/eventos.json", "w", encoding="utf-8") as f:
        json.dump(events, f, ensure_ascii=False, indent=4)

def guardar_agendamentos(bookings):
    fsos.makedirs("./data", exist_ok=True)
    with open("./data/agendamentos.json", "w", encoding="utf-8") as f:
        json.dump(bookings, f, ensure_ascii=False, indent=4)


def guardar_dados(bands, events, bookings): # Função redudante? 
    if not fsos.path.exists("./data"):
        fsos.makedirs("./data")

    with open("./data/bandas.json", "w", encoding="utf-8") as f:
        json.dump(bands, f, ensure_ascii=False, indent=4)

    with open("./data/eventos.json", "w", encoding="utf-8") as f:
        json.dump(events, f, ensure_ascii=False, indent=4)

    with open("./data/agendamentos.json", "w", encoding="utf-8") as f:
        json.dump(bookings, f, ensure_ascii=False, indent=4)

    print("Dados guardados com sucesso.")


# guardar ficheiros em json
# with open(filename_agendamentos,"w", encoding="utf-8") as manipfile:
 #                   json.dump(bookings, manipfile, ensure_ascii=False, indent=4)

'''
# ler o ficheiro
if fsos.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as manipfile:
        alunos=json.load(manipfile)
'''
    

#Iniciar menu

bands, events, bookings = carregar_dados()
menu(bands, events, bookings)