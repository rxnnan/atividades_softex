rodas = int(input("Quantas rodas o veículo possui: "))
peso = float(input("Qual o peso bruto do veículo em quilogramas: "))
vagas = int(input("Quantas pessoas cabem no veículo: "))

if 2<=rodas<=3:
    print("O tipo de habilitação recomendada é a A.")
elif rodas==4 and vagas<=8 and peso<=3500:
    print("O tipo de habilitação recomendada é a B.")
elif rodas>=4 and 3500<peso<=6000:
    print("O tipo de habilitação recomendada é a C.")
elif rodas>=4 and vagas>8:
    print("O tipo de habilitação recomendada é a D.")
elif rodas>=4 and peso>6000:
    print("O tipo de habilitação recomendada é a E.")
else:
    print("O veículo não se enquadra em nenhuma das categorias disponíveis.")