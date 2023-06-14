idade = int(input('Digite sua idade: '))

# 'Menor: de 18 anos'
# 'Adulto: maior de 18 anos'
# 'Idoso: acima de 65 anos'

if idade < 18:
    print(f'Menor de idade: {idade} anos')
elif idade >= 18 and idade < 60:
    print(f'Adulto: {idade} anos')
else:
    print(f'Você é idoso: {idade} anos')