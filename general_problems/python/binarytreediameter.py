class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    length = []

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        left = 0
        right = 0
        if root.left is not None:
            left = self.meter(root.left)
        if root.right is not None:
            right = self.meter(root.right)
        val = max(left, right) + 1
        return val

    def traverseTree(self, root: TreeNode) -> int:
        val = 0
        print(root.val)
        if root.left is not None:
            self.traverseTree(root.left)
        if root.right is not None:
            self.traverseTree(root.right)

    def meter(self, node: TreeNode) -> int:
        left = 0
        right = 0
        node_val = 0
        if node is not None and node.left is None and node.right is None:
            return 0
        if node is not None:
            node_val = 1
            if node.left is not None:
                left = self.meter(node.left)
            if node.right is not None:
                right = self.meter(node.right)
        print(node.val)
        print(str(left) + " " + str(right))
        val = max(left, right) + node_val
        return val


def main():
    node11 = TreeNode(11)
    node10 = TreeNode(10, node11)
    node9 = TreeNode(9)
    node8 = TreeNode(8, node9, node10)
    node7 = TreeNode(7, node8)
    node6 = TreeNode(6)
    node5 = TreeNode(5, node7)
    node4 = TreeNode(4, node6)
    node3 = TreeNode(3)
    node2 = TreeNode(2, node4, node5)
    node1 = TreeNode(1, node2, node3)
    node_test = TreeNode(1)
    obj = Solution()
    # print(obj.traverseTree(node1))
    # print(obj.diameterOfBinaryTree(node1))
    print(obj.meter(node1))


if __name__ == '__main__':
    main()

