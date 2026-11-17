from Q36 import encode
from utils import head, tail, init, last
import functools

def decode(codigo):
    return functools.reduce(lambda acc, x: acc + last(x)*head(x), codigo, '')

if __name__=="__main__":
    string = "aaaabccaadeeee"
    code = encode(string)
    print(code)
    print(decode(code))
    print(f"Inicial igual final? {string == decode(code)}")