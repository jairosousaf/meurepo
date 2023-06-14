#Cadastro de usuário
nome = input("Digite seu nome: ")

print("Olá,", nome)

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))


#declaração de variáveis
mult = num1 * num2
div = num1 / num2
soma = num1 + num2
sub = num1 - num2

#impressão das variáveis
print("multiplicação:", mult)
print("divisão:", div)
print("soma:", soma)
print("subtração:", sub)

#declaração das variáveis de resultados
result = soma + sub
result_multi = soma * sub

#impressão dos resultados
print("resultado da multiplicação entre soma e subtração:", result_multi)
print("resultado entre soma e subtração:", result)
