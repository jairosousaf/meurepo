#Crie um programa que cheque se um individuo é de maior ou não
nome = input("Digite o nome do individuo: ")
ano = int(input("Digite seu ano de nascimento: "))
idade = 2023 - ano

if(idade >= 18):
    print("O individuo é maior")
else:
    print("O individuo é menor")