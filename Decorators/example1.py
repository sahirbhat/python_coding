def sample_decorator(func):
    def wrapper(a,b):
        print(" i m inside decorator",a,b)
        func(a,b)
        return a+b
        print(" function is finished here")
    return wrapper    

       
        


@sample_decorator
def sample(a,b):
    print("hello i m function")




sum=sample(22,56)
print(sum)