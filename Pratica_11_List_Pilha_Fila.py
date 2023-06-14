# criando uma lista e printando [list]

# lista = []
# num = int(input('Digite quantas vezes se repetirá o range: '))

# for elemento in range(num):
#     n = int(input('Digite o número: '))
#     lista.append(n)
# print(lista)
# print(sum(lista * 2))

# lista = []
# num = int(input('Digite quantas vezes se repetirá o range: '))

# for elemento in range(num):
#     n = int(input('Digite o número: '))
#     lista.append(n)
# print(lista)
# result = sum(lista) / 2
# print(result)

# lista = []
# num = int(input('Digite quantas vezes se repetirá o range: '))

# for i in range(num): #para o elemento i, num range de X números, faça:
#     n = int(input('Digite o número: '))
#     lista.append(n)
# numX = int(input('Digite outro número: '))

# if numX in lista: #se numX estiver contido na lista, então faça:
#     print(f'O número digitado {numX}, está na {[lista]}.')
# else:
#     print('O número não está na lista.')
# print(lista)

# lista = []
# num = int(input('Digite quantas vezes se repetirá o range: '))

# for i in range(num):
#     n = int(input('Digite o número: '))
#     lista.append(n)
# print(lista)
# print()
# num_order = sorted(lista)
# num_maior = max(lista)
# num_menor = min(lista)
# # num_asc = ord(lista)
# media = sum(lista) / len(lista)
# print(f'A média é: {media:.2f}')
# print(num_maior, num_menor)
# print(num_order)
#

lista = []
count = int(input('Digite o número contador do range: '))

for i in range(count):
    num = int(input('Digite um número: '))
    lista.append(num)
print(lista)

# print('Printando um número da lista. O número é:', lista [4])

# num = [1, 2, 3, 4, 5]
# print(num) # imprimindo a lista/vetor completo
# #print(num [2]) # imprimindo um número específico na lista

# # adicionando elementos
# num = [1, 2, 3]
# num.append(4)
# print(num)

# # inserindo elementos
# num.insert(1, 9)
# num.insert(1, 5)
# print(num)

# # removendo elementos
# num.remove(9)
# print(num)

# removendo e retornando elementos
# valor = num.pop(3)
# print(valor)
# print(num)