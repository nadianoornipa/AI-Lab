import random


matrix = [[random.randint(1,99) for _ in range(5)] for _ in range(5)]

row_sums = [sum(row) for row in matrix]

print("Matrix:")
for row in matrix:
    print(row)
print("Row-wise sums:", row_sums)


