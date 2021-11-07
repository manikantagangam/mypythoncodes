def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    else: 
        p = list(str(x))
        v = ""
        for i in range(0, len(p)):
            v = p[i] + v
        v = int(v)
        print(v)
        if x == v:
            return True
        else:
            return False
print(isPalindrome(121))