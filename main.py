from solutions.advanced import DynamicProgramming, Greedy, TwoPointers, NumArray, NumMatrix, DivideAndConquer
from solutions.base import Math, String, Array
from solutions.bits import BitManipulation
from solutions.design import MyStack, MinStack, RandomPicker, MedianFinder
from solutions.lists import LinkedList, Stack
from solutions.maps import HashTable
from solutions.search import BinarySearch
from solutions.sort import Sorts
from solutions.trees import Dfs, Bfs
from utils import ListNode, TreeNode


def main():
    print(TwoPointers().moveZeroes([0,1,0,3,12]))


def _import():
    # Advanced
    DynamicProgramming()
    Greedy()
    TwoPointers()
    DivideAndConquer()
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

    # Utils
    ListNode()
    TreeNode()


if __name__ == '__main__':
    main()
