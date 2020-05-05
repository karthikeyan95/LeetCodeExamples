class Solution:
    def defangIPaddr(self, address: str)->str:
        print("defang function")
        return address.replace(".", "[.]")


def main():
    ipaddress = "255.100.50.0"
    obj = Solution()
    print(obj.defangIPaddr(ipaddress))


if __name__ == '__main__':
    main()
