class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # magazine = list(magazine)
        check = 0
        for i in range(0, len(ransomNote)):
            if ransomNote[i] in magazine:
                magazine = magazine.replace(ransomNote[i], "", 1)
                check += 1
            print(magazine)
        if check == len(ransomNote):
            return True
        else:
            return False


def main():
    ransome = "fffbfg"
    magazine = "effjfggbffjdgbjjhhdegh"
    obj = Solution()
    print(obj.canConstruct(ransome, magazine))


if __name__ == '__main__':
    main()
