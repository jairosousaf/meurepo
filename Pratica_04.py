nome = input('digite o nome do aluno: ')
cod = input('digite o codigo do aluno: ')
disc = input('digite o nome da disciplina: ')

n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
n3 = float(input('digite a terceira nota: '))

# checagem de validade de notas
if n1 > 10 or n2 > 10 or n3 > 10:
    print('Nota invalida')
    
total = n1 + n2 + n3
media = total / (n1 + n2 + n3)
    
if total >= 21 and total <= 29.9:
    print('Aprovado direto')
    
if total >= 15 and total < 21:
    print('Aluno de final')
    final = float(input('Digite a nota final'))
    mediaf = (media + final) / 2
    if mediaf >= 5:
        print ('Aprovado na final!')
    else:
        print('Aluno Reprovado!')

if total < 15:
    print('Reprovado direto')

if total == 30:
    print('Parabéns, nota máxima!')
    print('Nome do aluno:', nome)
    print('Código do aluno:', cod)
    print('Disciplina do aluno:', disc)