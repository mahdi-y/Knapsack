import matplotlib.pyplot as plt
from parser import parse_knapsack_instance  # Add this import
from greedy import greedy_knapsack
from utils import measure_time

# Parse the knapsack instance
items, capacity = parse_knapsack_instance("knapsack_varied_100000.in")

# Measure execution time of greedy_knapsack
result, time_taken = measure_time(greedy_knapsack, items, capacity)

# Output the results
print("[Greedy Algorithm Results]")
print(f"→ Knapsack Capacity         : {result['capacity']}")
print(f"→ Total Items Available     : {result['total_items_available']}")
print(f"→ Total Value (All Items)   : {result['total_value_available']}")
print(f"→ Total Weight (All Items)  : {result['total_weight_available']}")

print(f"\n→ Items Selected            : {result['count_selected']}")
print(f"→ Total Value Selected      : {result['total_value_selected']}")
print(f"→ Total Weight Selected     : {result['total_weight_selected']} / {result['capacity']}")

# print(f"\n→ Selected Items (index, value, weight):")
# for idx, val, wt in sorted(result['items_selected']):
#     print(f"   - Item {idx}: value={val}, weight={wt}")

print(f"\n→ Execution Time            : {time_taken:.6f} seconds")

# Graphical Output
# 1. Bar chart for selected items' value vs weight
selected_items = result['items_selected']
indices = [item[0] for item in selected_items]
values = [item[1] for item in selected_items]
weights = [item[2] for item in selected_items]

# Create the figure and axis
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Plot Value vs Weight for Selected Items
ax[0].bar(indices, values, label="Value", alpha=0.6, color='b')
ax[0].bar(indices, weights, label="Weight", alpha=0.6, color='r')
ax[0].set_title("Selected Items: Value vs Weight")
ax[0].set_xlabel("Item Index")
ax[0].set_ylabel("Value / Weight")
ax[0].legend()

# Plot Value vs Weight vs Capacity (scatter plot)
ax[1].scatter(weights, values, color='g', alpha=0.6)
ax[1].set_title("Selected Items: Weight vs Value")
ax[1].set_xlabel("Weight")
ax[1].set_ylabel("Value")
ax[1].plot([0, result['capacity']], [0, result['capacity']], 'k--', label="Capacity line")
ax[1].legend()

# Show the plot
plt.tight_layout()
plt.show()
