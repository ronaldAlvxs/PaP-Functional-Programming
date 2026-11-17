import functools
from utils import head, tail, init, last

def aux(acc, x):
    # Pega a letra da ultima tupla se ja existir alguma tupla.
    # E compara se eh igual a letra da rodada. Se for, soma
    if acc and last(last(acc)) == x:
        return init(acc) + [(head(last(acc))+1, x)]
    # Se nao existir tupla, ou a letra for diferente, adiciona na lista
    # uma nova tupla com a nova letra.
    else:
        return acc + [(1, x)]


def encode(string):
    return functools.reduce(aux, string, [])

if __name__=="__main__":
    string = "aaaabccaadeeee"
    print(encode(string))