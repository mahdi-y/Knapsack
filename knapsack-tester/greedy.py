from collections import Counter

def greedy_knapsack(items, capacity):
    # items: list of (value, weight, index)
    items_sorted = sorted(items, key=lambda x: x[0]/x[1], reverse=True)

    total_value = 0
    total_weight = 0
    selected_items = []

    # Track selected items to avoid duplicates
    seen_indices = set()

    for value, weight, index in items_sorted:
        if index in seen_indices:
            continue
        if total_weight + weight <= capacity:
            total_weight += weight
            total_value += value
            selected_items.append((index, value, weight))
            seen_indices.add(index)

    # Full stats
    all_values = sum(item[0] for item in items)
    all_weights = sum(item[1] for item in items)

    result = {
        "total_value_selected": total_value,
        "total_weight_selected": total_weight,
        "capacity": capacity,
        "items_selected": selected_items,
        "count_selected": len(selected_items),
        "total_items_available": len(items),
        "total_value_available": all_values,
        "total_weight_available": all_weights
    }

    return result