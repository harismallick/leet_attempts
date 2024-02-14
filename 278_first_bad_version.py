## 278. First Bad Version
'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''

def isBadVersion(version: int) -> bool:
    bad_version: list = [2, 3]
    return version in bad_version

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        start: int = 1
        end: int = n
        while start <= end:
            middle: int = (start + end) // 2

            if isBadVersion(middle) and not isBadVersion(middle-1):
                return middle
            elif isBadVersion(middle):
                end = middle - 1
            else:
                start = middle + 1
        return -1

# Solution faster than 99.5% of submissions.
    
if __name__ == '__main__':
    # version: int = 4
    v_list: list = [1,2,3,4,5]
    output = Solution()
    print(output.firstBadVersion(3))
