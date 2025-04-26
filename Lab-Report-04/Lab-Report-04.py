import random

# Step 1: Generate random points and centers
points = {f"P{i:02d}": (random.randint(0, 19), random.randint(0, 19)) for i in range(100)}
centers = {f"C{i}": (random.randint(0, 19), random.randint(0, 19)) for i in range(10)}

# Step 2: Print Generated Points in a Table
print("\nGenerated Points ")
print(f"{'Point':<6} {'X':<3} {'Y':<3}")
print("-" * 20)
for pname, (x, y) in points.items():
    print(f"{pname:<6} {x:<3} {y:<3}")
print("\n")

# Step 3: Print Initial Cluster Centers
print("\nInitial Cluster Centers ")
print(f"{'Center':<6} {'X':<3} {'Y':<3}")
print("-" * 20)
for cname, (x, y) in centers.items():
    print(f"{cname:<6} {x:<3} {y:<3}")
print("\n")

# Step 4: Manhattan distance function
def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# Step 5: Assign each point to the nearest center
assignments = {}
for pname, pcoord in points.items():
    min_dist = float('inf')
    nearest_center = None
    for cname, ccoord in centers.items():
        d = manhattan(pcoord, ccoord)
        if d < min_dist:
            min_dist = d
            nearest_center = cname
    assignments[pname] = nearest_center

# Step 6: Recalculate centers (average of assigned points)
new_centers = {}
for cname in centers.keys():
    assigned_points = [pcoord for pname, pcoord in points.items() if assignments[pname] == cname]
    if assigned_points:
        avg_x = sum(x for x, y in assigned_points) // len(assigned_points)
        avg_y = sum(y for x, y in assigned_points) // len(assigned_points)
        new_centers[cname] = (avg_x, avg_y)
    else:
        new_centers[cname] = centers[cname]

centers = new_centers

# Step 7: Create a 20x20 grid
grid = [[" ." for _ in range(20)] for _ in range(20)]

# Different cluster symbols (A, B, C, etc.)
cluster_symbols = {f"C{i}": chr(65 + i) for i in range(10)}  # A-J

# Place points
for pname, (px, py) in points.items():
    assigned_center = assignments[pname]
    symbol = cluster_symbols[assigned_center]
    if 0 <= px < 20 and 0 <= py < 20:
        grid[py][px] = f" {symbol}"

# Place centers with special symbol '#'
for cname, (cx, cy) in centers.items():
    if 0 <= cx < 20 and 0 <= cy < 20:
        grid[cy][cx] = " #"

# Step 8: Print the final visualization
print("Final Clustered Map (Y axis from Top 19 -> Bottom 0) :\n")
print("    " + " ".join(f"{i:02d}" for i in range(20)))  # X-axis labels
for y in range(19, -1, -1):
    print(f"{y:02d} " + " ".join(grid[y]))

# Step 9: Print cluster symbol key

print("\n# : Cluster Center (after recalculation)")
for cname, symbol in cluster_symbols.items():
    print(f"{symbol}: Points assigned to {cname}")
