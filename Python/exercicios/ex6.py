contador = 0
maior = 0
menor = 0
qtd_alunos = input("Qtd de alunos: ")

ate_20 = 0
entre_21_e_50 = 0
acima_de_50 = 0

while contador < qtd_alunos:
    nota = int(input("Nota do aluno: "))
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota

    if nota < 20:
        ate_20 = ate_20 + 1
    elif nota >= 21 and nota <= 50:
        entre_21_e_50 = entre_21_e_50 + 1
    else:
        nota > 50
        acima_de_50 = acima_de_50 + 1
    contador = contador + 1

print(f"A maior nota é {maior}")
print(f"A maior nota é {menor}")
