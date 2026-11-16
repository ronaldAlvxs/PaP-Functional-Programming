from utils import head, tail, init, last

def joinToken(marcador, lista):
    if not lista:
        return []

    return head(lista) + ([marcador] if tail(lista) else []) + joinToken(marcador, tail(lista))

if __name__=="__main__":
    lista = [[1], [3, 4], [5, 6, 7, 8, 9]]
    print(joinToken(2, lista))