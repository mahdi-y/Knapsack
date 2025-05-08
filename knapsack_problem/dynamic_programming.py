from knapsack_problem import load_knapsack_dataset

def dynamic_programming_knapsack(file_path):
    capacity, items = load_knapsack_dataset(file_path)
    n = len(items)
    dp = [0] * (capacity + 1)

    for value, weight, _ in items:
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)

    return dp[capacity]
