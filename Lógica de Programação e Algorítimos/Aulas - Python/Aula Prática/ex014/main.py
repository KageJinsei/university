cadastro = {'nome': [],
            'sexo': [],
            'ano': []
            }

while True:
    terminar = input('Deseja cadastar uma pessoa? [S/N]: ')
    if terminar.upper() in 'N':
        break
    if terminar.upper() not in 'S':
        print('Digite "S" para SIM ou "N" para NÃO')
    nome = input('Qual é o seu nome?: ')
    sexo = input('Qual é o seu sexo? [M/F]: ')
    ano = int(input('Qual é o seu ano de nascimento?: '))
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)

print(cadastro)