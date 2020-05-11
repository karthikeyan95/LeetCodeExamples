class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a = 1
        while a <= num:
            power = a * a
            if power == num:
                return True
            if power < num:
                a += 1
            else:
                return False
        return False

    def usingBinarySearchMethod(self, num: int) -> bool:
        if num < 2:
            return True
        L,R = 2,num
        while L<= R:
            mid = (L + R) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                R = mid -1
            else:
                L = mid + 1
        return False


def main():
    number = 1
    obj = Solution()
    print(obj.isPerfectSquare(number))


if __name__ == '__main__':
    main()
