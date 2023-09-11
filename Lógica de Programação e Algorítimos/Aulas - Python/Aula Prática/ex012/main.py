# Achar vogais nas palavras da tupla

palavras = ('Mario', 'Luigi', 'Peach', 'Yoshi', 'Bowser')

for palavra in palavras:
    print(f'\nPalavra: {palavra.upper()}. Vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end='')