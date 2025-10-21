lista = []

def Adicionar10ValoresNaLista(lista):
    while len(lista) < 9:
        valor = input(f"({10-len(lista)} RESTANTES) Informe um valor: ")
        lista.append(valor)

Adicionar10ValoresNaLista(lista)

print(lista)