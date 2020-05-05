class Solution:
    def firstUniqChar(self, s: str) -> int:
        temp_array = dict()
        for a in s:
            if a in temp_array:
                temp_array[a] += 1
            else:
                temp_array[a] = 1
        for key in temp_array.keys():
            if temp_array[key] is 1:
                return s.index(key)
        return -1


def main():
    string = "leetcode"
    obj = Solution()
    print(obj.firstUniqChar(string))


if __name__ == '__main__':
    main()
