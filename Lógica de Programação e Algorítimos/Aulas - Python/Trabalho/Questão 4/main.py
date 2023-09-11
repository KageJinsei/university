# Variáveis globais
listaColaborador = []
idGlobal = 0

# Início da função cadastrarColaborador(i]d)
def cadastrarColaborador(id):
    print('*' * 72, '\n'+
          '-' * 22, 'MENU CADASTRAR COLABORADOR', '-' * 22, '\n' +
          '*' * 72, '\n')
    print(f'ID do colaborador: {idGlobal}')
    nome = input('Entre com o nome do colaborador: ') # Armazena o nome do colaborador
    setor = input('Entre com o setor: ') # Armazena o setor do colaborador
    pagamento = int(input('Entre com o pagamento (R$): ')) # Armazena o o salário que o colaborador irá receber
    cadastros = {
    'id': id,
    'nome': nome,
    'setor': setor,
    'salário': pagamento
    }
    listaColaborador.append(cadastros.copy()) # Pegando uma cópia do dicionário cadastros e adicionando na lista
# Final da função cadastrarColaborador(i]d)

# Início da função consultarColaborador()
def consultarColaborador():
    print('*' * 72, '\n'+
          '-' * 22, 'MENU CONSULTAR COLABORADOR', '-' * 22, '\n' +
          '*' * 72, '\n')
    print('[1] Consultar Todos\n' +
          '[2] Consultar por ID\n' +
          '[3] Consultar por Setor\n' +
          '[4] Retornar ao menu')
    while True:
        consultando = input('Escolha a opção desejada: ') # Armazena a entrada do usuário na variável consultando
        if (consultando != '1') and (consultando != '2') and (consultando != '3') and (consultando != '4'): # Se a opção do usuário for diferente das opções mostradas, apresenta uma mensagem de erro
            print('Opção inválida!')
            continue # Volta para o início do while True
        elif (consultando == '1'):
            for colaborador in listaColaborador: # colaborador irá verificar toda a lista de colaboradores
                print('-' * 25)
                for key, value in colaborador.items():
                    print(f'{key}: {value}')
                print('-' * 25)
        elif (consultando == '2'):
            consultandoID = int(input('\nDigite o ID a ser consultado: '))
            for colaborador in listaColaborador:
                if (colaborador['id'] == consultandoID): # Verificando se o valor do campo id é igual o valor desejado
                    print('-' * 25)
                    for key, value in colaborador.items():
                        print(f'{key}: {value}')
                    print('-' * 25)
        elif (consultando == '3'):
            consultandoID = input('\nDigite o setor a ser consultado: ')
            for colaborador in listaColaborador:
                if (colaborador['setor'] == consultandoID): # Verificando se o valor do campo setor é igual o valor desejado
                    print('-' * 25)
                    for key, value in colaborador.items():
                        print(f'{key}: {value}')
                    print('-' * 25)
        elif (consultando == '4'):
            break
        print('\n[1] Consultar todos os colaboradores\n' +
          '[2] Consultar colaborador por ID\n' +
          '[3] Consultar colaborador por setor\n' +
          '[4] Retornar ao menu')
# Final da função consultarColaborador()

# Início da função removerColaborador()
def removerColaborador():
    print('*' * 72, '\n'+
          '-' * 22, 'MENU REMOVER COLABORADOR', '-' * 22, '\n' +
          '*' * 72, '\n')
    remover = int(input('Digite o ID do colaborador a ser removido: ')) # Pergunta o ID do colaborador e armazena na variável remover ( aceita apenas números inteiros)

    for colaborador in listaColaborador:
        if (colaborador['id'] == remover): # Verificando se o valor do campo id é igual o valor desejado
            listaColaborador.remove(colaborador) # Remove da lista um colaborador coforme a entrada do usuário
            print('Colaborador removido')
# Final da função removerColaborador()

# Início do main
while True:
    print('*' * 72, '\n'+
          'Bem-vindo(a) ao Controle de Colaboradores - PROPRIETÁRIO: Kage Jinsei\n' +
          '*' * 72, '\n'+
          '-' * 28, 'MENU PRINCIPAL', '-' * 28)
    print('\n[1] Cadastrar Colaborador\n' +
          '[2] Consultar Colaborador(es)\n' +
          '[3] Remover Colaborador\n' +
          '[4] Sair')
    menuPrincipal = input('Escolha a opção desejada: ') # Pergunta a opção desejada e armazena na variável menuPrincipal

    if (menuPrincipal != '1') and (menuPrincipal != '2') and (menuPrincipal != '3') and (menuPrincipal != '4'): # Se a opção do usuário for diferente das opções mostradas, apresenta uma mensagem de erro
            print('Opção inválida!')
            continue # Volta para o início do while True
    elif (menuPrincipal == '1'):
        idGlobal += 1 # Incrementa +1 na variável idGlobal
        cadastrarColaborador(idGlobal) # Chama a função cadastrarColaborador(idGlobal)
    elif (menuPrincipal == '2'):
        consultarColaborador() # Chama a função consultarColaborador()
    elif (menuPrincipal == '3'):
        removerColaborador() # Chama a função removerColaborador()
    elif (menuPrincipal == '4'):
        break # Encerra o programa
# Final do main