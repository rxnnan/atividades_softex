def calculadora(num1, num2, escolha):
    if escolha == 1:
        resultado = (f"{num1} + {num2} = {num1+num2}")
    elif escolha == 2:
        resultado = (f"{num1} - {num2} = {num1-num2}")
    elif escolha == 3:
        resultado = (f"{num1} * {num2} = {num1*num2}")
    elif escolha == 4:
        resultado = (f"{num1} / {num2} = {num1/num2}")
    else:
        resultado = ("0")
    return resultado    

n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))
esc = int(input('''Qual operação você quer realizar:
1.Soma
2.Subtração
3.Multiplicação
4.Divisão
'''))

print(calculadora(n1, n2, esc))