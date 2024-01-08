## 28. Find the Index of the First Occurrence in a String

'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

# Difficulty: Easy

def strStr(haystack: str, needle: str) -> int:
    if len(needle) > len(haystack):
        return -1
    i = 0
    needle_len = len(needle)

    while i <= len(haystack)-needle_len:
        if haystack[i:i+needle_len] == needle:
            return i
        i += 1
    return -1

print(strStr("sadbutsad", "sad"))
print(strStr("leetcode", "leeto"))
print(strStr("hello", "ll"))
print(strStr("a", "a"))

