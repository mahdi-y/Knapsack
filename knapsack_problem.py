def load_knapsack_dataset(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().strip().split('\n')
        capacity = int(lines[0])
        items = []
        for line in lines[1:]:
            idx, value, weight = map(int, line.strip().split())
            items.append((value, weight, idx))  # (value, weight, index)
        return capacity, items

