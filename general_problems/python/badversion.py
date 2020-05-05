import time

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        while left < right:
            midpoint = int(left + (right - left) / 2)
            if isBadVersion(midpoint) is True:
                right = midpoint
            else:
                left = midpoint + 1
        if left == right and isBadVersion(left) is True:
            return left
        return -1


temp_array = [False, False, False, True, True, True]


def isBadVersion(n: int) -> bool:
    return bool(temp_array[n])


def main():
    n = 5
    obj = Solution()
    print(obj.firstBadVersion(n))


if __name__ == '__main__':
    main()