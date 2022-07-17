nome = str(input("Informe o nome do(a) aluno(a): "))
n1 = float(input("Informe a primera nota do(a) aluno(a): "))
n2 = float(input("Informe a segunda nota do(a) aluno(a): "))
f = int(input("Informe a quantidade de faltas do(a) aluno(a): "))
m = (n1+n2)/2

if m<7:
    print("O(a) aluno(a) {} foi reprovado(a) por média.".format(nome))
if f>3:
    print("O(a) aluno(a) {} foi reprovado(a) por falta.".format(nome))
if f<=3 and m>=7:
    print("O(a) aluno(a) {} foi aprovado(a) por média.".format(nome))
