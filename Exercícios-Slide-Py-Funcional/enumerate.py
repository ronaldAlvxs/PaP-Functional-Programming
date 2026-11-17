import functools

def my_len(lista):
    return functools.reduce(lambda acc, x: acc+1, lista, 0)

def my_enumerate(lista):
    return map(
        lambda i, x:
            (i, x), 
            range(my_len(lista)), 
            lista
    )

if __name__=="__main__":
    lista1 = [1, 2, 3, 4]
    print(list(enumerate(lista1)))
    print(list(my_enumerate(lista1)))