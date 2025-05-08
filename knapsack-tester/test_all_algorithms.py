import time
from greedy import greedy_knapsack
from dynamic_programming import dynamic_programming_knapsack
from branch_and_bound import branch_and_bound_knapsack
from human_heuristic import human_heuristic_knapsack

def load_dataset(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    capacity = int(lines[0])
    items = []
    for line in lines[1:]:
        index, value, weight = map(int, line.strip().split())
        items.append((value, weight, index))
    return items, capacity

def run_and_print(name, func, items, capacity):
    start = time.time()
    result = func(items, capacity)
    end = time.time()

    print(f"[{name} Results]")
    print(f"→ Knapsack Capacity         : {result['capacity']}")
    print(f"→ Total Items Available     : {result['total_items_available']}")
    print(f"→ Total Value (All Items)   : {result['total_value_available']}")
    print(f"→ Total Weight (All Items)  : {result['total_weight_available']}\n")

    print(f"→ Items Selected            : {result['count_selected']}")
    print(f"→ Total Value Selected      : {result['total_value_selected']}")
    print(f"→ Total Weight Selected     : {result['total_weight_selected']} / {result['capacity']}\n")

    print(f"→ Execution Time            : {end - start:.6f} seconds")
    print("-" * 60 + "\n")

def main():
    filename = "knapsack_conflict_100000.in"  # or whichever file you want
    items, capacity = load_dataset(filename)

    run_and_print("Greedy Algorithm", greedy_knapsack, items, capacity)
    run_and_print("Dynamic Programming", dynamic_programming_knapsack, items, capacity)
    run_and_print("Branch and Bound", branch_and_bound_knapsack, items, capacity)
    run_and_print("Human Heuristic", human_heuristic_knapsack, items, capacity)

if __name__ == "__main__":
    main()
