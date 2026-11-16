# Retorna primeiro elemento da lista
def head(lista):
    return lista[0]

# Retorna a lista sem o primeiro elemento
def tail(lista):
    return lista[1:]

# Retorna a lista sem o ultimo elemento
def init(lista):
    return lista[:-1]

# Retorna último elemento da lista
def last(lista):
    return lista[-1]


# Retorna todos os elementos até o índice i (incluso)
def take(lista, i):
    if not lista:
        return []

    if i == 0:
        return [head(lista)]
    else:
        return [head(lista)] + take(tail(lista), i-1)

# Retorna a lista a partir do índice i (exclui i)
def drop(lista, i):
    if not lista:
        return []

    if i == 0:
        return tail(lista)
    else:
        return drop(tail(lista), i-1)

import functools

def list_len(lista):
    return functools.reduce(lambda result, current: result + 1, lista, 0)






import functools

# ACUMULADOR = 0 | []

# LISTA IMAGINARIA DE ENTRADA: [1, 2, 3, 4]

# ACUMULADOR, ELEMENTO DA LISTA
def aux(acc, b):
    return acc + b

def soma(lista):
    return functools.reduce(aux, lista, 0)

# or

def soma2(lista):
    return functools.reduce(lambda acc, x: acc+x, lista, 0)