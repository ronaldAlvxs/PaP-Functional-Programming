from utils import head, tail, init, last
from Q11 import ehPrimo # True se sim, False caso contrario

def pertence_a_lista(elemento, lista):
    if not lista:
        return False

    if elemento == head(lista):
        return True

    if elemento != head(lista):
        return pertence_a_lista(elemento, tail(lista))
    
if __name__=="__main__":
    lista1 = [1, 4, 1, "apple"]
    lista2 = ["marina", "meu", "amor"]
    print(pertence_a_lista("apple", lista1))