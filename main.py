from problems import Array, Math, String, Tree, TwoPointers, LinkedList, HashTable, Stack, BinarySearch
from utils import ListNode, TreeNode


def main():
    root = TreeNode(4)
    # root.left = TreeNode(0)
    # root.left.left = TreeNode(1)
    # root.left.left.left = TreeNode(7)
    # root.left.left.right = TreeNode(2)
    # root.right = TreeNode(1)
    # root.right.left = TreeNode(13)
    # root.right.right = TreeNode(4)
    # root.right.right.left = TreeNode(5)
    # root.right.right.right = TreeNode(1)

    print(Tree().smallestFromLeaf(root))


if __name__ == '__main__':
    main()
