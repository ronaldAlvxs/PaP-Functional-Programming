import functools

def divisores(n):
    return [i for i in range(1, n) if n%i == 0]

def soma(lista):
    return functools.reduce(lambda acumulador, atual: acumulador+atual, lista, 0)

def perfects(n):
    return [x for x in range(1, n+1) if soma(divisores(x)) == x]

if __name__=="__main__":
    print(perfects(500))