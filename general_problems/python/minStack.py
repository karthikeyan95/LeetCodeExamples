class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        temp_arr = list(self.stack)
        temp_arr.sort()
        return temp_arr[0]


def main():
    obj = MinStack()
    obj.push(-1)
    print(obj.top())
    print(obj.getMin())


if __name__ == '__main__':
    main()