# name = input('Digite seu nome: ')
# idade = int(input('Digite sua idade: '))
# localidade = input('Digite sua localidade: ')

# dicionario = {f'Nome: {name}, idade: {idade}, Cidade: {localidade}.'}

# print(name)

# outra situação com dicionário.
# chaves = ['a', 'b', 'c']
# valor_comun = 0

# dicionario = {}

# for chave in chaves:
#     dicionario[chave] = valor_comun
# print(dicionario)

# criando entrada de dados dinamicamente.

chaves = ['a', 'b', 'c']
valor = int(input('Digite o número de valores a serem inseridos: '))

dicionario = {}

for chave in chaves:
    num = int(input('Digite as chaves de acordo com a qtd de valores: ')) 
    dicionario[chave] = valor
print(dicionario)

####
# lista = []
# count = int(input('Digite o número contador do range: '))

# for i in range(count):
#     num = int(input('Digite um número: '))
#     lista.append(num)
# print(lista)