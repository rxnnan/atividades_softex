RAIZ = "raiz"
# CRIANDO uma árvore binária
class No:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None

    def __str__(self):
        return str(self.dado)

class ArvoreBinaria:
    def __init__(self, dado=None, no=None):
        if no:
            self.raiz = no
        elif dado:
            no = No(dado)
        else:
            self.raiz = None        
    
    # PERCORRENDO a árvore em ordem simétrica
    def ordenacao(self, no=None):
        if no is None:
            no = self.raiz
        if no.esquerda:
            self.ordenacao(no.esquerda)
        print(no, end=' ')
        if no.direita:
            self.ordenacao(no.direita)
        
# Árvore Binária de Busca
class ArvoreBinariaDeBusca(ArvoreBinaria):
    def insere(self, valor):
        pai = None
        aux = self.raiz
        while(aux):
            pai = aux
            if valor < aux.dado:
                aux = aux.esquerda
            else:
                aux = aux.direita
        if pai is None:
            self.raiz = No(valor)
        elif valor < pai.dado:
            pai.esquerda = No(valor)
        else:
            pai.direita = No(valor)

    def busca(self, valor):
        return self._busca(valor, self.raiz)

    def _busca(self, valor, no):
        if no is None:
            return no
        if no.dado == valor:
            return ArvoreBinariaDeBusca(no)
        if valor < no.dado:
            return self._busca(valor, no.esquerda)
        return self._busca(valor, no.direita)

    # ENCONTRANDO o maior e o menor valor da árvore
    def min(self, no=RAIZ):
        if no == RAIZ:
            no = self.raiz
        while no.esquerda:
            no = no.esquerda
        return no.dado     

    def max(self, no=RAIZ):
        if no == RAIZ:
            no = self.raiz
        while no.direita:
            no = no.direita
        return no.dado    
    
    # REMOVENDO um elemento da árvore
    def remocao(self, valor, no=RAIZ):
        if no == RAIZ:
            no = self.raiz
        if no is None:
            return no
        if valor < no.dado:
            no.esquerda = self.remocao(valor, no.esquerda)
        elif valor > no.dado:
            no.direita = self.remocao(valor, no.direita)
        else:
            if no.esquerda is None: 
                return no.direita
            elif no.direita is None:
                return no.esquerda
            else:
                sub = self.min(no.direita)
                no.dado = sub
                no.direita = self.remocao(sub, no.direita)
        return no         