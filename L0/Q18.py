from utils import head, tail
from Q13 import concat

def invertelista(lista):
    if not lista:
        return []

    return concat(invertelista(tail(lista)), [head(lista)])


if __name__=="__main__":
    lista = "abcd"
    print(invertelista(lista))