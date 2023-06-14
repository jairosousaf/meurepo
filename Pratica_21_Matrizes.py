# import numpy as np
# matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(matriz)

# criando matriz vazia
# import numpy as np

# linha = int(input('Digite a qtd de linhas: '))
# coluna = int(input('Digite a qtd de colunas: '))

# matriz = np.empty((linha, coluna))

# print(matriz)

# criando matriz com zero
# import numpy as np

# m = np.zeros((4,4), dtype = float) # método (zeros)

# print(m)

# criando um matriz dinamicamente

# solicitando as dimensões da Matriz
# import numpy as np

# linha = int(input('Digite a qtd de linhas: '))
# coluna = int(input('Digite a qtd de colunas: '))

# # cria uma matriz vazia com as dimensões especificadas
# matriz = [[0 for i in range(linha)] for j in range(coluna)]

# # preenche a matriz com valores fornecidos pelo usuário
# for i in range(linha):
#     for j in range(coluna):
#         valor = int(input(f'Digite o valor para o elemento [{i}][{j}]: '))
#         matriz[i][j] = valor

# # exibe a matriz
# for i in range(linha):
#     for j in range(coluna):
#         print(matriz[i][j], end='')
#     if matriz [i][j] == 8:
#         print(f'Numero encontrado na linha: {i}, e coluna: {j}')
# print()
# print(matriz)

# criando 
# solicitando as dimensões da Matriz
# import numpy as np

# linha = int(input('Digite a qtd de linhas: '))
# coluna = int(input('Digite a qtd de colunas: '))

# # cria uma matriz vazia com as dimensões especificadas
# matriz = [[0 for i in range(linha)] for j in range(coluna)]

# preenche a matriz com valores fornecidos pelo usuário
# for i in range(linha):
#     for j in range(coluna):
#         valor = int(input(f'Digite o valor para o elemento [{i}][{j}]: '))
#         matriz[i][j] = valor
#         count = 0
#         count = count + 1
#         if valor == 0:
#             print(f'count')

# exibe a matriz
# for i in range(linha):
#     for j in range(coluna):
#         print(matriz[i][j], end='')
#     if matriz [i][j] == 8:
#         print(f'Numero encontrado na linha: {i}, e coluna: {j}')
# print()
# print(matriz)

#for num in lista1:
#     if num % 2 != 0:
#         soma += num
# print(soma)

# linha = int(input('Digite a qtd de linhas: '))
# coluna = int(input('Digite a qtd de colunas: '))

# # cria uma matriz vazia com as dimensões especificadas
# matriz = [[0 for i in range(linha)] for j in range(coluna)]

# # preenche a matriz com valores fornecidos pelo usuário
# for i in range(linha):
#     for j in range(coluna):
#         valor = int(input(f'Digite o valor para o elemento [{i}][{j}]: '))
#         matriz[i][j] = valor
#         count = 0
#         count = count + 1
#         if valor == 0:
#             print(f'count')

import numpy as np

matriz = np.empty((2,2), dtype=float)
cont = 0

for i in range (2):
    for j in range (2):
        valor = float(input('Digite o valor do elemento:['+str(i)+']'+'['+str(j)+']')) #if num % 2 != 0:
        matriz[i][j] = valor
        if valor == 0:
            cont = cont + 1
        
        lista_par = []
        if valor % 2 == 0:
            lista_par.append([valor])
print(matriz)
print(f'A quantidade Cont é: {cont}')
print()
print(f'A lista de números Par é: {lista_par}')


# crie um programa que rertorne a soma de todos os elementos de uma matriz.
# import numpy as np
# matriz = np.empty((2,2), dtype=int)

# # Preenchendo uma matriz com seus elementos
# soma = 0
# for i in range (2):
#     for j in range (2):
#         valor = int(input('Digite o valor do elemento: ')) #if num % 2 != 0:
#         matriz[i][j] = valor
    
#     soma = 0        # somando os elementos de uma matriz.
#     for i in matriz:
#         for j in i:
#             soma += j
   
# print(matriz)       # exibindo a soma
# print(f'A soma dos elementos da matriz é: {soma}')