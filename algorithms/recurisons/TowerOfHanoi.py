class Solution:
    def solveTowerOfHanoi(self, disks: int, sourcetower: int, destinationtower: int, auxillarytower: int) -> None:
        if disks is 0:
            return
        self.solveTowerOfHanoi(disks - 1, sourcetower, auxillarytower, destinationtower)
        print("move disk: " + str(disks) + " to tower : " + str(destinationtower))
        self.solveTowerOfHanoi(disks -1, auxillarytower, destinationtower, sourcetower)


def main():
    disks = 4
    obj = Solution()
    print("Number of disks: " + str(disks))
    print("solution")
    obj.solveTowerOfHanoi(disks, 1, 3, 2)


if __name__ == '__main__':
    main()

