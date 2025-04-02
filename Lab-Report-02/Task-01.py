def iddfs(maze, start, target, max_depth):
    def dls(node, depth, path, visited):
        if depth < 0:
            return False
        x, y = node
        if node == target:
            path.append(node)
            return True
        visited.add(node)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and (nx, ny) not in visited and maze[nx][ny] == 0:
                if dls((nx, ny), depth - 1, path, visited):
                    path.append(node)
                    return True
        return False
    for depth in range(max_depth + 1):
        path = []
        visited = set()
        if dls(start, depth, path, visited):
            print(f"Path found at depth {depth} using IDDFS")
            print("Traversal Order:", path[::-1])
            return
    
    print(f"Path not found at max depth {max_depth} using IDDFS")


def parse_input():
    import sys
    
    rows, cols = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(rows)]
    
    start_x, start_y = map(int, input().split()[1:])
    target_x, target_y = map(int, input().split()[1:])
    
    iddfs(maze, (start_x, start_y), (target_x, target_y), rows * cols)
parse_input()
