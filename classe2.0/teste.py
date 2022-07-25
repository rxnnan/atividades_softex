class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_idade(self):
        return self.idade

    def set_idade(self, idade):
        self.idade = idade

pessoa = Pessoa("Carlos", 35)
print(pessoa.__dict__)
pessoa.nome = str(input("Informe o seu nome: "))
pessoa.idade = int(input("Informe a sua idade: "))
print(pessoa.nome)
print(pessoa.idade)