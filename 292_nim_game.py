## 292. Nim Game
'''
You are playing the following Nim Game with your friend:

Initially, there is a heap of stones on the table.
You and your friend will alternate taking turns, and you go first everytime.
On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
The one who removes the last stone is the winner.
Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.

'''

class Solution:
    def canWinNim(self, n: int) -> bool:
    #     if n in [1,2,3]:
    #         return True
    #     answer: bool = self.recursive_check(n)
    #     return answer
    
    # def recursive_check(self, n: int, round: int=1):

    #     if n > 0:
    #         if n == 3 and (round % 2) != 0:
    #             return True
            
    #         # temp = round + 1
    #         one: bool = self.recursive_check(n-3, round=round+1)

    #         two: bool = self.recursive_check(n-2, round=round+1)

    #         three: bool = self.recursive_check(n-1, round=round+1)
    #         if one or two or three:
    #             return True

    #     return False
        return n % 4 != 0

# Recursive solution to complex. Didn't pass all test cases.
# One liner solution taken from solutions section.

if __name__ == '__main__':
    output = Solution()
    print(output.canWinNim(5))