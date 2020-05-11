from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        print("town judge problem")
        solution_arr = [0] * N
        for a in trust:
            if solution_arr[a[1] - 1] is not -1:
                solution_arr[a[1] - 1] += 1
            solution_arr[a[0] - 1] = -1
        print(solution_arr)
        judge = max(solution_arr)
        if judge == N - 1:
            return solution_arr.index(judge) + 1
        return -1

    def anotherSolution(self, N: int, trust: List[List[int]]) -> int:
        solution_arr = [0] * N
        for a in trust:
            solution_arr[a[0] - 1] -= 1
            solution_arr[a[1] - 1] += 1
        for i in range(0, len(solution_arr)):
            if solution_arr[i] == N - 1:
                return i + 1
        return -1


def main():
    arr = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    N = 4
    obj = Solution()
    print(obj.findJudge(N, arr))


if __name__ == '__main__':
    main()
