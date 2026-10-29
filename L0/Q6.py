import utils

def fatorial(n: int) -> int:
    if(n == 0):
        return 1
    else:
        return n*fatorial(n-1)

if __name__=="__main__":
    n = fatorial(10)
    print(f"{n}")