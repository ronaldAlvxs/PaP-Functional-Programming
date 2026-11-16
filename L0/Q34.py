from utils import head, tail, init, last
import functools

def aux(acc, current):
    if not acc:
        return [current]

    if last(acc) == current:
        return acc
    else:
        return acc + [current]

def compress(lista):
    return functools.reduce(aux, lista, [])

if __name__=="__main__":
    lista = [1, 1, 2, 2, 2, 4, 5, 6, 77, 7, 9, 9, 10]
    print(compress(lista))