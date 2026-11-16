import functools

def aux(acc, x):
    return acc + x

def my_sum(lista):
    return functools.reduce(aux, lista, 0)

if __name__=="__main__":
    lista = [1, 2, 3, 4]
    print(my_sum(lista))
