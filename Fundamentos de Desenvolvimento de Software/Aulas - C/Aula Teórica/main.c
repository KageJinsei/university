#include <stdio.h>
#include <stdlib.h>

/*
1 - obter as notas
2 - calcular a média
3 - verificar se o aluno foi aprovado ou não
4 - se a média for >= 7 é aprovado
5 - senão, é reprovado
*/
int main(void) {
    // declaração de variáveis
    float nota1, nota2, media;

    // obter as notas digitadas
    printf("Digite a primeira nota: ");
    scanf("%f", &nota1);

    printf("Digite a segunda nota: ");
    scanf("%f", &nota2);
    // calcula a média
    media = (nota1 + nota2)/2;
    // verificar se foi aprovado ou não
    if(media >= 7) {
        printf("Aluno aprovado!");
    } else {
        printf("Aluno reprovado");  
    }

    return 0;
}