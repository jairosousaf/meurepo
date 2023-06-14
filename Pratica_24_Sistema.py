# criando a estrutura de dados para armazenar os funcionários
funcionarios = {}

def cadastrar_funcionario():
    nome = input('Digite o nome do funcionário: ')
    idade = int(input('Digite a idade do funcionário: '))
    cargo = input('Digite o cargo do funcionário: ')
    salario = float(input('Digite o valor do salário do funcionário: '))
    
    funcionario = {
        'nome': nome,
        'idade': idade,
        'cargo': cargo,
        'salario': salario
    }
    
    funcionarios[nome] = funcionario
    print('Funcionário cadastrado com sucesso!')
print(cadastrar_funcionario())

def exibir_funcionario():
    nome = input('Digite o nome do funcionário: ')
    
    if nome in funcionarios:
        funcionario = funcionarios[nome]
        print('Dados do funcionário: ')
        print('Nome:', funcionario['nome'])
        print('Idade:', funcionario['idade'])
        print('Cargo:', funcionario['cargo'])
        print('Salário:', funcionario['salario'])
    else:
        print('Funcionário não encontrado!')

def exibir_funcionarios():
    if funcionarios:
        print('Lista de Funcionários:')
        for nome, funcionario in funcionarios.items():
            print('Dados do funcionário: ')
            print('Nome:', funcionario['nome'])
            print('Idade:', funcionario['idade'])
            print('Cargo:', funcionario['cargo'])
            print('Salário:', funcionario['salario'])
            print('--------------------------')
    else:
        print('Não há funcionários cadastrados!')

def remover_funcionario():
    nome = input('Digite o nome do funcionário: ')
    
    if nome in funcionarios:
        del funcionarios[nome]
        print('Funcionário removido com sucesso!') 
    else:
        print('Funcionário não encontrado!')
        
# Menu principal
while True:
    print('\n=== Sistema de Cadastro de Funcionários ===')
    print()
    print('1 - Cadastrar funcionários')
    print('2 - Exibir dados de um funcionário')
    print('3 - Exibir todos os funcionários cadastrados')
    print('4 - Remover funcionário')
    print('0 - Sair')
    print()
    opcao = input('Digite a opção desejada: ')
    
    if opcao == '1':
        cadastrar_funcionario()
    elif opcao == '2':
        exibir_funcionario()
    elif opcao == '3':
        exibir_funcionarios()
    elif opcao == '4':
        remover_funcionario()
    elif opcao == '0':
        break
    else:
        print('Opção invalida. Digite novamente!')