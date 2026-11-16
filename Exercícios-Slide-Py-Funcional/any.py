import functools

def aux(acc, x):
    return acc or bool(x)

def my_any(lista):
    return functools.reduce(aux, lista, False)

if __name__=="__main__":
    lista = [False, False, False, "oi", False]
    print(my_any(lista))