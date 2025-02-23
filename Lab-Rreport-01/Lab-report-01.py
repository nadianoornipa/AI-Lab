import random

class Node:
    def __init__(self, x, y, depth=0):
        self.x, self.y, self.depth = x, y, depth
    def __repr__(self):
        return f"({self.x},{self.y})"

def generate_grid():
    N = random.randint(4, 7)
    grid = [[1 if random.random() < 0.7 else 0 for _ in range(N)] for _ in range(N)]
    free = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == 1]
    if len(free) < 2:
        grid[0][0] = grid[N-1][N-1] = 1
        return grid, Node(0, 0), Node(N-1, N-1), N
    src, goal = random.sample(free, 2)
    return grid, Node(src[0], src[1]), Node(goal[0], goal[1]), N

def print_grid(grid, source, goal):
    print("Grid:")
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == source.x and j == source.y:
                print("S", end=" ")
            elif i == goal.x and j == goal.y:
                print("G", end=" ")
            else:
                print(grid[i][j], end=" ")
        print()
    print()

def dfs(grid, node, goal, N, dfs_order, path):
    grid[node.x][node.y] = 0  # mark as visited
    dfs_order.append((node.x, node.y))
    path.append((node.x, node.y))
    if (node.x, node.y) == (goal.x, goal.y):
        return True
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = node.x + dx, node.y + dy
        if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 1:
            if dfs(grid, Node(nx, ny, node.depth+1), goal, N, dfs_order, path):
                return True
    path.pop()
    return False

def main():
    grid, source, goal, N = generate_grid()
    print_grid(grid, source, goal)
    print(f"Source: {source}\nGoal: {goal}\n")
    grid_copy = [row[:] for row in grid]
    dfs_order, path = [], []
    if dfs(grid_copy, source, goal, N, dfs_order, path):
        print("Goal found!")
        print("DFS Path:", " -> ".join(map(str, path)))
        print("Number of moves =", len(path) - 1)
    else:
        print("Goal cannot be reached from the starting block")
    print("\nDFS Order:", " -> ".join(map(str, dfs_order)))

if __name__ == "__main__":
    main()
