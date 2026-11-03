from utils import head, tail, init, last
from Q11 import ehPrimo # True se sim, False caso contrario
from Q14 import pertence_a_lista

def conta_qtd_superiores(numero, lista_numeros):
    if not lista_numeros:
        return 0

    if head(lista_numeros) > numero:
        return 1 + conta_qtd_superiores(numero, tail(lista_numeros))

    if not (head(lista_numeros) > numero):
        return conta_qtd_superiores(numero, tail(lista_numeros))

        
if __name__=="__main__":
    # Assumindo que as entradas ja são um conjunto matemático sem repetições
    lista = [1, 2, 3, 4, 10, 9, 5, 3, 1]
    print(conta_qtd_superiores(2, lista))