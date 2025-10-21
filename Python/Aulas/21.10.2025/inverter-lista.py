def InverterLista(lista:list):
    total_lista = len(lista) - 1
    while total_lista >= 0:
        print(f"{lista[total_lista]}")
        total_lista = total_lista - 1

lista = [9, 72, 47, 31]
InverterLista(lista)