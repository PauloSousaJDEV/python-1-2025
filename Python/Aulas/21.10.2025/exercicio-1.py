lista = []

while len(lista) < 9:
    valor = input(f"({10-len(lista)} RESTANTES) Informe um valor: ")
    lista.append(valor)

print(lista)