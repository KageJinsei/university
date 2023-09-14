def validaInt(pergunta, min, max):

    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def criaArquivo(nomeArquivo):
    try:
        archive = open(nomeArquivo, 'wt+')
        archive.close
    except:
        print('Erro na criação do arquivo')
    else:
        print(f'Arquivo {nomeArquivo} foi criado com sucesso!\n')    

def existeArquivo(nomeArquivo):
    try:
        archive = open(nomeArquivo, 'rt')
        archive.close()
    except FileNotFoundError:
        return False
    else:
        return True

def listarArquivo(nomeArquivo):
    try:
        archive = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(archive.read())        


def cadastrarJogo(nomeArquivo, nomeJogo, nomePlataforma):
    try:
        archive = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        archive.write(f'{nomeJogo};{nomePlataforma}\n')
    finally:
        archive.close()    

# main
pastaDestino = '/home/kagehinsei/Documentos/estudos-vscode/adsuninter/Lógica de Programação e Algorítimos/Aulas - Python/Aula Prática/ex011/'
arquivo = 'games.txt'
caminho = pastaDestino + arquivo
if existeArquivo(caminho):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente!')
    criaArquivo(caminho)

while True:
    print('-' *10 + 'MENU' + '-' * 10 + '\n' +
          '1 - Cadastrar novo item\n' +
          '2 - Listar cadastros\n' +
          '3 - Sair')
    
    opcao = validaInt('Escolha a opção desejada: ', 1, 3)

    if (opcao == 1):
        print('Opção de cadastrar novo item selecionada...\n')
        nomeJogo = input('Nome do jogo: ')
        nomePlataforma = input('Nome da plataforma: ')
        cadastrarJogo(caminho, nomeJogo, nomePlataforma)
    elif (opcao == 2):
        print('Opção de listar selecionada...\n')
        listarArquivo(caminho)
    elif (opcao == 3):
        print('Encerrando programa...')
        break