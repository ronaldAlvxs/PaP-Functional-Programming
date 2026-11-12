from utils import head, tail, init, last
from Q14 import pertence_a_lista
from Q13 import concat

def strip(lista1, lista2):
    if not lista2:
        return []

    if pertence_a_lista(head(lista2), lista1):
        return strip(lista1, tail(lista2))
    else:
        return concat([head(lista2)], strip(lista1, tail(lista2)))

if __name__=="__main__":
    lista1 = [1, 4, 1, "apple", 5]
    lista2 = ["apple", 1,"marina", "meu", "amor", 5, 1, 4, "apple"]
    print(strip(lista1, lista2))