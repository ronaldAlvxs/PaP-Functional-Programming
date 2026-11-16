from Q23 import proximoPrimo

def prime_aux(num, k):
    if num<=1:
        return []

    if num%k == 0:
        return [k] + prime_aux(num//k, k)
    else:
        return prime_aux(num, proximoPrimo(k))
    
def prime(k):
    return prime_aux(k, 2)

if __name__=="__main__":
    print(prime(27))