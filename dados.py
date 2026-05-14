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
    resposta = input("Deseja guardar as bandas? (s/n): ").strip().lower()
    if resposta == "s":
        fsos.makedirs("./data", exist_ok=True)
        with open("./data/bandas.json", "w", encoding="utf-8") as f:
            json.dump(bands, f, ensure_ascii=False, indent=4)
    else:
        print("Operação cancelada.")

def guardar_eventos(events):
    resposta = input("Deseja guardar os eventos? (s/n): ").strip().lower()
    if resposta == "s":
        fsos.makedirs("./data", exist_ok=True)
        with open("./data/eventos.json", "w", encoding="utf-8") as f:
            json.dump(events, f, ensure_ascii=False, indent=4)
        print("Eventos guardados com sucesso.")
    else:
        print("Operação cancelada.")

def guardar_agendamentos(bookings):
    resposta = input("Deseja guardar os agendamentos? (s/n): ").strip().lower()
    if resposta == "s":
        fsos.makedirs("./data", exist_ok=True)
        with open("./data/agendamentos.json", "w", encoding="utf-8") as f:
            json.dump(bookings, f, ensure_ascii=False, indent=4)
        print("Agendamentos guardados com sucesso.")
    else:
        print("Operação cancelada.")


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