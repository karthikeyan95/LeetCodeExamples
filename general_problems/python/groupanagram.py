from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hash_map = {}
        for a in strs:
            added = 0
            temp = self.sortString(a)
            for key in hash_map:
                if key == temp:
                    hash_map[key].append(a)
                    added = 1
            if added == 0:
                hash_map[temp] = [a]
        for key in hash_map:
            result.append(hash_map[key])
        return result

    def sortString(self, string: str) -> str:
        temp_array = []
        result = ""
        for a in string:
            temp_array.append(ord(a))
        temp_array.sort()
        for a in temp_array:
            result += chr(a)
        return result


def main():
    arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # arr = ["", ""]
    obj = Solution()
    print(obj.groupAnagrams(arr))


if __name__ == "__main__":
    main()
