from solutions.advanced import DynamicProgramming, Greedy, TwoPointers, NumArray, NumMatrix, DivideAndConquer, \
    BackTracking
from solutions.base import Math, String, Array
from solutions.bits import BitManipulation
from solutions.design import MyStack, MinStack, RandomPicker, MedianFinder
from solutions.graphs import Dfs, Bfs, TopologicalSort
from solutions.lists import LinkedList, Stack
from solutions.maps import HashTable
from solutions.search import BinarySearch
from solutions.sort import Sorts
from utils import ListNode, TreeNode


def main():
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    print(Dfs().kthSmallest(root, 1
))


def _import():
    # Advanced
    DynamicProgramming()
    Greedy()
    TwoPointers()
    DivideAndConquer()
    BackTracking()
    NumArray([])
    NumMatrix([])

    # Base
    Math()
    String()
    Array()

    # Bits
    BitManipulation()

    # Design
    MyStack()
    MinStack()
    RandomPicker([])
    MedianFinder()

    # Lists
    LinkedList()
    Stack()

    # Maps
    HashTable()

    # Search
    BinarySearch()

    # Sort
    Sorts()

    # Trees
    Dfs()
    Bfs()
    TopologicalSort()

    # Utils
    ListNode()
    TreeNode()


if __name__ == '__main__':
    main()
