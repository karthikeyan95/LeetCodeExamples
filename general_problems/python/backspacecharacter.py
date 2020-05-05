class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S = self.parseString(S)
        T = self.parseString(T)
        if S == T:
            return True
        else:
            return False

    def parseString(self, parsing_string: str) -> str:
        string_array = []
        result = ""
        string_array = list(parsing_string)
        for i in range(0, len(string_array)):
            if string_array[i] == "#":
                j = i-1
                while j>=0 and string_array[j] == "#":
                    j -= 1
                if j >= 0:
                    string_array[j] = "#"
        for a in string_array:
            if a != "#":
                result += a
        return result
    def backspaceCompare1(self, S, T):
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)


def main():
    first_string = "y#fo##f"
    second_string = "y#f#o##f"
    obj = Solution()
    print(obj.backspaceCompare(first_string, second_string))


if __name__ == '__main__':
    main()
