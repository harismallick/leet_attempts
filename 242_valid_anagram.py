## 242. Valid Anagram
'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
# Difficulty: Easy

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for i in range(0, len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] += 1
            if t[i] not in t_dict:
                t_dict[t[i]] = 1
            else:
                t_dict[t[i]] += 1

        if s_dict == t_dict:
            return True

        return False
# Beats 78%

    
if __name__ == '__main__':
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram"))
    # print(solution.isAnagram("rad", "and"))

