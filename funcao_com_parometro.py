def celsius_para_f(temp_c):
    return temp_c * 9/5 + 32

print(f'{celsius_para_f(30):.1f} °F')

def extremos(valores):
    return min(valores), max(valores)
menor, maior = extremos([25, 27, 24])
print(f'Menor: {menor}, Maior: {maior}')
