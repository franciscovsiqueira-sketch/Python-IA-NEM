# Definir classe Pessoa:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")

# criando objetos (instâncias) da classe Pessoa
pessoa1 = Pessoa("Francisco", 15)
pessoa2 = Pessoa("Helena", 15)
pessoa3 = Pessoa("Giovanna", 16)
pessoa4 = Pessoa("Ana", 17)
pessoa5 = Pessoa("Arrascaeta", 32)

pessoa1.apresentar()
pessoa2.apresentar()
pessoa3.apresentar()
pessoa4.apresentar()
pessoa5.apresentar()
