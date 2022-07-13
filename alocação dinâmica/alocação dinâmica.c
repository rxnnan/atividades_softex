# include <stdio.h>
# include <stdlib.h>

int main(){
    int i, tam = 7;
    char *nome;
    nome = (char *) malloc(tam * sizeof(char));
    nome = "Rennan";
    printf("\n\t%s", nome);
    nome = (char *) realloc(NULL, 22 * sizeof(char));
    nome = "Rennan Carbas";
    printf("\n\t%s", nome);
    free(nome);
printf("\n\n");
return 0;
}
