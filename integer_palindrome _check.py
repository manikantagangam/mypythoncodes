def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    else: 
        p = list(str(x))
        if p[::-1] == p:
            return True
        else:
            return False
print(isPalindrome(121))