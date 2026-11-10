class Carro:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def buzinar(self):
        print(f"O {self.modelo} está buzinando: BEEP BEEP!")

carro1 = Carro("Volks", "Fusca", "Azul", 1980)
carro2 = Carro("BYD", "Seal", "branco", 2026)

print(carro1.modelo)
print(carro2.cor)

carro1.buzinar()
carro2.buzinar()
