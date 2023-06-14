# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

# def aprovadoreprovado (n1, n2, n3):
#     media = (n1 + n2 + n3) /3
             
#     if num media <7:
#         print('reprovado.')
#     else:
#         print('Aprovado')  
## print(media)

# def salario():
#     vlr_hora = float(input('qnto vc ganha por hora? '))
#     hrs_trabalho = int(input('quantas horas trabalha no mês? '))
#     total = vlr_hora * hrs_trabalho
#     return total
# print(salario())

# def temperatura():
#     temp = float(input('Qual a temperatura "F"? '))
#     temp_celsius = 5 * ((temp - 32) / 9)
#     return temp_celsius
# print(f'A temperatura em Graus Celsius é: {temperatura():.2f}')

# 10. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# ● Para homens: (72.7*h) - 58
# ● Para mulheres: (62.1*h) - 44.7

# def peso_ideal():
#     altura = float(input("Digite a sua altura em metros: "))
#     genero = input("Digite o seu gênero (M para masculino, F para feminino): ")
    
#     if genero == 'M':
#         peso_idealM = (72.7 * altura) - 58
#         print("O seu peso ideal (para homens) é:", peso_idealM, "kg")
       
#     elif genero == 'F':
#         peso_idealF = (62.1 * altura) - 44.7
#         print("O seu peso ideal (para mulheres) é:", peso_idealF, "kg")
    
#     else:
#         print('Gênero inválido. Digite "M" para masculino ou "F" para feminino.')
# print(peso_ideal())

def investigacao():
    
    respostas = []
    texto = 'Olá, seja bem vindo ao programa de investigação. Responda "S" para Sim ou "N" para Não.'
    print(texto)
    p1 = input("Você entrou em contato com a vítima? ")
    #respostas.append(p1)
    p2 = input("Você esteve no local do crime nas últimas 24h? ")
    #respostas.append(p2)
    p3 = input("Você mora próximo da vítima? ")
    #respostas.append(p3)
    p4 = input("Você mora próximo da vítima? ")
    #respostas.append(p4)
    p5 = input("Você esteve no local do crime nas últimas 24h? ")
    #respostas.append(p5)
    
    respostas.append(p1 + p2 + p3 + p4 + p5)
           
    qtd_sim = respostas.count('S')
                
    if qtd_sim in respostas == 2:
        print('Suspeita!')
    elif qtd_sim in respostas == 3 or 4:
        print('Cumplice!')
    elif qtd_sim in respostas == 5:
        print('Assassino!')
    else:
        print('Inocente!')
print(investigacao())