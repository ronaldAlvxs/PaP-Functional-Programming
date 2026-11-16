from utils import head, tail, init, last
from Q20 import strip
from Q21 import consoantList

def matches(consonants, lista):
    if not lista:
        return []
    
    if consoantList(consonants, head(lista)):
        return [head(lista)] + matches(consonants, tail(lista))
    else:
        return matches(consonants, tail(lista))

if __name__=="__main__":
    lista = ["arara", "arreio","haskell" ,"vaca", "vacuo", "velho", "vermelho", "vicio"]
    print(matches("rr", lista))