import functools

def my_reversed(lista):
    return functools.reduce(
        lambda acc, x:
            [x] + acc,
        lista,
        []
    )

if __name__=="__main__":
    lista1 = [1, 2, 3, 4]
    print(my_reversed(lista1))