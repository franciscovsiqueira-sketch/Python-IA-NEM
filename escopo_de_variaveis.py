LIMITE = 70

def verificar(temp):
    excesso = temp - LIMITE
    print(excesso)
    return excesso > 0
    

verificar(75)
