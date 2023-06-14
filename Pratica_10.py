# Conferindo se a senha é igual. Para isso o usuário tem 3 chances de acerto. Iniciando no 0 seria 4 chances.

senha = int(input('Digite a senha: '))
tentativas = 1

while senha != 123 and tentativas < 3:
    tentativas = tentativas + 1 # ou tentativas += 1
    print('Senha incorreta, tente novamente!')
    senha = int(input('Digite a senha novamente: '))
    
if senha == 123:
    print('Senha correta:')
else:
    print('Número de tentativas excedeu o limite!')