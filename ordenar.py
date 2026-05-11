# ordenação

def menu_ordenar(bands, events, bookings):
    while True:
        print("\n--- Ordenação ---")
        print("1 - Ordenar bandas")
        print("2 - Ordenar eventos")
        print("3 - Ordenar agendamentos")
        print("4 - Voltar")

        choice = input("Escolha uma opção: ")

        match choice:
            case "1":
                campo = input("Campo de ordenação: ").strip()
                ordem = input("Ordem (crescente/decrescente): ").strip().lower()
                crescente = ordem == "crescente"
                bands = bubble_sort(bands, campo, crescente)
                print("Bandas ordenadas.")
            case "2":
                campo = input("Campo de ordenação: ").strip()
                ordem = input("Ordem (crescente/decrescente): ").strip().lower()
                crescente = ordem == "crescente"
                events = selection_sort(events, campo, crescente)
                print("Eventos ordenados.")
            case "3":
                campo = input("Campo de ordenação: ").strip()
                ordem = input("Ordem (crescente/decrescente): ").strip().lower()
                crescente = ordem == "crescente"
                bookings = bubble_sort(bookings, campo, crescente)
                print("Agendamentos ordenados.")
            case "4":
                break
            case _:
                print("Opção inválida.")


def bubble_sort(lista, campo, crescente=True):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i): # comparação um a um
            a = lista[j][campo]
            b = lista[j + 1][campo]

            if crescente:
                if a > b:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
            else:
                if a < b:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def selection_sort(lista, campo, crescente=True):
    n = len(lista)

    for i in range(n - 1):
        pos_melhor = i

        for j in range(i + 1, n): # pesquisa pelo menor elemento e compara com o resto da lista
            if crescente:
                if lista[j][campo] < lista[pos_melhor][campo]:
                    pos_melhor = j
            else:
                if lista[j][campo] > lista[pos_melhor][campo]:
                    pos_melhor = j

        if pos_melhor != i:
            lista[i], lista[pos_melhor] = lista[pos_melhor], lista[i]

    return lista