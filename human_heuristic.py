import random

def fitness(individual, items, capacity):
    total_value = total_weight = 0
    for gene, (value, weight, _) in zip(individual, items):
        if gene:
            total_value += value
            total_weight += weight
    return total_value if total_weight <= capacity else 0

def create_individual(n):
    return [random.randint(0, 1) for _ in range(n)]

def mutate(individual, mutation_rate=0.01):
    return [1 - gene if random.random() < mutation_rate else gene for gene in individual]

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:]

def select(population, fitnesses, k=3):
    selected = random.sample(list(zip(population, fitnesses)), k)
    return max(selected, key=lambda x: x[1])[0]

def genetic_knapsack(items, capacity, population_size=100, generations=100, mutation_rate=0.01):
    n = len(items)
    population = [create_individual(n) for _ in range(population_size)]

    best_individual = None
    best_fitness = 0

    for _ in range(generations):
        fitnesses = [fitness(ind, items, capacity) for ind in population]
        for ind, fit in zip(population, fitnesses):
            if fit > best_fitness:
                best_individual = ind
                best_fitness = fit

        new_population = []
        for _ in range(population_size):
            parent1 = select(population, fitnesses)
            parent2 = select(population, fitnesses)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

    # Extract selected items
    selected_items = []
    total_value = total_weight = 0
    for i, gene in enumerate(best_individual):
        if gene:
            value, weight, index = items[i]
            selected_items.append((index, value, weight))
            total_value += value
            total_weight += weight

    return {
        'items_selected': selected_items,
        'total_value_selected': total_value,
        'total_weight_selected': total_weight,
        'capacity': capacity,
        'count_selected': len(selected_items),
        'total_items_available': len(items),
        'total_value_available': sum(i[0] for i in items),
        'total_weight_available': sum(i[1] for i in items),
    }
