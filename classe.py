class Sensor:
    def __init__(self, codigo, local):
        self.codigo = codigo
        self.local = local
        self.leituras = []

t01 = Sensor('T01', 'Linha 1')
t02 = Sensor('T02', 'Linha 2')
print(t01.codigo, t02.local)
