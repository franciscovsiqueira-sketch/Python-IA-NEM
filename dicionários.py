sensor = {'id': 'T01', 'local': 'Linha 3', 'temp': 25.0}
sensor['local']
sensor['temp'] = 26.4
sensor['ativo'] = True
sensor.get('umid', 'n/d') 
del sensor['ativo']
len(sensor)
