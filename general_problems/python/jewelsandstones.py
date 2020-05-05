class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewel_stack = []
        result = 0
        for a in J:
            jewel_stack.append(a)
        for a in S:
            if a in jewel_stack:
                result += 1
        return result


def main():
    obj = Solution()
    J = "aA"
    S = "aAAbbbb"
    print(obj.numJewelsInStones(J, S))


if __name__ == '__main__':
    main()
