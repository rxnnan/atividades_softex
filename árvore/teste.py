import random
from arvore import ArvoreBinariaDeBusca
# CRIANDO a árvore
def arvore_1():
    lista1 = [45, 20, 30, 60, 81, 97, 100, 7, 8, 4]
    arvore = ArvoreBinariaDeBusca()
    for x in lista1:
        arvore.insere(x)
    return arvore    

abdb = arvore_1()
abdb.ordenacao()

print("\nMaior elemento: ", abdb.max())
print("Menor elemento: ", abdb.min())

# ADICIONANDO um valor extra na árvore
print("")
a = random.randint(0, 100)
abdb.insere(a)
print("Após inserir {}".format(a))
abdb.ordenacao()
print("\nMaior elemento: ", abdb.max())
print("Menor elemento: ", abdb.min())

# REMOVENDO um nó com dois filhos
print("")
r = random.choice([45, 20, 7])
abdb.remocao(r)
print("Após remover {}".format(r))
abdb.ordenacao()
print("\nMaior elemento: ", abdb.max())
print("Menor elemento: ", abdb.min())
print("\n------------------------------------")

# CRIANDO a árvore
def arvore_2():
    lista2 = [15, 6, 18, 3, 7, 16, 20, 4]
    arvore = ArvoreBinariaDeBusca()
    for x in lista1:
        arvore.insere(x)
    return arvore    

abdb = arvore_2()
abdb.ordenacao()

print("\nMaior elemento: ", abdb.max())
print("Menor elemento: ", abdb.min())

# ADICIONANDO um valor extra na árvore
print("")
r = random.randint(0, 100)
abdb.insere(r)
print("Após inserir {}".format(r))
abdb.ordenacao()
print("\nMaior elemento: ", abdb.max())
print("Menor elemento: ", abdb.min())

# REMOVENDO um nó com dois filhos
print("")
r = random.choice([15, 18])
abdb.remocao(r)
print("Após remover {}".format(r))
abdb.ordenacao()
print("\nMaior elemento: ", abdb.max())
print("Menor elemento: ", abdb.min())