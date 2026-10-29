from utils import head, tail, init, last

def soma_negativos(lista):
    if head(lista) < 0:
        return head(lista) + soma_negativos(tail(lista))
    elif head(lista) > 0:
        return soma_negativos(tail(lista))
    else:
        return 0

if __name__=="__main__":
    entrada = [1, -4, 3, 1, -2, 1, 0]
    print(soma_negativos(entrada))

