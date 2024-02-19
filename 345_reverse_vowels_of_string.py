## 345. Reverse Vowels of a String
'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
'''

# Difficulty: Easy

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels: set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        letters_array: list = list(s) # Only this syntax splits string into letters in Python. s.split("") does not work.
        i: int = 0
        j: int = len(letters_array) - 1
        while j > i:
            if letters_array[j] not in vowels:
                j -= 1
            if letters_array[i] not in vowels:
                i += 1
            if letters_array[i] in vowels and letters_array[j] in vowels:
                letters_array[i], letters_array[j] = letters_array[j], letters_array[i]
                i += 1
                j -= 1

        return "".join(letters_array)
    
# Beats 97.5% of submissions.
    
if __name__ == '__main__':
    s: str = "hello"
    output = Solution()
    print(output.reverseVowels(s))