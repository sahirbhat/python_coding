import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds to execute")
        return result
    return wrapper

@timing_decorator
def slow_function(seconds):
    time.sleep(seconds)
    print("Function finished")

# Using the function
slow_function(2)
