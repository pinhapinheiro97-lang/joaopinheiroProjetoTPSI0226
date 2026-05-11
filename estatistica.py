#estatitisca
from validadores import ler_data
def menu_estatistica(bands, events, bookings):
    while True:
        print("1 - Ver total e média de cachet faturado.")
        print("2 - Ver cachet previsto.")
        print("3 - Ver máximo e minimo faturado.")
        print("4 - Ver quantas bandas disponíveis.")
        print("5 - Ver géneros musicais.")
        print("6 - Filtrar agendamentos por data.")
        print("7 - Sair ")

        choice = input("Escolha uma das opções: ")

        match choice:
            case "1":
                ver_cachet(events)                               
            case "2":
                ver_cachet_naofaturado(events)
            case "3":
                ver_max_min(events)
            case "4":
                ver_bandas_disponivel(bands)
            case "5":
                ver_generos(bands)
            case "6":
                filtrar_agendamentos_pordata(bookings)
            case "7":
                break
            case _:
                print("Insere uma das opções válidas.")

def ver_cachet(events):
    eventos_pagos = [
        evento for evento in events
        if evento["estado_evento"].lower() == "pago"
    ]

    total_cachet = sum(evento["cachet"] for evento in eventos_pagos)
    print("Total faturado confirmado: ", total_cachet, "€")

    if len(eventos_pagos) > 0:

        media_cachet = (total_cachet/len(eventos_pagos))
        print("Média dos cachets pagos: ", media_cachet, "€")
    else:
        print("Não existem eventos pagos.")

def ver_cachet_naofaturado(events):
    eventos_naopagos = [
    evento for evento in events
    if evento["estado_evento"].strip().lower() == "nao pago"
    ]

    if len(eventos_naopagos) > 0:

        total_cachet = sum(evento["cachet"]for evento in eventos_naopagos)

        media_cachet = (total_cachet / len(eventos_naopagos))

        print("Total por faturar:", total_cachet, "€")

        print("Média dos cachets a faturar:", media_cachet, "€")

    else:
        print("Não existem agendamentos previstos")

def ver_bandas_disponivel(bands):
    bandas_disponivel= [ 
        banda for banda in bands
        if banda["disponivel"] == True
    ]

    if len(bandas_disponivel) > 0:
        print("Existem ", len(bandas_disponivel), "bandas disponiveis")

        for banda in bandas_disponivel:
            print("-", banda["nome"])
    
    else:
        print("Não existem bandas disponiveis.")

def ver_max_min(events):
        
    if len(events) == 0:
        print("Não existem eventos.")
        return
    
    max_cachet = events[0]
    for evento in events:
        if evento["cachet"] > max_cachet["cachet"]:
            max_cachet = evento
    
    min_cachet = events[0]
    for evento in events:
        if evento["cachet"] < min_cachet["cachet"]:
            min_cachet = evento

    print("---VALORES MÁXIMOS---")
    print("Maior cachet:", max_cachet["nome_evento"], "-", max_cachet["cachet"], "€")
    print("---VALORES MINIMOS---")
    print("Menor cachet:", min_cachet["nome_evento"], "-", min_cachet["cachet"], "€")

def ver_generos(bands):

    generos = {}

    for banda in bands:

        genero = banda["genero"].lower()

        if genero in generos:
            generos[genero] += 1
        else:
            generos[genero] = 1

    print("--- GÉNEROS MUSICAIS ---")

    for genero, quantidade in generos.items():
        print(genero, ":", quantidade, "bandas")


def filtrar_agendamentos_pordata(bookings):

    data_inicio = ler_data("Insira a data inicio YYYY-MM-DD: ")
    data_fim = ler_data("Insira a data fim YYYY-MM-DD: ")
    
    if data_inicio > data_fim:
        print("Erro: data início maior que data fim")
        return

    resultados = []

    for booking in bookings:

        data = booking["data_marcacao"]

        if data_inicio <= data <= data_fim:
            resultados.append(booking)

    print(f"--- Agendamentos entre {data_inicio} e {data_fim} ---")

    if len(resultados) > 0:

        for r in resultados:
            print(
                "ID Evento:",
                r["event_id"],
                "| ID Banda:",
                r["band_id"],
                "| Estado:",
                r["estado_confirmacao"],
                "| Data:",
                r["data_marcacao"]
            )

    else:
        print("Não existem agendamentos nesse intervalo.")












