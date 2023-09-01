A = int(input('Digite o primeiro lado do triângulo: '))
B = int(input('Digite o segundo lado do triângulo: '))
C = int(input('Digite o terceiro lado do triângulo: '))

if (A > 0) and (B > 0) and (C > 0):
    if (A + B > C) and (A + C > B) and (B + C > A):
    # Se vocÊ chegou até aqui, o triângulo é válido!

        if (A != B) and (A != C) and (B != C):
            print('Triangulo escaleno!')
        else:
            if (A == B) and (A == C) and (B == C):
                print('Triangulo equilátero!')
            else:
                print('Triangulo isósceles!')

    else:
        print('Ao menos um dos valores indicados não servem para formar um triângulo')
else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo')