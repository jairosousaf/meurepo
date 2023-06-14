# # Lista de Exercicios
# # Programação de Sistemas
# # Atividade Prática de Fixação

# # 1. Faça um Programa que peça um número e então mostre a mensagem: O número informado foi [número].
# num = int(input('Digite um número: '))
# print('O número informado foi:', num)

# # 2. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
# nome = input('Digite o nome do aluno:')
# not1 = float(input('Digite a nota do 1º Bimestre:'))
# not2 = float(input('Digite a nota do 2º Bimestre:'))
# not3 = float(input('Digite a nota do 3º Bimestre:'))
# not4 = float(input('Digite a nota do 4º Bimestre:'))
# 
# total = not1 + not2 + not3 + not4
# media = total / 4
# print('A média do aluno foi:', media)

# if media >= 7:
#     print('O Aluno:', nome + ' foi aprovado.')
# else:
#     print('O Aluno:', nome + ' foi reprovado.')

# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
lista = []
nome = input('Digite o nome do aluno: ')
lancar_notas = int(input('Digite a qtd de notas a serem lançadas no sistema:'))

for notas in range(lancar_notas):
    num = float(input('Digite a primeira nota: '))
    lista.append(num)
print()
media = sum(lista) / len(lista)

if media >= 7:
    print(f'O Aluno: {nome} foi aprovado.')
else:
    print(f'O Aluno: {nome} foi reprovado.')

print(f'A média do aluno: {nome} foi --> {media:.2f}.')

# # 3. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
# altura = float(input('Digite a medida da altura:'))
# area = altura ** 2
# print('A área do quadrado é:', area)

# # 4. Faça um Programa que peça dois números e imprima o maior deles.
# num1 = float(input('Digite o primeiro número:'))
# num2 = float(input('Digite o segundo número:'))

# if num1 > num2:
#     print(f'O número {num1} é maior que {num2}.')
# else:
#     print(f'O número {num2} é maior que {num1}.')
    
# # 5. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
# prod1 = float(input('Digite o preço do primeiro produto:'))
# prod2 = float(input('Digite o preço do segundo produto:'))
# prod3 = float(input('Digite o preço do terceiro produto:'))

# if prod1 < prod2 and prod1 < prod3:
#     print('Você deve comprar o produto de menor valor: ', prod1)
# elif prod2 < prod1 and prod2 < prod3:
#     print('Você deve comprar o produto de menor valor: ', prod2)
# elif prod3 < prod1 and prod3 < prod2:
#     print('Você deve comprar o produto de menor valor: ', prod3)
# else:
#     print('Os preços dos produtos são iguais, fica à sua escolha.')

# # 6. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou
# # escaleno.

# # Dicas:
# # Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# # Triângulo Equilátero: três lados iguais;
# # Triângulo Isósceles: quaisquer dois lados iguais;
# # Triângulo Escaleno: três lados diferentes;

# lado1 = float(input('Digite o valor do primeiro lado do triângulo. '))
# lado2 = float(input('Digite o valor do segundo lado do triângulo. '))
# lado3 = float(input('Digite o valor do terceiro lado do triângulo. '))

# if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
#     if lado1 == lado2 == lado3:
#         print('Os lados formam um triângulo equilátero: ')
#     elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
#         print('Os lados formam um triângulo isóisceles: ')
#     else:
#         print('Os lados formam um triângulo escaleno: ')
# else:
#     print('Os lados não formam um triângulo: ')

# # 7. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N-Noturno. Imprima a mensagem
# # "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

# turno = input("Em qual turno você estuda? Digite M para matutino, V para vespertino ou N para noturno: ")

# if turno == "M":
#     print("Bom dia!")
# elif turno == "V":
#     print("Boa tarde!")
# elif turno == "N":
#     print("Boa noite!")
# else:
#     print("Valor inválido!")

# 8. Faça um Programa que peça 2 números inteiros e um número real.
# Calcule e mostre:
# ● o produto do dobro do primeiro com metade do segundo.
# ● a soma do triplo do primeiro com o terceiro.
# ● o terceiro elevado ao cubo.

# num1 = int(input("Digite o primeiro número inteiro: "))
# num2 = int(input("Digite o segundo número inteiro: "))
# num3 = float(input("Digite um número real: "))

# result1 = (2 * num1) * (num2 / 2)
# result2 = (3 * num1) + num3
# result3 = num3 ** 3

# print("O produto do dobro do primeiro com metade do segundo é:", result1)
# print("A soma do triplo do primeiro com o terceiro é:", result2)
# print("O terceiro número elevado ao cubo é:", result3)

# # 9. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
# # (72.7*altura) - 58

# altura = float(input("Digite a sua altura em metros: "))
# peso_ideal = (72.7 * altura) - 58
# print("O seu peso ideal é:", peso_ideal, "kg")

# # 10. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# # ● Para homens: (72.7*h) - 58
# # ● Para mulheres: (62.1*h) - 44.7

# altura = float(input("Digite a sua altura em metros: "))
# genero = input("Digite o seu gênero (M para masculino, F para feminino): ")

# if genero == "M":
#     peso_idealM = (72.7 * altura) - 58
#     print("O seu peso ideal (para homens) é:", peso_idealM, "kg")
# elif genero != 'M':
#     print(genero.upper())
# elif genero == "F":
#     peso_idealF = (62.1 * altura) - 44.7
#     print("O seu peso ideal (para mulheres) é:", peso_idealF, "kg")
# else:
#     print('Gênero inválido. Digite "M" para masculino ou "F" para feminino.')

#print(s1.upper()) # transformas todas as letras em maiúsculas
# print(s1.lower()) # transformas todas as letras em minúscula
# print(s2.title()) # transforma a primeira letra de cada palavra em maiúscula

# print(s1.replace('Horizonte', 'Monte')) # substitui Horizonte por Monte
# print(s1.startswith('Belo')) # verifica se a string "começa" com 'Belo'
# print(s1.endswith('Monte')) # verifica se a string "termina" com 'Monte'

# print(s2.find('frase')) # retorna o índice da primeira ocorrencia da palavra 'frase'
# print(s2.split()) # particiona a string em outras separadas por espaço
# print(s2.split(',')) # particiona a string em outras separadas por vírgula

# print(f'Porcentagem já gasta do orçamento: {pct}%')
# print(f'Porcentagem já gasta do orçamento: {pct:.2f}%') # acrescentando casas decimais.