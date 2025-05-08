from knapsack_problem import load_knapsack_dataset

def greedy_knapsack(file_path):
    capacity, items = load_knapsack_dataset(file_path)
    items = sorted(items, key=lambda x: x[0]/x[1], reverse=True)

    total_value = 0
    total_weight = 0
    for value, weight, _ in items:
        if total_weight + weight <= capacity:
            total_weight += weight
            total_value += value

    return total_value
