from knapsack_problem import load_knapsack_dataset

def human_heuristic_knapsack(file_path):
    capacity, items = load_knapsack_dataset(file_path)

    total_value = 0
    total_weight = 0
    for value, weight, _ in items:
        if total_weight + weight <= capacity:
            total_weight += weight
            total_value += value

    return total_value
