from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        number = 0
        count = 0
        for a in nums:
            if a != number:
                if count > int(n / 2):
                    return number
                else:
                    number = a
                    count = 1
            else:
                count += 1
        if count > int(n / 2):
            return number
        return -1


def main():
    arr = [2,2,1,1,1,2,2]
    obj = Solution()
    print(obj.majorityElement(arr))


if __name__ == '__main__':
    main()