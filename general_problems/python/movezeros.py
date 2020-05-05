from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for i in range(0, len(nums)):
            if nums[i] == 0:
                temp = nums[i]
                temp_index = i + 1
                while temp_index < (size -1) and nums[temp_index] == 0:
                    temp_index += 1
                if temp_index <= (size-1):
                    nums[i] = nums[temp_index]
                    nums[temp_index] = temp
        print(nums)


def main():
    # arr = [0, 1, 0, 3, 12]
    arr = [0, 0, 1]
    obj = Solution()
    print(obj.moveZeroes(arr))


if __name__ == "__main__":
    main()