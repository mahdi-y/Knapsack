import time
from branch_and_bound import branch_and_bound_knapsack
from dynamic_programming import dynamic_programming_knapsack
from greedy import greedy_knapsack
from human_heuristic import human_heuristic_knapsack

FILE = "knapsack_realistic_3000.in"

def run_test(name, func):
    start = time.time()
    result = func(FILE)
    end = time.time()
    print(f"[{name}] → Value: {result}, Time: {end - start:.4f} s")

if __name__ == "__main__":
    run_test("Greedy", greedy_knapsack)
    run_test("Human Heuristic", human_heuristic_knapsack)
    run_test("Dynamic Programming", dynamic_programming_knapsack)
    run_test("Branch and Bound", branch_and_bound_knapsack)
