from time import sleep
t = int(input("Informe quanto tempo (em segundos) você quer até a explosão: "))

print("Iniciando contagem regressiva")
for i in range(t, -1, -1):
    if i == 1:
        print("{} segundo até a explosão!".format(i))
    else:
        print("{} segundos até a explosão!".format(i))
    sleep(1)  
print("BUM!")    