def human_heuristic_knapsack(items, capacity):
    total_value = 0
    total_weight = 0
    selected_items = []

    for value, weight, index in items:
        if total_weight + weight <= capacity:
            total_weight += weight
            total_value += value
            selected_items.append((index, value, weight))

    result = {
        "total_value_selected": total_value,
        "total_weight_selected": total_weight,
        "capacity": capacity,
        "items_selected": selected_items,
        "count_selected": len(selected_items),
        "total_items_available": len(items),
        "total_value_available": sum(i[0] for i in items),
        "total_weight_available": sum(i[1] for i in items)
    }
    return result
