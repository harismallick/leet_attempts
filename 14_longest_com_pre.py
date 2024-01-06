## Longest Common Prefix
# Difficulty: Easy
'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''
# My solution:
# def longestCommonPrefix(arr: list) -> str:
#     shortest_word = arr.pop(arr.index(min(arr)))
#     lcp = len(shortest_word)
#     temp = lcp
#     for word in arr:
#         i: int = 0

#         while lcp > 0:
#             if word.startswith(shortest_word[:lcp-i]):
#                 lcp = temp
#                 break
#             else:
#                 i += 1
#                 temp -= 1
        
#     return shortest_word[:lcp]

# More optimal solution:
# Sorting an array of string does it based on ASCII
# Just compare the common ASCII in the first and last strings in array.

def longestCommonPrefix(arr: list) -> str:
    arr_sorted = sorted(arr)
    first_word = arr_sorted[0]
    last_word = arr_sorted[-1]
    answer: str = ""
    for i in range(min(len(first_word), len(last_word))):
        if first_word[i] != last_word[i]:
            return answer
        answer += first_word[i]

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["cir","car"]))
# print(longestCommonPrefix(["flz","flg","fla"]))


