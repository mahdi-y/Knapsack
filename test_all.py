import time
from branch_and_bound import branch_and_bound_knapsack
from dynamic_programming import dynamic_programming_knapsack
from greedy import greedy_knapsack
# from human_heuristic import human_heuristic_knapsack
from profiling_utils import profile_function
import matplotlib.pyplot as plt
from genetic import genetic_knapsack


FILE = "knapsack_realistic_3000.in"

def run_test(name, func):
    print(f"Running [{name}]...")
    result, real_time, peak_memory = profile_function(func, FILE)
    print(f"[{name}]")
    print(f"  Value Achieved       : {result['value']}")
    print(f"  Weight Used / Capacity: {result['weight']} / {result['capacity']}")
    print(f"  Items Selected       : {result['items_count']}")
    print(f"  Elapsed time             : {real_time:.4f} s")
    print(f"  Peak Memory Usage    : {peak_memory:.4f} MiB")
    print("-" * 60)

    return {
    'Algorithm': name,
    'Value': result['value'],
    'Execution Time (s)': real_time,  # Now real elapsed time
    'Memory (MiB)': peak_memory,
    'Items Selected': result['items_count']
}


def annotate_bars(ax, bars, fmt="{:.0f}"):
    """Add value labels above bars."""
    for bar in bars:
        height = bar.get_height()
        ax.annotate(fmt.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # Offset above the bar
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9)

if __name__ == "__main__":
    results = []
    results.append(run_test("Greedy", greedy_knapsack))
    # results.append(run_test("Human Heuristic", human_heuristic_knapsack))
    results.append(run_test("Dynamic Programming", dynamic_programming_knapsack))
    results.append(run_test("Branch and Bound", branch_and_bound_knapsack))
    results.append(run_test("Genetic Algorithm", genetic_knapsack))


    # Extract data
    algorithms = [r['Algorithm'] for r in results]
    values = [r['Value'] for r in results]
    times = [r['Execution Time (s)'] for r in results]
    memory = [r['Memory (MiB)'] for r in results]
    items_selected = [r['Items Selected'] for r in results]

    x = range(len(algorithms))

    plt.figure(figsize=(18, 10))

    # Total Value
    ax1 = plt.subplot(2, 2, 1)
    bars1 = ax1.bar(x, values, color='skyblue')
    ax1.set_title("Total Value Achieved")
    ax1.set_xticks(x)
    ax1.set_xticklabels(algorithms, rotation=15)
    ax1.set_ylabel("Value")
    annotate_bars(ax1, bars1)

    # Execution Time
    ax2 = plt.subplot(2, 2, 2)
    bars2 = ax2.bar(x, times, color='orange')
    ax2.set_title("Elapsed Time")
    ax2.set_xticks(x)
    ax2.set_xticklabels(algorithms, rotation=15)
    ax2.set_ylabel("Time (s)")
    annotate_bars(ax2, bars2, fmt="{:.4f}")

    # Items Selected
    ax3 = plt.subplot(2, 2, 3)
    bars3 = ax3.bar(x, items_selected, color='purple')
    ax3.set_title("Number of Items Selected")
    ax3.set_xticks(x)
    ax3.set_xticklabels(algorithms, rotation=15)
    ax3.set_ylabel("Item Count")
    annotate_bars(ax3, bars3)

    # Memory Usage
    ax4 = plt.subplot(2, 2, 4)
    bars4 = ax4.bar(x, memory, color='green')
    ax4.set_title("Peak Memory Usage")
    ax4.set_xticks(x)
    ax4.set_xticklabels(algorithms, rotation=15)
    ax4.set_ylabel("Memory (MiB)")
    annotate_bars(ax4, bars4, fmt="{:.2f}")

    plt.tight_layout()
    plt.savefig("algorithm_comparison_with_items.png")
    plt.show()