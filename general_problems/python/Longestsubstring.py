class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = ""
        result_length=0
        for element in s:
            print("result string: " + result)
            print("iter string: " + element)
            index = result.find(element)
            if index == 0:
                result = result[1:]
                result = result + element
            elif index > 0:
                result = result[index+1:]
                result = result + element
            else:
                result = result + element
                if result_length < len(result):
                    result_length = len(result)
        return result_length


def main():
    input_string = "ggububgvfk"
    obj = Solution()
    print(obj.lengthOfLongestSubstring(input_string))


if __name__ == "__main__":
    main()
