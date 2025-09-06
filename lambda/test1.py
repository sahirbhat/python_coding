



weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
# output: [[‘wed’, 1], [‘sun’, 2], [‘thu’, 1], [‘tue’, 1], [‘mon’, 3], [‘fri’, 1]]

d={}

for days in weekdays:
    if days in d:
        d[days]+=1
    else:
        d[days] =1
print(d)    

def sample_deco(func):
    def wrapper():
        print(" i m inside deco")
        func()
        print("back to deco")
    return wrapper    


@sample_deco
def sample_hello() :
    print("helllo i m using decorator")  
 
sample_hello()


def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

# Using the decorator
@log_execution
def add_numbers(a, b):
    return a + b

# @log_execution
# def greet_person(name, greeting="Hello"):
#     return f"{greeting}, {name}!"

# Test the decorated functions
sum_result = add_numbers(10, 20)
# greeting_message = greet_person("Sahir", greeting="Hi")
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the original function
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time  # Calculate elapsed time
        print(f"{func.__name__} took {elapsed_time:.4f} seconds to execute.")
        return result
    return wrapper

# Using the decorator
@measure_time
def sample_function(n):
    time.sleep(n)  # Simulate a function that takes time
    return f"Function slept for {n} seconds"

# Test the decorated function
result = sample_function(2)
print(result)
