import functools
from utils import head, tail, init, last

def pack_aux(acc, x):
    if acc and head(last(acc)) == x:
        return init(acc) + [last(acc) + [x]]
    else:
        return acc + [[x]]

def pack(lista):
    return functools.reduce(pack_aux, lista, [])

if __name__=="__main__":
    lista = [1, 1, 2, 2, 2, 4, 5, 6, 77, 7, 9, 9, 10]
    print(pack(lista))
    # a = [[]]
    # print(init(a))



    # zip([1, 2, 3], [4, 5, 6])
    # [(1, 4), (2, 5), (3, 6)]

    # for x, y in 