## 290. Word Pattern
'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_set = set(pattern)
        string_arr: list = s.split(" ")
        string_set = set(string_arr)
        if len(pattern_set) != len(string_set) or len(pattern) != len(string_arr):
            return False

        pattern_string_map: dict = {}
        for i in range(0, len(pattern)):
            if string_arr[i] not in pattern_string_map:
                pattern_string_map[string_arr[i]] = pattern[i]
            elif pattern_string_map[string_arr[i]] != pattern[i]:
                return False
            
        return True

# Solution beats 92% for both space and time.
if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
    output = Solution()
    print(output.wordPattern(pattern, s))