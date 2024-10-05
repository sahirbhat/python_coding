# import time
# from functools import wraps
# def mysample_decor(func):
#     def wrapper():
#         print(" im inside decorator")
#         func()
#         print(" i m inside doc but after function executio")
#     return wrapper
# @mysample_decor
# def say_hello():
#     print("hello i m simple function")

# say_hello() 


    


# # def simple_decor(func):
# #     def wrapper():
# #         print("this is function before")
# #         func()
# #         print("this is after functim")
# #     return wrapper


# # @simple_decor
# # def sample_hello():
# #     print("hello")



# # sample_hello()    # Call the function


def sample_decorator(func):
    def wrapper():
        print(" i m inside decorator function")
        func()
        # print("i m inside dec after calll function")
    return wrapper    



@sample_decorator
def say_hello():
    print("hello i m func with decorator")

say_hello()  








