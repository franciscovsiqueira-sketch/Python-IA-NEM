def media(*valores):
    return sum(valores) / len (valores)
media(25, 26, 27)

def registrar(sensor, **dados):
    for chave, valor in dados.items():
        print(f'{sensor} {chave}={valor}')
registrar('T01', temp=25.0, umid=63)
