class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def obterNome(self):
        return self.nome

    def alterarNome(self, nome):
        self.nome = nome

pessoa1 = Pessoa("Junior")

print(pessoa1.obterNome())

pessoa1.alterarNome("João")
print(pessoa1.obterNome())