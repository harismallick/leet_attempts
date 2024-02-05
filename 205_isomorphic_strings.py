## 205. Isomorphic Strings
'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
'''

def isIsomorphic(s: str, t: str) -> bool:
    letters_map: dict = {}
    s_len: str = len(s)
    t_len: str = len(t)
    for i in range(0, max(s_len, t_len)):
        if s[i] not in letters_map and t[i] not in letters_map.values():
            letters_map[s[i]] = t[i]
        elif s[i] not in letters_map and t[i] in letters_map.values():
            return False
        elif letters_map[s[i]] != t[i]:
            return False

    return True

# faster than 77% of solutions.

if __name__ == '__main__':
    print(isIsomorphic("egg", "add"))
    # test: dict = {}
    # test["e"] = "a"
    # test["d"] = "f"
    # if "a" not in test:
    #     print("letter not in here")
    # else:
    #     print("letter in here")