import functools

def soma(lista):
    return functools.reduce(lambda acc, current: acc+current, lista, 0)

def produto_interno(vetor_A, vetor_B):
    return soma([x*y for x, y in zip(vetor_A, vetor_B)])

if __name__=="__main__":
    vetor_A = [1, 2, 3, 4]
    vetor_B = [3, 4, 5, 6]
    print(produto_interno(vetor_A, vetor_B))