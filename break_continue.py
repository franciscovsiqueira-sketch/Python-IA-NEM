while True:
    cmd = input('Comando: ').strip().lower()
    if cmd == 'sair':
        break #enerra o laço
    if cmd == '':
        continue #volta ao início
    print(f'Executando {cmd}')