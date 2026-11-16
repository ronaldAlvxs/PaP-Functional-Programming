import sys
from utils import head, tail, init, last
import functools


# Coloca os elementos antes do marcador em uma lista, e deixa os demais na ultima lista. Se nao encontrar marcador, coloca uma lista vazia no final
def aux(marcador, lista):
    if not lista:
        return [[]]

    if head(lista) == marcador:
        return [tail(lista)]
    else:
        return [head(lista)] + aux(marcador, tail(lista))

def splitToken(marcador, lista):
    if not lista:
        return []

    list_marked = aux(marcador, lista)
    print(list_marked)
    return [init(list_marked)] + splitToken(marcador, last(list_marked))

if __name__=="__main__":
    lista = [1, 1, 1,2,3,4,2,5,6,7,8,9,0,3]
    print(splitToken(2, lista))
    