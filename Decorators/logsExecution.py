def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' is being called with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' finished execution")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

# Using the function
print(add(5, 3))
