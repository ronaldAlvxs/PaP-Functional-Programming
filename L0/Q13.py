from utils import head, tail, init, last
from Q11 import ehPrimo # True se sim, False caso contrario

def concat(list1, list2):
    if not list1:
        return list2

    # Isto eh redudante
    if not list2:
        return list1

    return [head(list1)] + concat(tail(list1), list2)

        
if __name__=="__main__":
    lista1 = [1, 4, 1, "apple"]
    lista2 = ["marina", "meu", "amor"]
    print(concat(lista1, lista2))