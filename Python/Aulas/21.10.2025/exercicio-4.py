num_informado = int(input("Informe um valor: "))
lista = []
contador = 1

while len(lista) < num_informado:
    num_sequencia = int(input(f"({contador} DE {num_informado}) Informe um número real: "))
    lista.append(num_sequencia)
    contador = contador + 1

while 