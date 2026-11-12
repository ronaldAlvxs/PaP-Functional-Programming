from utils import head, tail, init, last
from Q20 import strip

def consoantList(consonants, string):
    consoants_string = strip(['a', 'e', 'i', 'o', 'u'], string)

    if compare_lists(consonants, consoants_string):
        return True
    else:
        return False

def compare_lists(lista1, lista2):
    if (not lista1) and (not lista2):
        return True

    if (not lista1) and (lista2):
        return False

    if (lista1) and (not lista2):
        return False

    if (lista1) and (lista2):
        return (head(lista1) == head(lista2)) and compare_lists(tail(lista1), tail(lista2))

if __name__=="__main__":
    print(consoantList("sdd", "saude"))
    print(consoantList("sdd", "saudade"))