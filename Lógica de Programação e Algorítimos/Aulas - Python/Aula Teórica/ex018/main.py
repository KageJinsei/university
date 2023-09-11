def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tamanho = len(s1)
    while ((tamanho < min) or (tamanho > max)):
        s1 = input(pergunta)
        tamanho = len(s1)
    return s1

# Programa principal

x = valida_string('Digite uma string: ', 10, 30)
print(f'Você digitou a string: {x}.\n Dado válido. Encerrando o programa...')