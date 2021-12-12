from AoCInputReader import AoCInputReader
from collections import defaultdict, deque

class Solution(AoCInputReader):
    def __init__(self):
        # Create an adjacency list for our (somewhat directed?) graph.
        # Nodes are not allowed to point to 'start' (start is directed outward only).
        # 'end' is not allowed to point to any other nodes (end is directed inward only).
        self.graph = defaultdict(list)
        for line in self._data:
            node_1 = line.split("-")[0]
            node_2 = line.split("-")[1]
            if node_1 != 'end' and node_2 != 'start':
                self.graph[node_1].append(node_2)
            if node_2 != 'end' and node_1 != 'start':
                self.graph[node_2].append(node_1)

    def solve_part_1(self):
        paths = []

        def checkPaths(path):
            """
            Recursive backtracking. Base cases are when we have reached the 'end', or we have
            already visited a small cave in which case the path is invalid.
            """
            current_node = path[-1]
            if current_node == 'end':
                paths.append(path.copy())
                return

            if current_node.islower() and path.count(current_node) >=2:
                return

            for destination in self.graph[current_node]:
                path.append(destination)
                checkPaths(path)
                path.pop()

        checkPaths(["start"])
        return len(paths)

    def solve_part_2(self):
        """
        Iterative approach using a stack, to avoid recursive stack overflow.
        """
        paths = []
        stack = deque([['start']])

        while stack:
            path = stack.pop()
            current_node = path[-1]

            if current_node == 'end':
                paths.append(path.copy())
                continue

            # We are allowed to visit a single small cave (lowercase label) twice for any path.
            # If we find that we have visited a single small cave > 2 times, or we have visited
            # more than 1 small cave 2 times, this path is invalid.
            if current_node.islower() and current_node != 'start':
                visited_twice = set()
                visited_thrice = set()
                for node in path:
                    if node.islower():
                        if path.count(node) > 2:
                            visited_thrice.add(node)
                        elif path.count(node) == 2:
                            visited_twice.add(node)

                if len(visited_twice) > 1 or len(visited_thrice) > 0:
                    continue

            for destination in self.graph[current_node]:
                path.append(destination)
                stack.append(path.copy())
                path.pop()

        return len(paths)


if __name__ == "__main__":
    solution = Solution()
    solution.read_input("input12.txt", "string")
    solution.print_answers(12, 4792, 133360)
