def contaLetra(palavra, caractere):
    aux = palavra.count(caractere)
    print(f"Na string {palavra} temos {aux} caracteres {caractere}.")
    return aux

def maiusculo(palavra):
    aux = palavra.upper()
    print(f"Colocando todas as letras da string {palavra} em maiúsculo vamos ter: {aux}")
    return aux

def tamanhoString(palavra):
    aux = len(palavra)
    print(f"A string {palavra} tem {aux} caracteres.")
    return aux         

p = str(input("Informe uma string: "))
c = str(input(f"Qual caractere você que contar na palavra {p}? "))
tamanhoString(p)
contaLetra(p, c)
maiusculo(p)
