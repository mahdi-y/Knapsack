import time

def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    duration = end - start
    return result, duration
