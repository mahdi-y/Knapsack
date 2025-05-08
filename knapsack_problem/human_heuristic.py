from knapsack_problem import load_knapsack_dataset

def human_heuristic_knapsack(file_path):
    capacity, items = load_knapsack_dataset(file_path)

    total_value = 0
    total_weight = 0
    selected_items = []

    for value, weight, _ in items:
        if total_weight + weight <= capacity:
            total_weight += weight
            total_value += value
            selected_items.append((value, weight))

    total_weight = sum(item[1] for item in selected_items)
    return {
    'value': total_value,
    'weight': total_weight,
    'items_count': len(selected_items),
    'capacity': capacity,
    'items': selected_items
}
