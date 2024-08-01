from random import randrange, shuffle



def sorteio_unico(lista):
    sorteado = randrange(0,len(lista))
    return lista[sorteado]

def sorteio_ordenado(lista):
    shuffle(lista)
    return lista
