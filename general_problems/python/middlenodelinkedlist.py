import math


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        obj_handler = []
        iter_obj = head
        while iter_obj.next is not None:
            obj_handler.append(iter_obj)
            iter_obj = iter_obj.next
        obj_handler.append(iter_obj)
        mid = int(math.floor(len(obj_handler) / 2))
        return obj_handler[mid]


def addNewNode(x, head: ListNode):
    obj = ListNode(x)
    iter_obj = head
    while iter_obj.next is not None:
        iter_obj = iter_obj.next
    iter_obj.next = obj
    return head


def main():
    head = ListNode(1)
    for i in range(2, 11):
        head = addNewNode(i, head)
    obj = Solution()
    print(obj.middleNode(head))


if __name__ == "__main__":
    main()
