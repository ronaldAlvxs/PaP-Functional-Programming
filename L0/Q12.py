from utils import head, tail, init, last
from Q11 import ehPrimo # True se sim, False caso contrario

def primeiros_n_primos_a_partir_de_candidato(candidato, n):
    if n <= 0:
        return []

    if ehPrimo(candidato):
        return [candidato] + primeiros_n_primos_a_partir_de_candidato(candidato+1, n-1)

    if not ehPrimo(candidato):
        return primeiros_n_primos_a_partir_de_candidato(candidato+1, n)

def primeiros_n_primos(n):
    return primeiros_n_primos_a_partir_de_candidato(1, n)
        
if __name__=="__main__":
    print(primeiros_n_primos(10))