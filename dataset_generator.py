import random

def generate_realistic_knapsack_dataset(
    num_items=3000,
    max_value=100,
    max_weight=100,
    capacity_ratio=0.3,
    output_file="knapsack_realistic_3000.in"
):
    """
    Generates a realistic knapsack dataset.
    
    Parameters:
    - num_items: Number of items to generate.
    - max_value: Maximum value for an item.
    - max_weight: Maximum weight for an item.
    - capacity_ratio: Capacity as a ratio of total weight.
    - output_file: File to save the dataset.
    """
    items = []
    total_weight = 0

    for i in range(num_items):
        value = random.randint(max_value // 2, max_value)     # Higher average value
        weight = random.randint(1, max_weight)                # Keep some small weights
        items.append((i, value, weight))
        total_weight += weight

    capacity = int(total_weight * capacity_ratio)

    with open(output_file, "w") as f:
        f.write(f"{capacity}\n")
        for idx, value, weight in items:
            f.write(f"{idx} {value} {weight}\n")

    print(f"✅ Dataset generated: {output_file}")
    print(f"📦 Items: {num_items}")
    print(f"🪶 Total weight: {total_weight}")
    print(f"🎯 Capacity: {capacity} (≈{capacity_ratio*100:.0f}%)")

if __name__ == "__main__":
    generate_realistic_knapsack_dataset()
