class Solution:
    def findComplement(self, num: int) -> int:
        result = 0
        power = 1
        while num > 0:
            result += ((num % 2)^1) * power
            power <<= 1
            num >>= 1
        return result


def main():
    number = 10
    obj = Solution()
    print(obj.findComplement(number))


if __name__ == '__main__':
    main()
