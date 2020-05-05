from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        print(arr)
        result = 0
        for i in range(0, len(arr)):
            if arr[i] + 1 in arr:
                result += 1
        return result


def main():
    arr = [1,1,2,2]
    obj = Solution()
    print(obj.countElements(arr))


if __name__ == "__main__":
    main()
