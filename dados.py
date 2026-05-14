# JSON
import os as fsos
import json

filename_bandas="./data/bandas.json"
filename_eventos="./data/eventos.json"
filename_agendamentos="./data/agendamentos.json"

def carregar_dados():
    fsos.makedirs("./data", exist_ok=True)

    try:
        if fsos.path.exists(filename_bandas):
            with open(filename_bandas, "r", encoding="utf-8") as f:
                bands = json.load(f)
        else:
            bands = []

        if fsos.path.exists(filename_eventos):
            with open(filename_eventos, "r", encoding="utf-8") as f:
                events = json.load(f)
        else:
            events = []

        if fsos.path.exists(filename_agendamentos):
            with open(filename_agendamentos, "r", encoding="utf-8") as f:
                bookings = json.load(f)
        else:
            bookings = []

        return bands, events, bookings

    except json.JSONDecodeError:
        print("Erro: O ficheiro JSON é inválido.")
        return [], [], []

    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return [], [], []


# função com apenas um parametro 
def guardar_bandas(bands):
    resposta = input("Deseja guardar as bandas? (s/n): ").strip().lower()
    if resposta == "s":
        try:
            fsos.makedirs("./data", exist_ok=True)

            with open(filename_bandas, "w", encoding="utf-8") as f:
                json.dump(bands, f, ensure_ascii=False, indent=4)

            print("Bandas guardadas com sucesso.")

        except Exception as e:
            print(f"Erro ao guardar bandas: {e}")

    else:
        print("Operação cancelada.")


def guardar_eventos(events):
    resposta = input("Deseja guardar os eventos? (s/n): ").strip().lower()
    if resposta == "s":
        try:
            fsos.makedirs("./data", exist_ok=True)

            with open(filename_eventos, "w", encoding="utf-8") as f:
                json.dump(events, f, ensure_ascii=False, indent=4)

            print("Eventos guardados com sucesso.")

        except Exception as e:
            print(f"Erro ao guardar eventos: {e}")

    else:
        print("Operação cancelada.")


def guardar_agendamentos(bookings):
    resposta = input("Deseja guardar os agendamentos? (s/n): ").strip().lower()
    if resposta == "s":
        try:
            fsos.makedirs("./data", exist_ok=True)

            with open(filename_agendamentos, "w", encoding="utf-8") as f:
                json.dump(bookings, f, ensure_ascii=False, indent=4)

            print("Agendamentos guardados com sucesso.")

        except Exception as e:
            print(f"Erro ao guardar agendamentos: {e}")

    else:
        print("Operação cancelada.")

'''
# Esta função é redudante, deixo aqui caso seja necessário a sua utilização
 
def guardar_dados(bands, events, bookings): 
    if not fsos.path.exists("./data"):
        fsos.makedirs("./data")

    with open("./data/bandas.json", "w", encoding="utf-8") as f:
        json.dump(bands, f, ensure_ascii=False, indent=4)

    with open("./data/eventos.json", "w", encoding="utf-8") as f:
        json.dump(events, f, ensure_ascii=False, indent=4)

    with open("./data/agendamentos.json", "w", encoding="utf-8") as f:
        json.dump(bookings, f, ensure_ascii=False, indent=4)

    print("Dados guardados com sucesso.")
'''