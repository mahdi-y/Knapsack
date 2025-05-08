from parser import parse_knapsack_instance
from human_heuristic import human_heuristic_knapsack
from utils import measure_time

items, capacity = parse_knapsack_instance("knapsack_varied_100000.in")
result, time_taken = measure_time(human_heuristic_knapsack, items, capacity)

print("[Human Heuristic Results]")
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
