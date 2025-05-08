def dynamic_programming_knapsack(items, capacity):
    n = len(items)
    dp = [0] * (capacity + 1)
    keep = [[False] * (capacity + 1) for _ in range(n)]

    for i in range(n):
        value, weight, _ = items[i]
        for w in range(capacity, weight - 1, -1):
            if dp[w - weight] + value > dp[w]:
                dp[w] = dp[w - weight] + value
                keep[i][w] = True

    # Reconstruct solution
    w = capacity
    total_weight = 0
    selected_items = []
    for i in reversed(range(n)):
        if keep[i][w]:
            value, weight, index = items[i]
            selected_items.append((index, value, weight))
            total_weight += weight
            w -= weight

    total_value = dp[capacity]
    result = {
        "total_value_selected": total_value,
        "total_weight_selected": total_weight,
        "capacity": capacity,
        "items_selected": selected_items,
        "count_selected": len(selected_items),
        "total_items_available": n,
        "total_value_available": sum(i[0] for i in items),
        "total_weight_available": sum(i[1] for i in items)
    }
    return result
