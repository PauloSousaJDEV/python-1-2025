import random

def ListaAleatoria(num: int):
    list = []
    contador = 0

    while contador < num:
        list.append(random.randint(1,1001))
        contador = contador + 1
    
    return list
    
tamanho_array = int(input("Informe o tamanho da lista: "))
print(ListaAleatoria(tamanho_array))