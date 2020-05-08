 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_val = self.traverse(root, x, 0, 0)
        y_val = self.traverse(root, y, 0, 0)
        if x_val[0] != y_val[0] and x_val[1] == y_val[1]:
            return True
        return False

    def traverse(self, root: TreeNode, searchVal: int, height: int, rootval: int) -> list:
        if root is None:
            return None
        if root.val == searchVal:
            temp_arr =list()
            temp_arr.append(rootval)
            temp_arr.append(height)
            return temp_arr
        resultVal = self.traverse(root.left, searchVal, height + 1, root.val)
        if resultVal is None:
            resultVal = self.traverse(root.right, searchVal, height + 1, root.val)
        return resultVal



def main():
    node8 = TreeNode(8)
    node7 = TreeNode(7)
    node6 = TreeNode(6, node7)
    node5 = TreeNode(5)
    node4 = TreeNode(4)
    node3 = TreeNode(3, node5, node8)
    node2 = TreeNode(2, node4, node6)
    node1 = TreeNode(1, node2, node3)
    obj = Solution()
    print(obj.isCousins(node1, 8, 7))


if __name__ == '__main__':
    main()
