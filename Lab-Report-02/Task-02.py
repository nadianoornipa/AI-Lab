def is_safe(node, graph, color, c):
    for neighbor in graph[node]:
        if color[neighbor] == c:
            return False
    return True
def graph_coloring(graph, m, color, node, n):
    if node == n:
        return True 
    for c in range(1, m + 1):
        if is_safe(node, graph, color, c):
            color[node] = c
            if graph_coloring(graph, m, color, node + 1, n):
                return True
            color[node] = 0
    return False
def solve_coloring_problem():
    n, m, k = map(int, input().split())
    graph = {i: [] for i in range(n)}
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    color = [0] * n
    if graph_coloring(graph, k, color, 0, n):
        print(f"Coloring Possible with {k} Colors")
        print("Color Assignment:", color)
    else:
        print(f"Coloring Not Possible with {k} Colors")
solve_coloring_problem()
