from knapsack_problem import load_knapsack_dataset

def dynamic_programming_knapsack(file_path):
    capacity, items = load_knapsack_dataset(file_path)
    n = len(items)
    dp = [0] * (capacity + 1)
    selected_items = []

    # Dynamic programming to calculate max value
    for value, weight, _ in items:
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)

    # Backtrack to find selected items
    w = capacity
    for i in range(n - 1, -1, -1):
        # Ensure the check doesn't go out of range for dp[]
        if w - items[i][1] >= 0 and dp[w] != dp[w - items[i][1]] + items[i][0]:
            selected_items.append(items[i])
            w -= items[i][1]

    total_weight = sum(item[1] for item in selected_items)
    return {
    'value': dp[capacity],
    'weight': total_weight,
    'items_count': len(selected_items),
    'capacity': capacity,
    'items': selected_items
}
