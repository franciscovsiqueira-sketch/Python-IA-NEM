try:
    temp = float(input('Temperatura'))
except ValueError:
    print(f'Valor inválido: use números')
else:
    print(f'Leitura aceita: {temp:.1f}')
finally:
    print('Fim da tentativa')
