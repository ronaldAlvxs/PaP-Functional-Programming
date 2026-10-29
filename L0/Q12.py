from utils import head, tail, init, last

def aux_primo(n, m):
    if m == 1:
        return True

    if n%m == 0:
        return False
    else:
        return aux_primo(n, m-1)

def ehPrimo(n: int):
    return aux_primo(n, n-1)

def n_primeiros_primos(n, start):
    if n == 0:
        return

    if ehPrimo(start):
        print(start)

    
        
if __name__=="__main__":
    print(ehPrimo(18))