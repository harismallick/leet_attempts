## 290. Word Pattern
'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_set = set(pattern)
        string_set = set(s.split(" "))
        if len(pattern_set) != len(string_set):
            return False
        
    
if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    output = Solution()
    print(output.wordPattern(pattern, s))