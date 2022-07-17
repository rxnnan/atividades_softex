x = 0 
y = 0 
z = 0 
n = 0

while True:
    try:
        voto = int(input('''Informe o número do candidato que você quer eleger: 
889 - Candidato X  
847 - Candidato Y 
515 - Candidato Z 
0 - Branco 
Qualquer valor diferente dos acima - Nulo
'''))
    except:
        print("Digite apenas números! Por favor, vote novamente.")
        continue

    if voto == 889:
        while True:
            x = x + 1
            print("Você votou no candidato X.")
            break
    elif voto == 847:
        while True:
            y = y + 1
            print("Você votou no candidato Y.")
            break
    elif voto == 515:
        while True:
            z = z + 1
            print("Você votou no candidato Z.")
            break
    elif voto == 0:
        while True:
            n = n + 1
            print("Você votou branco")
            break
    else: 
        while True:
            n = n + 1
            print("Você votou nulo.")
            break

    while True:
        de_novo = str(input('''Quer encerrar a votação aqui?
Digite S pra sim | Digite N para não    
'''))
        if de_novo == "S":
            if x > y and x > z:
                print(f"O vencedor da eleição foi o candidato X com {x} voto(s).")
            elif y > x and y > z:
                print(f"O vencedor da  votação foi o candidato Y com {y} voto(s).")
            elif z > x and z > y:
                print(f"O vencedor da  votação foi o candidato Z com {z} voto(s).")    
            else:
                print("Nenhum candidato ganhou a votação.")    
            
            print(f'''Votos para o candidato X: {x}
Votos para o candidato Y: {y}
Votos para o candidato Z: {z}
Votos nulos e brancos: {n}''')
            break
        
        elif de_novo == "N":
            break
        
        else:
            print("Entrada inválida. Por favor responda apenas com S ou N.")
            continue
    if de_novo == "S":
        break
