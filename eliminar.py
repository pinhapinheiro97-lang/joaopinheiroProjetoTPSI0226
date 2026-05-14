# Eliminar registos
from validadores import ler_inteiro, ler_email, ler_data
from pesquisar import pesquisar_por_campo
from dados import guardar_agendamentos, guardar_bandas, guardar_eventos

# sub menu de elminação
def menu_eliminar(bands, events, bookings):
    
    bandas_alteradas = False
    eventos_alterados = False
    agendamentos_alterados = False
    while True:
        print("\n--- ELIMINAR ---")
        print("1 - Eliminar banda")
        print("2 - Eliminar evento")
        print("3 - Eliminar agendamento")
        print("4 - Guardar e voltar")

        choice = input("Escolha uma opção: ")

        match choice:
            case "1":
                # como eliminar bandas elimina agendamentos associados tem que se guardar os dois
                if eliminar_bandas(bands, bookings):
                    bandas_alteradas = True
                    agendamentos_alterados = True
            case "2":
                if eliminar_eventos(events):
                    eventos_alterados = True
            case "3":
                if eliminar_agendamentos(bookings, bands, events):
                    agendamentos_alterados = True
            case "4":
                if bandas_alteradas:
                    guardar_bandas(bands)

                if eventos_alterados:
                    guardar_eventos(events)

                if agendamentos_alterados:
                    guardar_agendamentos(bookings)
                break
            case _:
                print("Opção inválida.")

# falta questionar se pretende apagar agendamentos associados
def eliminar_bandas(bands:list, bookings:list):
    id_banda = ler_inteiro("ID da banda: ")
    banda = pesquisar_por_campo(bands, "id", id_banda)

    if banda is None:
        print("Sem registo de Banda.")
        return False
    
    #verificar se há agendamentos relacionados
    tem_agendamentos = False
    for agendamento in bookings:
        if agendamento["band_id"] == id_banda:
            tem_agendamentos = True
            break

    if tem_agendamentos:
        confirmar = input(
            f"A banda {banda['nome']} tem agendamentos associados. "
            "Apagar a banda eliminará os agendamentos. Queres continuar? (s/n) "
        ).lower()
    else:
        confirmar = input(f"Eliminar {banda['nome']}? (s/n) ").lower()

    if confirmar == "s":
        bands.remove(banda)

        i = 0
        while i < len(bookings):
            if bookings[i]["band_id"] == id_banda:
                del bookings[i]
            else:
                i += 1

        print("Banda eliminada com sucesso.")
        return True
    else:
        print("Operação cancelada.")
        return False


def eliminar_eventos(events:list):
    id_evento = ler_inteiro("ID do evento: ")
    evento = pesquisar_por_campo(events, "id", id_evento)

    if evento is None:
        print("Sem registo de evento")
        return False
    confirmar = input(f"Eliminar {evento['nome_evento']}? (s/n)").lower()
    if confirmar == "s":
        events.remove(evento)
        print("Evento eliminada com sucesso.")
        return True
    else:
        print("Operação cancelada.")

def eliminar_agendamentos(bookings: list, bands: list, events: list):
    id_booking = ler_inteiro("ID do agendamento: ")
    booking = pesquisar_por_campo(bookings, "id", id_booking)

    if booking is None:
        print("Sem registo de agendamento.")
        return False

    banda = pesquisar_por_campo(bands, "id", booking["band_id"])
    evento = pesquisar_por_campo(events, "id", booking["event_id"])

    nome_banda = banda["nome"] if banda is not None else "Banda não encontrada"
    nome_evento = evento["nome_evento"] if evento is not None else "Evento não encontrado"

    print(f"\nAgendamento encontrado:")
    print(f"ID: {booking['id']}")
    print(f"Banda: {nome_banda}")
    print(f"Evento: {nome_evento}")
    print(f"Data: {booking['data_marcacao']}")
    print(f"Estado: {booking['estado_confirmacao']}")
    print(f"Observações: {booking['observacoes']}")

    confirmar = input("Eliminar este agendamento? (s/n): ").strip().lower()
    if confirmar == "s":
        bookings.remove(booking)
        print("Agendamento eliminado com sucesso.")
        return True

    print("Operação cancelada.")
    return False


