import random

target = int(input("Enter Target Sum (T): "))
length = int(input("Enter List Length (k): "))

pop_size = 10
max_gen = 100

def generate_ind():
    return [random.randint(0, 9) for _ in range(length)]

def fitness(ind):
    return abs(target - sum(ind))

def mutation(ind):
    id = random.randint(0, length-1)
    ind[id] = random.randint(0, 9)
    return ind

initial_pop = [generate_ind() for _ in range(pop_size)]

for gen in range(max_gen):
    initial_pop.sort(key=fitness)

    if fitness(initial_pop[0]) == 0:
        break

    elites = initial_pop[:pop_size // 2]

    new_generation = []
    while len(new_generation) < pop_size - len(elites):
        parent = random.choice(elites)
        offspring = mutation(parent.copy())
        new_generation.append(offspring)

    initial_pop = elites + new_generation

print(*initial_pop[0])
