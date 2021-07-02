from solutions import Math, String
from solutions.advanced import (
    DynamicProgramming, Greedy, TwoPointers, NumArray, NumMatrix, DivideAndConquer, BackTracking
)
from solutions.bits import BitManipulation
from solutions.search import BinarySearch
from solutions.sort import Sorts
from solutions.structs import Array, HashTable, Heap, LinkedList, Stack
from solutions.structs.design import MyStack, MinStack, RandomPicker, MedianFinder, Codec
from solutions.structs.graphs import Dfs, Bfs, TopologicalSort
from utils import ListNode, TreeNode, Node


def main():
    pass


def _import():
    # Advanced
    DynamicProgramming()
    Greedy()
    TwoPointers()
    DivideAndConquer()
    BackTracking()

    NumArray([])
    NumMatrix([])

    # Bits
    BitManipulation()

    # Search
    BinarySearch()

    # Sort
    Sorts()

    # Design
    MyStack()
    MinStack()
    RandomPicker([])
    MedianFinder()
    Codec()

    # Graphs
    Dfs()
    Bfs()
    TopologicalSort()

    # Structs
    Array()
    HashTable()
    Heap()
    LinkedList()
    Stack()

    # Base
    Math()
    String()

    # Utils
    ListNode()
    TreeNode()
    Node()


if __name__ == '__main__':
    main()
