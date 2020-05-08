from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]
        x2 = coordinates[1][0]
        y2 = coordinates[1][1]
        for i in range(2, len(coordinates)):
            points = coordinates[i]
            lhs = int((points[0] - x1) * (y2 - y1))
            rhs = int((points[1] - y1) * (x2 - x1))
            if lhs != rhs:
                return False
        return True


def main():
    arr = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    obj = Solution()
    print(obj.checkStraightLine(arr))


if __name__ == '__main__':
    main()

