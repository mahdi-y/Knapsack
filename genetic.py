import random
from knapsack_problem import load_knapsack_dataset

def fitness(individual, items, capacity):
    total_value = total_weight = 0
    for gene, (value, weight, _) in zip(individual, items):
        if gene:
            total_value += value
            total_weight += weight
    return total_value if total_weight <= capacity else 0

def create_individual(n):
    return [random.randint(0, 1) for _ in range(n)]

def two_point_crossover(parent1, parent2):
    if len(parent1) < 2:
        return parent1  # fallback
    pt1, pt2 = sorted(random.sample(range(len(parent1)), 2))
    return parent1[:pt1] + parent2[pt1:pt2] + parent1[pt2:]

def mutate(individual, mutation_rate):
    return [1 - gene if random.random() < mutation_rate else gene for gene in individual]

def select(population, fitnesses, k=5):
    selected = random.sample(list(zip(population, fitnesses)), k)
    return max(selected, key=lambda x: x[1])[0]

def repair(individual, items, capacity):
    # Remove items until within capacity, using value/weight ratio
    total_weight = sum(weight for gene, (_, weight, _) in zip(individual, items) if gene)
    if total_weight <= capacity:
        return individual

    item_indices = [i for i, gene in enumerate(individual) if gene]
    # Sort by lowest value-to-weight ratio
    item_indices.sort(key=lambda i: items[i][0] / items[i][1])

    for i in item_indices:
        individual[i] = 0
        total_weight -= items[i][1]
        if total_weight <= capacity:
            break

    return individual

def genetic_knapsack(file_path, population_size=300, generations=500, base_mutation=0.01, stagnation_threshold=30):
    capacity, items = load_knapsack_dataset(file_path)
    n = len(items)

    population = [create_individual(n) for _ in range(population_size)]
    fitnesses = [fitness(ind, items, capacity) for ind in population]

    best_fitness = max(fitnesses)
    best_individual = population[fitnesses.index(best_fitness)]
    stagnant_generations = 0
    mutation_rate = base_mutation

    for _ in range(generations):
        new_population = []

        for _ in range(population_size):
            parent1 = select(population, fitnesses, k=5)
            parent2 = select(population, fitnesses, k=5)
            child = two_point_crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            child = repair(child, items, capacity)
            new_population.append(child)

        population = new_population
        fitnesses = [fitness(ind, items, capacity) for ind in population]
        gen_best = max(fitnesses)

        if gen_best > best_fitness:
            best_fitness = gen_best
            best_individual = population[fitnesses.index(gen_best)]
            stagnant_generations = 0
            mutation_rate = base_mutation  # reset
        else:
            stagnant_generations += 1
            if stagnant_generations > stagnation_threshold:
                mutation_rate = min(0.1, mutation_rate * 1.5)  # increase mutation
                stagnant_generations = 0  # reset stagnation

    # Extract results
    selected_items = []
    total_value = total_weight = 0
    for i, gene in enumerate(best_individual):
        if gene:
            value, weight, _ = items[i]
            selected_items.append((value, weight))
            total_value += value
            total_weight += weight

    return {
        'value': total_value,
        'weight': total_weight,
        'items_count': len(selected_items),
        'capacity': capacity,
        'items': selected_items
    }
