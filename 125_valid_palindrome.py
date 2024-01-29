## 125. Valid Palindrome
'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

def isPalindrome(s: str) -> bool:
    i: int = 0
    j: int = len(s)-1
    letters_ascii: list = [x for x in range(ord("a"), ord("z")+1)]
    letters_ascii = letters_ascii + [x for x in range(ord("0"), ord("9")+1)]
    while i <= j:
        left_letter: str = s[i].lower()
        right_letter: str = s[j].lower()
        if ord(left_letter) not in letters_ascii:
            i += 1
            continue
        if ord(right_letter) not in letters_ascii:
            j -= 1
            continue
        if left_letter != right_letter:
            return False
        i += 1
        j -= 1
        
    return True

if __name__ == '__main__':
    print(isPalindrome("A man, a plan, a canal: Panama"))
    print(isPalindrome("race a car"))
    print(isPalindrome(" "))
    print(isPalindrome("0P"))
    print(isPalindrome("a."))


