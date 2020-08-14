from problems import Array, Math, String, Tree, TwoPointers, LinkedList, HashTable, Stack, BinarySearch
from utils import ListNode, TreeNode


def main():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)

    # root.left.left = TreeNode(3)
    root.right.right = TreeNode(20)
    # root.left.left.left = TreeNode(4)
    root.right.left = TreeNode(6)

    print(Tree().isValidBST(root))


if __name__ == '__main__':
    main()
