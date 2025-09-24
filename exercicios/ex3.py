qtd_alunos = int(input("Qtd de Alunos: "))
contador = 0
soma = 0
notas_menor_6 = 0
notas_maior_6 = 0

while contador < qtd_alunos:
    nota_aluno = int(input(f"Informe a nota do aluno {contador} entre 1 e 10: "))

    if nota_aluno >= 0 and nota_aluno <= 5:
        notas_menor_6 = notas_menor_6 + 1
    else:
        notas_maior_6 = notas_maior_6 + 1

    if nota_aluno > 10:
        print("A nota informada é maior que 10")
    elif nota_aluno < 1:
        print("A nota informada é menor que 10")
    else:
        soma = soma + nota_aluno
        contador = contador + 1

media_nota = soma / qtd_alunos
print(f"A média da nota destes alunos é: {media_nota}")
print(f"Quantidade de notas entre 0 e 5: {notas_menor_6}")
print(f"Quantidade de notas entre 6 e 10: {notas_maior_6}")