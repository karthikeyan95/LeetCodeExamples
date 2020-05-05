from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max = 0
        global_max = -999999999
        for i in range(0, len(nums)):
            if nums[i] < nums[i] + local_max:
                local_max = nums[i] + local_max
            else:
                local_max = nums[i]
            if local_max > global_max:
                global_max = local_max
        return global_max


def main():
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # arr = [-1]
    obj = Solution()

    print(obj.maxSubArray(arr))


if __name__ == "__main__":
    main()
