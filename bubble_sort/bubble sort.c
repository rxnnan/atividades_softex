#include <stdlib.h>
#include <locale.h>
#include <string.h>
#define NORMA 10

int main()
{
    setlocale(LC_ALL, "");
    int vetor [NORMA];
    int i, aux, j;

    printf("Informe 10 valores para preencher o vetor:\n");
    for (i = 0; i < NORMA; i++) {
        scanf("%d", &vetor[i]);
    }
    printf("Ordem inicial do números no vetor:\n");
    for (i = 0; i< NORMA; i++) {
        printf("%5d", vetor[i]);
    }
    for (j = 1; j < NORMA; j++) {
        for (i = 0; i < NORMA - 1; i++) {
            if (vetor[i] > vetor[i + 1]) {
                aux = vetor[i];
                vetor[i] = vetor[i + 1];
                vetor[i + 1] = aux;
            }
        }
    }
    printf("\nNúmeros do vetor em ordem crescente:\n");
    for (i = 0; i < NORMA; i++) {
        printf("%5d", vetor[i]);
    }
    return 0;
}
