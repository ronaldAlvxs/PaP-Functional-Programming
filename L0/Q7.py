def fat(n: int) -> int:
    if(n == 0):
        return 1
    else:
        return n*fat(n-1)

def e(n: int) -> int:
    if(n == 0):
        return fat(0)
    else:
        return 1/fat(n) + e(n-1)

if __name__=="__main__":
    n = int(input("Digite um numero: "))
    if(n < 0):
        exit("Digite um valor >= 0. Encerrando.")

    print(e(n))