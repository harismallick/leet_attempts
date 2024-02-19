## 344. Reverse String
'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
'''
# Difficulty: Easy

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i: int = 0
        j: int = len(s) - 1
        while j > i:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return None
    
# Beats 58% of submissions
    
if __name__ == '__main__':
    s = ["h","e","l","l","o"]
    output = Solution()
    output.reverseString(s)
    print(s)