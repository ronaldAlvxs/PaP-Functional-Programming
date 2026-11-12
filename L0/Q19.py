from utils import head, tail, init, last
from Q18 import invertelista
from Q13 import concat

def geraPalindromo(string):
    delimiter = ""
    return delimiter.join(concat(string, invertelista(string)))

if __name__=="__main__":
    print(geraPalindromo("abcd"))