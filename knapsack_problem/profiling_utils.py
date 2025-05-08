import time
from memory_profiler import memory_usage

def profile_function(func, *args, **kwargs):
    """
    Profiles a function's execution time and memory usage.
    Returns (result, real_time, peak_memory)
    """
    def wrapped():
        return func(*args, **kwargs)

    # Measure real elapsed (wall-clock) time
    start = time.time()
    mem_usage, result = memory_usage(wrapped, max_iterations=1, retval=True)
    end = time.time()

    real_time = end - start
    peak_memory = max(mem_usage) - min(mem_usage)  # Net increase in memory
    return result, real_time, peak_memory