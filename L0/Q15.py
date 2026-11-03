from utils import head, tail, init, last
from Q11 import ehPrimo # True se sim, False caso contrario
from Q14 import pertence_a_lista

def uniao(list1, list2):
    if not list1:
        return list2

    if not pertence_a_lista(head(list1), list2):
        return [head(list1)] + uniao(tail(list1), list2)

    if pertence_a_lista(head(list1), list2):
        return uniao(tail(list1), list2)

        
if __name__=="__main__":
    # Assumindo que as entradas ja são um conjunto matemático sem repetições
    lista1 = [1, 4, "apple"]
    lista2 = ["marina", "meu", "amor", 1, 4]
    print(uniao(lista1, lista2))