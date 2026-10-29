import utils

def finobacci(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return finobacci(n-1) + finobacci(n-2)


if __name__=="__main__":
    n = finobacci(2)
    print(f"{n}")