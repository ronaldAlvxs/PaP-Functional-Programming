from utils import head, tail, init, last, take, drop, list_len


def pyths(n):
    return [
        (x, y, z) 
        for x in range(1, n+1) 
        for y in range(1, n+1) 
        for z in range(1, n+1) 
        if (x**2 + y**2) == z**2]

if __name__=="__main__":
    print(pyths(5))