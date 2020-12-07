from typing import List


# noinspection PyPep8Naming,PyTypeChecker,PyMethodMayBeStatic
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

        def visit(k: int) -> None:
            visited[k] = True

            for neighbour in adjacency_list[k]:
                if not visited[neighbour]:
                    visit(neighbour)

            order.append(k)

        for i in range(numCourses):
            if not visited[i]:
                visit(i)

        indices = [-1 for _ in range(numCourses)]

        for i in range(len(order) - 1, -1, -1):
            indices[order[i]] = numCourses - i

        for i in range(numCourses):
            for node in adjacency_list[i]:
                if indices[i] > indices[node]:
                    return []

        return reversed(order)
