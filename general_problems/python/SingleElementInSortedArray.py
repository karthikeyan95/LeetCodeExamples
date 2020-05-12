from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i = 0
        if len(nums) == 1:
            return nums[0]
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                i += 2
            else:
                break
        return nums[i]


def main():
    arr = [1,1,3]
    obj = Solution()

    print(obj.singleNonDuplicate(arr))


if __name__ == '__main__':
    main()
