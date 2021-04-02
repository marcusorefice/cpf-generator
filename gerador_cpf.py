from random import randint

numero = str(randint(100000000, 999999999))
novo_cpf = numero
mult = 10
soma = 0
temp = []

while True:
    if len(novo_cpf) == 10:
        mult = 11
    for p in novo_cpf:
        temp.append(int(p) * mult)
        mult -= 1
    soma = sum(temp)
    temp.clear()
    digito1 = 11 - (soma % 11)

    if digito1 > 9:
        digito1 = 0
    novo_cpf += str(digito1)

    if len(novo_cpf) == 11:
        print(novo_cpf)
        break
