from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        check = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if check == nums[i]:
                count = count + 1
            elif count > 1:
                count = 1
                check = nums[i]
            elif count == 1:
                return check
        return check


def main():
    arr = [4, 1, 2, 1, 2]
    obj = Solution()
    print(obj.singleNumber(arr))


if __name__ == "__main__":
    main()
