from validadores import ler_inteiro, ler_email, ler_data, ler_contacto, ler_float, validar_contacto, validar_data, validar_email
from pesquisar import pesquisar_por_campo
from dados import guardar_agendamentos, guardar_bandas, guardar_eventos
from listar import mostrar_banda, mostrar_evento, mostrar_agendamento

def menu_editar(bands, events, bookings):
    
    alterado = False
    while True:
        print("\n--- EDITAR ---")
        print("1 - Editar banda")
        print("2 - Editar evento")
        print("3 - Editar agendamento")
        print("4 - Guardar e voltar")

        choice = input("Escolha uma opção: ")

        match choice:
            case "1":
                if editar_banda(bands):
                    alterado = True
            case "2":
                if editar_evento(events):
                    alterado = True
            case "3":
                if editar_agendamento(bookings, bands, events):
                    alterado = True
            case "4":
                if alterado:
                    guardar_agendamentos(bookings)
                    guardar_bandas(bands)
                    guardar_eventos(events)
                break
            case _:
                print("Opção inválida.")

def editar_banda(bands:list):
    id_banda = ler_inteiro("ID da banda: ")
    banda = pesquisar_por_campo(bands, "id", id_banda)

    if banda is None:
        print("Sem registo de Banda.")
        return False
    confirmar = input(f"Editar {banda['nome']}? (s/n)").lower()
    if confirmar == "s":

        print("\n--- DADOS ATUAIS ---")
        mostrar_banda(banda)

        print("\n--- NOVOS DADOS ---")
        novo_nome = input("Novo nome (Enter para manter): ").strip()
        if novo_nome:
            banda["nome"] = novo_nome
        
        novo_numero_membros = input("Número de membros (Enter para manter): ")
        if novo_numero_membros:
            # melhor do que ler_inteiro() para aceitar o enter para manter valor antigo
            while True:
                try:
                    banda["numeros_membros"] = int(novo_numero_membros)
                    break
                except ValueError:
                    print("Insere um número válido.")
                    novo_numero_membros = input("Número de membros (Enter para manter): ").strip()

        
        novo_genero = input("Género (Enter para manter): ")
        if novo_genero:
            banda["genero"] = novo_genero
        
        novo_contacto = input("Novo contacto (Enter para manter): ").strip()
        if novo_contacto:
            while not validar_contacto(novo_contacto):
                print("Contacto inválido.")
                novo_contacto = input("Novo contacto (Enter para manter): ").strip()
            banda["contacto"] = novo_contacto


        novo_email = input("Novo email (Enter para manter): ").strip()
        if novo_email:
            while not validar_email(novo_email):
                print("Email inválido.")
                novo_email = input("Novo email (Enter para manter): ").strip()
            banda["email"] = novo_email

        
        nova_disponibilidade = input("Está disponível? (s/n/Enter para manter): ").strip().lower()
        if nova_disponibilidade:
            while nova_disponibilidade not in ("s", "n"):
                print("Resposta inválida. Escreve (s) ou (n).")
                nova_disponibilidade = input("Está disponível? (s/n/Enter para manter): ").strip().lower()

            banda["disponivel"] = True if nova_disponibilidade == "s" else False

        print("Banda editada com sucesso.")
        return True
    else:
        print("Operação cancelada.")


def editar_evento(events: list):
    id_evento = ler_inteiro("ID do evento: ")
    evento = pesquisar_por_campo(events, "id", id_evento)

    if evento is None:
        print("Sem registo de Evento.")
        return False

    
    confirmar = input(f"Editar {evento['nome_evento']}? (s/n) ").lower()
    if confirmar == "s":
        print("\n--- DADOS ATUAIS ---")
        mostrar_evento(evento)

        print("\n--- NOVOS DADOS ---")

        novo_nome_evento = input("Nome de evento (Enter para manter): ").strip()
        if novo_nome_evento:
            evento["nome_evento"] = novo_nome_evento

        novo_local = input("Local (Enter para manter): ").strip()
        if novo_local:
            evento["local"] = novo_local

        nova_data = input("Data YYYY-MM-DD (Enter para manter): ").strip()
        if nova_data:
            while not validar_data(nova_data):
                print("Data inválida")
                nova_data = input("Data YYYY-MM-DD (Enter para manter): ").strip()
            evento["data"] = nova_data

        novo_cachet = input("Cachet (Enter para manter): ").strip()
        if novo_cachet:
            while True:
                try:
                    evento["cachet"] = float(novo_cachet)
                    break
                except ValueError:
                    print("Insere um número válido.")
                    novo_cachet = input("Cachet (Enter para manter): ").strip()

        novo_tipo_evento = input("Tipo de evento (Enter para manter): ").strip()
        if novo_tipo_evento:
            evento["tipo_evento"] = novo_tipo_evento

        novo_estado_evento = input("Estado do evento (pendente/confirmado/Enter para manter): ").strip().lower()
        if novo_estado_evento:
            while novo_estado_evento not in ("pendente", "confirmado"):
                print("Estado inválido. Escreve 'pendente' ou 'confirmado'.")
                novo_estado_evento = input("Estado do evento (pendente/confirmado/Enter para manter): ").strip().lower()
            evento["estado_evento"] = novo_estado_evento

        print("Evento editado com sucesso.")
        return True
    else:
        print("Operação cancelada.")
        return False