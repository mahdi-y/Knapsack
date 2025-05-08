def parse_knapsack_instance(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    # The first line is the knapsack capacity
    capacity = int(lines[0].strip())
    items = []

    # Parse each item starting from the second line
    for idx, line in enumerate(lines[1:]):
        try:
            # Unpack three values: index, value, weight
            index, value, weight = map(int, line.strip().split())
            items.append((value, weight, index))  # Correct order: value, weight, index
        except ValueError:
            # Handle lines with incorrect number of values (not exactly 3)
            print(f"Skipping invalid line {idx + 2}: {line.strip()}")
            continue

    return items, capacity
