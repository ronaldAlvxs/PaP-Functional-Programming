from utils import head, tail, init, last
from Q11 import ehPrimo

def proximoPrimo(k):
    if ehPrimo(k+1):
        return k+1
    else:
        return proximoPrimo(k+1)

if __name__=="__main__":
    print(proximoPrimo(3))