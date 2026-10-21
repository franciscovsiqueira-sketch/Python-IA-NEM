temp_c = 27.5
temp_f = temp_c * 9 / 5 + 32
print('Temperatura:', temp_f, '°F')

segundos = 7530
horas = segundos // 3600
minutos = segundos % 3600 // 60
resto = segundos % 60
print(horas , 'h', minutos, 'min', resto, 's')


leitura = input('Leitura ADC: ')
tensao = leitura * 5 / 1023
print( 'Tensão:' + tensao)















