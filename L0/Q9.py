from utils import head, tail, init, last

def conta_negativos(n, lista):
    if(n == 0):
        return 0

    if head(lista) < 0:
        return 1 + conta_negativos(n-1, tail(lista))
    else:
        return conta_negativos(n-1, tail(lista))

if __name__=="__main__":
    entrada = [1, -4, 3, -1, 2, 1, 1]
    print(conta_negativos(len(entrada), entrada))
