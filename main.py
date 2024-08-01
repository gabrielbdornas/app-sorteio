from random import randrange

lista = ['Gabriel', 'Maria', 'José']

def sorteio(lista):
    sorteado = randrange(0,len(lista))
    return lista[sorteado]
