from solutions import Math, String, TwoPointers
from solutions.bits import BitManipulation
from solutions.design import MyStack, MinStack
from solutions.lists import Array, LinkedList, Stack
from solutions.maps import HashTable
from solutions.search import BinarySearch
from solutions.trees import Dfs, Bfs
from utils import ListNode, TreeNode


def main():
    print(Array().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


def _import():
    BitManipulation()
    MyStack()
    MinStack()
    HashTable()
    Array()
    LinkedList()
    Stack()
    BinarySearch()
    Dfs()
    Bfs()
    Math()
    String()
    TwoPointers()
    ListNode()
    TreeNode()


if __name__ == '__main__':
    main()
