from utils import head, tail
from Q24 import prime
from Q20 import strip
import functools

def freq_termo(termo, lista):
    return functools.reduce(lambda result, current: result + 1 if current == termo else result, lista, 0)

def factors_processing(list_factors):
    if not list_factors:
        return []
    
    numero = head(list_factors)
    return [(numero, freq_termo(numero, list_factors))] + factors_processing(strip([numero], list_factors))

    
def primeFactors(k):
    return factors_processing(prime(k))

if __name__=="__main__":
    print(primeFactors(92))