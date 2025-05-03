import random

def calculate_fitness(individual):
    """
    Calculates the number of non-attacking queen pairs.
    Fitness is negative of conflict count (the higher, the better).
    """
    conflicts = 0
    n = len(individual)
    for i in range(n):
        for j in range(i + 1, n):
            if individual[i] == individual[j] or abs(individual[i] - individual[j]) == abs(i - j):
                conflicts += 1
    return -conflicts

def create_individual(n):
    """Generate a random individual with N genes (columns for each queen row)."""
    return [random.randint(0, n - 1) for _ in range(n)]

def initialize_population(n, size):
    """Initialize a population of given size."""
    return [(create_individual(n), 0) for _ in range(size)]

def tournament_selection(population, k=5):
    """Select one parent using tournament selection."""
    contenders = random.sample(population, k)
    return max(contenders, key=lambda ind: ind[1])[0]

def single_point_crossover(parent1, parent2):
    """Single-point crossover between two parents."""
    point = random.randint(1, len(parent1) - 2)
    return parent1[:point] + parent2[point:]

def mutate(individual, mutation_rate):
    """Randomly mutate one gene in the individual."""
    if random.random() < mutation_rate:
        index = random.randint(0, len(individual) - 1)
        individual[index] = random.randint(0, len(individual) - 1)

def genetic_algorithm(n, population_size, mutation_rate, max_generations):
    """Main loop for the Genetic Algorithm."""
    population = initialize_population(n, population_size)

    for generation in range(max_generations):
    
        population = [(ind, calculate_fitness(ind)) for ind, _ in population]
        population.sort(key=lambda x: x[1], reverse=True)

        if population[0][1] == 0:
            return population[0][0], generation

        new_generation = [population[0]]

        while len(new_generation) < population_size:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child = single_point_crossover(parent1, parent2)
            mutate(child, mutation_rate)
            new_generation.append((child, 0))  

        population = new_generation

    return None, max_generations

if __name__ == "__main__":
    n = int(input("Enter the number of queens (N): "))
    population_size = int(input("Enter the population size: "))
    mutation_rate = float(input("Enter the mutation rate (e.g. 0.05): "))
    max_generations = int(input("Enter the maximum number of generations: "))

    solution, generations = genetic_algorithm(n, population_size, mutation_rate, max_generations)

    if solution:
        print("\nSolution found!")
        print(f"Generations taken: {generations}")
        print(f"Board configuration (column positions per row): {solution}")
    else:
        print("\nNo solution was found within the given number of generations.")
