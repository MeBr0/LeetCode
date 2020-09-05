from typing import List


# noinspection PyPep8Naming,PyTypeChecker
class Solution:
    # id210 _DepthFirstSearch _BreadthFirstSearch _Graph _TopologicalSort
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Transform edge list prerequisites to adjacency list
        Store top (reversed) top sort in order
        Check whether top sort is valid or not:
        Write all appearance of elements in order to indices (not reversed)
        If there is reversed edge in graph (check index appearance) -> there is cycle, return []
        Return reversed (actual) order
        """
        adjacency_list = [[] for _ in range(2002)]

        for edge in prerequisites:
            adjacency_list[edge[1]].append(edge[0])

        visited = [False for _ in range(numCourses)]

        order = []

        for i in range(numCourses):
            if not visited[i]:
                self._findOrder(adjacency_list, visited, order, i)

        indices = [-1 for _ in range(numCourses)]

        for i in range(len(order) - 1, -1, -1):
            indices[order[i]] = numCourses - i

        for i in range(numCourses):
            for node in adjacency_list[i]:
                if indices[i] > indices[node]:
                    return []

        return reversed(order)

    def _findOrder(self, prerequisites: List[List[int]], visited: List[bool], result: List[int], i: int) -> None:
        visited[i] = True

        for node in prerequisites[i]:
            if not visited[node]:
                self._findOrder(prerequisites, visited, result, node)

        result.append(i)
