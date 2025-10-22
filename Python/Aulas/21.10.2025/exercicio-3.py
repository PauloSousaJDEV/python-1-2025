max_strings = 10
lista_strings = []
contador = 1

print(f"\nINFORME 10 PALAVRAS\n")

while len(lista_strings) < max_strings:
    lista_strings.append(str(input(f"Palavra {contador}: ")))
    contador = contador + 1

tamanho_lista = len(lista_strings) - 1

print(f"\nExibindo lista invertida: \n")

while tamanho_lista >= 0:    
    print(f"{lista_strings[tamanho_lista]}")
    tamanho_lista = tamanho_lista - 1