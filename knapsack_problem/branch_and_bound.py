from knapsack_problem import load_knapsack_dataset
import heapq

class Node:
    def __init__(self, level, value, weight, bound, items_selected):
        self.level = level
        self.value = value
        self.weight = weight
        self.bound = bound
        self.items_selected = items_selected
    def __lt__(self, other):
        return self.bound > other.bound  # Max heap behavior

def bound(node, items, capacity):
    if node.weight >= capacity:
        return 0
    profit_bound = node.value
    j = node.level
    total_weight = node.weight
    while j < len(items) and total_weight + items[j][1] <= capacity:
        total_weight += items[j][1]
        profit_bound += items[j][0]
        j += 1
    if j < len(items):
        profit_bound += (capacity - total_weight) * (items[j][0] / items[j][1])
    return profit_bound

def branch_and_bound_knapsack(file_path):
    capacity, items = load_knapsack_dataset(file_path)
    items = sorted(items, key=lambda x: x[0]/x[1], reverse=True)
    queue = []
    v = Node(0, 0, 0, 0.0, [])
    v.bound = bound(v, items, capacity)
    heapq.heappush(queue, v)

    max_value = 0
    best_items = []

    while queue:
        v = heapq.heappop(queue)
        if v.bound > max_value and v.level < len(items):
            item = items[v.level]

            # Take item
            wt = v.weight + item[1]
            val = v.value + item[0]
            selected = v.items_selected + [item]
            u = Node(v.level + 1, val, wt, 0.0, selected)

            if wt <= capacity and val > max_value:
                max_value = val
                best_items = selected

            u.bound = bound(u, items, capacity)
            if u.bound > max_value:
                heapq.heappush(queue, u)

            # Don't take item
            u = Node(v.level + 1, v.value, v.weight, 0.0, v.items_selected)
            u.bound = bound(u, items, capacity)
            if u.bound > max_value:
                heapq.heappush(queue, u)

    return max_value
