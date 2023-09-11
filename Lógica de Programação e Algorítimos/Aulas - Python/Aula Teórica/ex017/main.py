def borda(s1):
    tamanho = len(s1)
    # só imprime caso exista algum caractere
    if tamanho:
        print('+', '-' * tamanho, '+')
        print('|', s1, '|')
        print('+', '-' * tamanho, '+')

# programa principal
borda('Olá, Mundo!')
borda('Lógica de Programação e Algoritimos')