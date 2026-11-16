import functools

def aux(acc, x):
    return acc and bool(x)

def my_all(lista):
    return functools.reduce(aux, lista, True)

if __name__=="__main__":
    lista = ["oi", True]
    print(my_all(lista))