# # calculando funções

# def somar(): # função de soma
#     num1 = float(input('Digite o primeiro número: '))
#     num2 = float(input('Digite a segunda número: '))
#     num3 = float(input('Digite a terceira número: '))
    
#     media = (num1 + num2 + num3) / 3
#     soma = (num1 + num2 + num3)
    
#     return media, soma
# print(f'A média e soma do cômputo das notas do aluno foram respectivamente: {somar()}')

# calculando a área de um triângulo

# def areatriangulo():
#     base = float(input('Digite o tamanho da base: '))
#     altura = float(input('Digite o tamanho da altura: '))
    
#     area = (base * altura) / 2
    
#     return area
# print(f'A área do triangulo é: {areatriangulo()}')

# Funcionamento de uma função
# crie uma função para resolver uma equação de 2º Grau (a*(x**2) + (b*x) + c = 0)

# import math

# def equacao2grau (a, b, c):
#     a = float(input('Digite o valor de "a" na equação: '))
#     b = float(input('Digite o valor de "b" na equação: '))
#     c = float(input('Digite o valor de "c" na equação: '))
    
#     # calculando o discriminante: báscara
#     discriminante = (b ** 2) - (4 * a * c)
    
#     # verificar se a equação tem raizes reais
#     if discriminante >= 0:
#         # calcule as raizes reais
#         raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
#         raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
#         return raiz1, raiz2
#     else:
#         # calcula as raízes complexas
#         raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
#         raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
#         return raiz1, raiz2

# # Exemplo de uso da função
# coeficiente_a = 1
# coeficiente_b = -3
# coeficiente_c = 2

# raiz1, raiz2 = equacao2grau(coeficiente_a, coeficiente_b, coeficiente_c)

# print('As raízes da equação são: ')
# print()
# print(f'Raiz 1: {raiz1}')
# print(f'Raiz 2: {raiz2}')

# crie uma função para saber se é maior de idade ou não.

# def maior_idade ():
#     idade = int(input('Digite sua idade: '))
             
#     if idade < 18:
#         print(f'Você é menor de idade!')
#     elif idade >= 18 and idade < 60:
#         print(f'Você é um adulto!')
#     else:
#         print(f'O(a) senhor(a) é idoso(a)!')
#     return idade
# print(f'Sua idade é: {maior_idade()}')

# crie uma função para saber se um número é par ou impar.

def par_impar ():
    num = int(input('Digite um número: '))
             
    if num % 2 == 0:
        print(f'O número {num} é par.')
    else:
        print(f'O número {num} é impar.')  
    return num
print(f'O número é: {par_impar()}')