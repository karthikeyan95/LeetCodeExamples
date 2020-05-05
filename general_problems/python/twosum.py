from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int)->List[int]:
        result_set = []
        for idx1, num1 in enumerate(nums):
            for idx2,num2 in enumerate(nums):
                if idx1 == idx2:
                    continue
                elif num1 + num2 == target:
                    result_set.append(idx1)
                    result_set.append(idx2)
                    return result_set


def main():
    print("main function")
    numbers = [3, 3]
    target = 6
    obj = Solution()
    result = obj.two_sum(numbers, target)
    print(result)


if __name__ == '__main__':
    main()
