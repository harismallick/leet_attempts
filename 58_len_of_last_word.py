## 58. Length of Last Word

'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.
'''

# Difficulty: Easy

# def lenOfLastWord(s: str) -> int:
#     letter_ascii_set: set = {x for x in range(ord("A"), ord("z")+1) if x not in range(91, 97)}
#     len_of_string: int = len(s)
#     last_word_len: int = 0
#     temp_word_len: int = 0
#     for i in range(0, len_of_string):
#         letter: str = s[i]
#         if ord(s[i]) not in letter_ascii_set:
#             if temp_word_len > 0:
#                 last_word_len = temp_word_len
#             temp_word_len = 0

#         else:
#             temp_word_len += 1

#     if temp_word_len > 0:
#         last_word_len = temp_word_len

#     return last_word_len

## faster solution:
# Since len of last word is required, loop the string from the back, break after first word
# This solution slower in Python for some reason. Original solutoin faster.

def lenOfLastWord(s: str) -> int:
    letter_ascii_set: set = {x for x in range(ord("A"), ord("z")+1) if x not in range(91, 97)}
    len_of_string: int = len(s)
    last_word_len: int = 0
    temp_word_len: int = 0
    
    for i in range(len_of_string-1, -1, -1):
        if ord(s[i]) not in letter_ascii_set:
            if temp_word_len > 0:
                last_word_len = temp_word_len
                break
            temp_word_len = 0

        else:
            temp_word_len += 1

    if temp_word_len > 0:
        last_word_len = temp_word_len

    return last_word_len

print(lenOfLastWord("hell world"))
print(lenOfLastWord("   fly me   to   the moon  "))
print(lenOfLastWord("luffy is still joyboy"))
print(lenOfLastWord("a"))
