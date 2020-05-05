from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        length = 0
        sample_string = ""
        for i in range(0, len(arr)):
            sample_string = arr[i]
            if not self.uniqueCheck(sample_string):
                continue
            for j in range(i+1, len(arr)):
                if self.uniqueCheck(sample_string + arr[j]):
                    sample_string += arr[j]
            if len(sample_string) > length:
                length = len(sample_string)
        return length

    def uniqueCheck(self, s: str) -> bool:
        check_val = [False] * 128
        for i in range(0, len(s)):
            val = ord(s[i])
            if check_val[val]:
                return False
            check_val[val] = True
        return True


def main():
    arr = ["a", "abc", "d", "de", "def"]
    obj = Solution()
    print(obj.maxLength(arr))


if __name__ == "__main__":
    main()
