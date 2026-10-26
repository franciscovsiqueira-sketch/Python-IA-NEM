soma, qtd = 0, 0
temp = float(input ('Temperatura (-999 encerra) : '))
while temp != -999:
    soma += temp #acumulador
    qtd+= 1 #contador
    temp = float(input ('Temperatura (-999 encerra): '))
print(f"Média de {qtd} leituras: {soma / qtd:.1f}")
