class Pessoa: 
    incremento = 0
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 

    def minhaf(self, incremento):
        print(f"Olá {self.nome}, você tem {self.idade} anos atualmente. Em {incremento} anos você terá {self.idade + incremento} anos.")


p1 = Pessoa("Rennan", 23)
p1.minhaf(5)


p2 = Pessoa("João", 27)
p2.minhaf(3)


p3 = Pessoa("Gabriel", 17)
p3.minhaf(10)


