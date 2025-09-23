num = int(input("Informe um número: "))
soma = 0

while num != 0:
    if num % 2 == 0:
        soma = soma + num
    num = int(input("Informe outro número: "))

print(soma)