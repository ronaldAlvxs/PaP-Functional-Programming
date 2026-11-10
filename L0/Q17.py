from utils import head, tail, init, last
from Q13 import concat

def numeros_maiores_que_n(n, lista):
    if not lista:
        return []
    
    if head(lista) > n:
        return concat([head(lista)], numeros_maiores_que_n(n, tail(lista)))
    else:
        return numeros_maiores_que_n(n, tail(lista))

if __name__=="__main__":
    lista = [1, 2, 3, 4, 10, 9, 5, 3, 1]
    print(numeros_maiores_que_n(10, lista))