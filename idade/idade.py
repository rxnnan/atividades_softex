nome = str(input("Informe o seu nome completo: "))
a = True
while a:
    try:
        nascimento = int(input("Informe o ano do seu nascimento: "))
        if nascimento >= 1922 and nascimento <= 2021:
            idade_atual = 2022 - nascimento
        print(f"Muito bem {nome}, você tem ou vai ter {idade_atual} anos em 2022.")
        
        a = False
    except:
        print("Ano de nascimento invalido.")
        continue