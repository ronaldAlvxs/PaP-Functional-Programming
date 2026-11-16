from utils import head, tail, init, last


def isPalindrome(string):
    if not string:
        return True

    if head(string) == last(string):
        return isPalindrome(tail(init(string)))
    else:
        return False


if __name__=="__main__":
    print(isPalindrome("maram"))