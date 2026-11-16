from utils import head, tail, init, last, take, drop, list_len

def splitHalf(lista):
    half = list_len(lista) // 2 
    # Subtraio 1 pois, qnd é par, o índice half/2 é metade + 1
    return [take(lista, half-1), drop(lista, half-1)]


if __name__=="__main__":
    lista = [1, 3, 4, 5, 6, 7, 8]
    print(splitHalf(lista))

