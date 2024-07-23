
#bfs
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.visited = []

    def BFS(self, start, goal):
        queue = []
        queue.append(start)
        self.visited.append(start)
        while queue:
            current = queue.pop(0)
            print(current, end=" ")

            if current == goal:
                print("\nGoal state reached!")
                return

            for neighbor in self.graph[current]:
                if neighbor not in self.visited:
                    queue.append(neighbor)
                    self.visited.append(neighbor)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

start_state = 0
goal_state = 3

print(f"Following is Breadth First Traversal (starting from vertex {start_state} to reach goal state {goal_state}):")
g.BFS(start_state, goal_state)
