import random


array = [random.random() for _ in range(100)]


min_val = min(array)
max_val = max(array)
normalized_array = [(x - min_val) / (max_val - min_val) for x in array]

print(normalized_array)
