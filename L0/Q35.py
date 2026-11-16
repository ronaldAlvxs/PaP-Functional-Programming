import functools
from utils import head, tail, init, last

def aux(acc, x):
    if not acc:
        return [[x]]

    if last(last(acc)) == x:
        

def pack(lista):
    functools.reduce(aux, lista, [])

if __name__=="__main__":
    lista = [1, 1, 2, 2, 2, 4, 5, 6, 77, 7, 9, 9, 10]
    print(compress(lista))