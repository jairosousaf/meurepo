#Iniciando
nome = input("Digite seu nome: ")

#Declarando variáveis
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
MF = input("Se for homem, digite M, senão, F: ")

#Declarando variáveis com operadores matemáticos
mult = num1 * num2
div = num1 / num2
soma = num1 + num2
sub = num1 - num2
resto = num1 % num2
exp = num1 ** num2

#Impressão dos resultados na tela
print("Olá, " + nome + "!")
print("O resultado da multiplicação é: ", mult)
print("O resultado da divisão é: ", div)
print("O resultado da soma é: ", soma)
print("O resultado da subtração é: ", sub)
print("O resto da divisão é: ", resto)
print("O resultado da exponenciação é: ", exp)
print("O número Flutuante é: ", num3)
print("Você é do sexo: ", MF)