# Retorna primeiro elemento da lista
def head(lista):
    return lista[0]

# Retorna a lista sem o primeiro elemento
def tail(lista):
    return lista[1:]

# Retorna a lista sem o ultimo elemento
def init(lista):
    return lista[:-1]*x

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


# list comprehension exemplos

s = [x for x in range(0,11)]

pares = [x for x in s if x % 2 == 0] # Diferente de s?

impares = [x for x in s if not x % 2 == 0] # Qual o conteúdo?

pares_ou_zeros = [0 if x % 2 == 0 else x for x in s] # O q faz?

quadrados = [x*x for x in range(5)] # [0, 1, 4, 9, 16]

res = [n for n in range(100) if n % 5 == 0 if n % 6 == 0]

res = [n for n in range(100) if n % 5 == 0 and n % 6 == 0] #equivalente