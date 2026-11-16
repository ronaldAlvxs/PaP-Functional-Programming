import functools
from utils import head, last

def ataque_valido(posicaoA, posicaoB):
    if head(posicaoA) == head(posicaoB):
        return True

    if last(posicaoA) == last(posicaoB):
        return True

    # Diagonal que X e Y crescem na mesma direção
    if (head(posicaoA) - head(posicaoB)) == (last(posicaoA) - last(posicaoB)):
        return True

    # Diagonal que X e Y crescem em direções opostas (se avança X, diminui Y igualmente)
    if ((head(posicaoA) - head(posicaoB)) + (last(posicaoA) - last(posicaoB))) == 0:
        return True

    return False

def ataca(posicao, posicoes):
    return functools.reduce(lambda flag, x: True if ataque_valido(posicao, x) else flag, posicoes, False)


if __name__=="__main__":
    # Lista vazia
    assert ataca((1, 1), []) == False

    # Mesma linha
    assert ataca((1, 1), [(1, 5)]) == True
    assert ataca((2, 5), [(2, 1)]) == True

    # Mesma coluna
    assert ataca((1, 1), [(4, 1)]) == True
    assert ataca((5, 2), [(1, 2)]) == True

    # Diagonal principal (linha e coluna crescem juntas)
    assert ataca((1, 1), [(3, 3)]) == True
    assert ataca((4, 4), [(2, 2)]) == True

    # Diagonal secundária (uma cresce, a outra diminui)
    assert ataca((1, 4), [(3, 2)]) == True
    assert ataca((4, 2), [(2, 4)]) == True
    assert ataca((1, 8), [(8, 1)]) == True

    # Diagonal longa
    assert ataca((1, 1), [(8, 8)]) == True

    # Não ataca (movimento de cavalo e parecidos)
    assert ataca((1, 1), [(2, 3)]) == False
    assert ataca((1, 1), [(3, 2)]) == False
    assert ataca((1, 1), [(8, 7)]) == False

    # Várias posições, nenhuma ataca
    assert ataca((1, 1), [(2, 3), (3, 2), (4, 6)]) == False

    # Várias posições, só a primeira ataca
    assert ataca((1, 1), [(1, 2), (2, 4), (4, 6)]) == True

    # Várias posições, só a última ataca
    assert ataca((1, 1), [(2, 3), (3, 2), (4, 4)]) == True

    # Solução válida de 4 rainhas: nenhuma rainha ataca as outras
    assert ataca((4, 3), [(1, 2), (2, 4), (3, 1)]) == False
    assert ataca((3, 1), [(1, 2), (2, 4), (4, 3)]) == False
    assert ataca((2, 4), [(1, 2), (3, 1), (4, 3)]) == False
    assert ataca((1, 2), [(2, 4), (3, 1), (4, 3)]) == False

    # Candidatas para a linha 3, com as rainhas (1,2) e (2,4) já colocadas
    assert ataca((3, 1), [(1, 2), (2, 4)]) == False   # segura
    assert ataca((3, 2), [(1, 2), (2, 4)]) == True    # mesma coluna de (1,2)
    assert ataca((3, 3), [(1, 2), (2, 4)]) == True    # diagonal com (2,4)
    assert ataca((3, 4), [(1, 2), (2, 4)]) == True    # mesma coluna de (2,4)

    # Candidatas para a linha 4, com (1,2), (2,4) e (3,1) já colocadas
    assert ataca((4, 1), [(1, 2), (2, 4), (3, 1)]) == True    # coluna de (3,1)
    assert ataca((4, 2), [(1, 2), (2, 4), (3, 1)]) == True    # coluna de (1,2)
    assert ataca((4, 3), [(1, 2), (2, 4), (3, 1)]) == False   # segura
    assert ataca((4, 4), [(1, 2), (2, 4), (3, 1)]) == True    # coluna de (2,4)

    print("Todos os testes passaram")