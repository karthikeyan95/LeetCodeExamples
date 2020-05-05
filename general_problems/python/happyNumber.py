class Solution:
    def isHappy(self, n: int) -> bool:
        result = n
        resultSet = []
        while True:
            result = self.findHappyNumber(n)
            if result == 1:
                return True
            elif result in resultSet:
                return False
            else:
                n = result
                resultSet.append(n)

    def findHappyNumber(self, n: int) -> int:
        result = 0
        while n > 0:
            remainder = int(n % 10)
            n = int(n / 10)
            result = result + remainder * remainder
        return result


def main():
    n = 20
    obj = Solution()
    print(obj.isHappy(n))


if __name__ == "__main__":
    main()
