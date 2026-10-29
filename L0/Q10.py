from utils import head, tail, init, last

def conta_elementos(lista):
    if lista == []:
        return 0
    else:
        return 1 + conta_elementos(tail(lista))

if __name__=="__main__":
    entrada = []
    print(conta_elementos(entrada))