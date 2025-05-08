import random

def generate_conflicting_knapsack_dataset(
    filename,
    target_capacity=100000,
    num_items=3000,
    seed=42
):
    random.seed(seed)
    items = []

    # Category 1: High value, high weight (low value/weight)
    for _ in range(num_items // 3):
        value = random.randint(80, 100)
        weight = random.randint(80, 100)
        items.append((value, weight))

    # Category 2: Low value, low weight (moderate value/weight)
    for _ in range(num_items // 3):
        value = random.randint(10, 30)
        weight = random.randint(1, 10)
        items.append((value, weight))

    # Category 3: Medium everything (confusing heuristics)
    for _ in range(num_items // 3):
        value = random.randint(40, 70)
        weight = random.randint(20, 60)
        items.append((value, weight))

    # Now shuffle
    random.shuffle(items)

    # Assign indices and calculate total weight
    indexed_items = [(idx, val, wt) for idx, (val, wt) in enumerate(items)]
    total_weight = sum(w for _, _, w in indexed_items)
    total_value = sum(v for _, v, _ in indexed_items)

    with open(filename, 'w') as f:
        f.write(f"{target_capacity}\n")
        for idx, value, weight in indexed_items:
            f.write(f"{idx} {value} {weight}\n")

    print(f"Dataset generated: {filename}")
    print(f"Total items: {len(items)}")
    print(f"Total value: {total_value}")
    print(f"Total weight: {total_weight}")
    print(f"Knapsack capacity: {target_capacity}")
    print(f"Total weight vs capacity ratio: {total_weight / target_capacity:.2f}")

# Example
generate_conflicting_knapsack_dataset("knapsack_conflict_100000.in")
