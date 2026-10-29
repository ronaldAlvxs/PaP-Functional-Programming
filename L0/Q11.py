from utils import head, tail, init, last

def aux(n, m):
    if m == 1:
        return True

    if n%m == 0:
        return False
    else:
        return aux(n, m-1)

def ehPrimo(n: int):
    return aux(n, n-1)
        
if __name__=="__main__":
    print(ehPrimo(18))