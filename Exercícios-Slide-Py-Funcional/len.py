import functools

def aux(acc, x):
    return acc + 1

def my_len(lista):
    return functools.reduce(aux, lista, 0)

if __name__=="__main__":
    lista = [False, False, False, "oi", False]
    print(my_len(lista))