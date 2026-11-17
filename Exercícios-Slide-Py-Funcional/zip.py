import functools

def my_zip(lista1, lista2):
    return map(
        lambda x, y: (x, y), lista1, lista2
    )

if __name__=="__main__":
    lista1 = [1, 2, 3, 4]
    lista2 = [5, 6, 7, 8]
    print(list(my_zip(lista1, lista2)))
