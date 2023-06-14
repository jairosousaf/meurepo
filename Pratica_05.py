#As organizações Tabajaras resolveram dar um aumento de salário aos seus colaboradores e os convidaram para desenvolver um programa que calculasse os reajustes.
#Faça um programa que recebe o salário e um colaborador e o reajuste segundo o seguindo o seguinte critério:

#Salários até R$ 280.00 < aumento de 20%
#Salários de R$ 280.00 até R$ 700.00 < aumento de 15%
#Salários de R$ 700.00 até 1500.00 < aumento de 10%
#Salários >= R$ 1500.00 < aumento de 5%

#Após o aumento ser reajustado, informar na tela:
    #Salário anterior;
    #O percentual de aumento aplicado;
    #O valor do aumento;
    #O salário reajustado.

nome = input('Digite seu nome: ')
salario = float(input('Digite o salário: '))

if salario < 280:
    print(salario + (salario * 0.2))
    print('Salário anterior: R$ ', salario)
    print('O percentual aplicado foi: 20%')
    print('O Valor do aumento foi: ', salario * 0.2)
    print('O salário reajustado é: R$', salario + (salario * 0.2))

if salario >= 280 and salario < 700:
    print(salario + (salario * 0.15))
    print('Salário anterior: R$ ', salario)
    print('O percentual aplicado foi: 15%')
    print('O Valor do aumento foi: ', salario * 0.15)
    print('O salário reajustado é: R$', salario + (salario * 0.15))

if salario >= 700 and salario < 1500:
    print(salario + (salario * 0.10))
    print('Salário anterior: R$ ', salario)
    print('O percentual aplicado foi: 10%')
    print('O Valor do aumento foi: ', salario * 0.10)
    print('O salário reajustado é: R$', salario + (salario * 0.10))

if salario >= 1500:
    print(salario + (salario * 0.05))
    print('Salário anterior: R$ ', salario)
    print('O percentual aplicado foi: 5%')
    print('O Valor do aumento foi: ', salario * 0.05)
    print('O salário reajustado é: R$', salario + (salario * 0.05))