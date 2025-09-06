
def sample_decorator(func):
    def wrapper():
        print("insdide docrator")
        func()
    return wrapper

@sample_decorator
def sample_hello():
    print(" i m outside the decorator ")
sample_hello()


import time

# Define the decorator
def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Execute the original function
        end_time = time.time()  # Record end time
        print(f"Execution time of {func.__name__}: {end_time - start_time:.3f} seconds")
        return result
    return wrapper

# Use the decorator
@execution_time_decorator
def sample_function(n):
    # print(f"Processing {n} items...")
    time.sleep(3)  # Simulate a time-consuming task
    return f"Completed processing {n} items!"

# Call the decorated function
result = sample_function(5)
print(result)


