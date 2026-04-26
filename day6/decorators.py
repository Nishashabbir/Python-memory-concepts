
# They are basically functions that take another function and return a new function with added behavior.


# def decorator(func):
#     def wrapper():
#         print("before ")
#         func()
#         print("after")
#     return wrapper

# @decorator
# def func():
#     print("Hello I am here ")

# # until you call this function , there is no ouput 
# func()


# it is same as 
# What @decorator means
# # This:
# @decorator
# def say_hello():
# # is the same as:
# def say_hello():
#     print("Hello!")

# say_hello = decorator(say_hello)


# import time 

# def timer(func):
#     def wrapper(*args , **kwargs):
#         start = time.time() 
#         result=func(*args , **kwargs)
#         end=time.time()
#         print(f"the time taken is : {end-start}s")
#         return result 
#     return wrapper

# @timer
# def work():
#     time.sleep(1)
#     print("the work is done ")

# this is same calling like this :work = timer(work)
# work()

# func is the original work function
# *args, **kwargs?
# it’s for safety/flexibility.
# Even though work() currently takes no arguments, the decorator is written generically so it would still work if you later did:

# @timer
# def add(a, b):
#     return a + b


# you can use multiple decoratos on a function 


# def decorator_a(func):
#     def wrapper(*args, **kwargs):
#         print("A before")
#         result = func(*args, **kwargs)
#         print("A after")
#         return result
#     return wrapper


# def decorator_b(func):
#     def wrapper(*args, **kwargs):
#         print("B before")
#         result = func(*args, **kwargs)
#         print("B after")
#         return result
#     return wrapper

# @decorator_a
# @decorator_b
# def greet():
#     print("Hello!")


# greet()


# or you can use the same  decorator on multiple functions or decorate multiple functions with the same decorator 
# def decorator_a(func):
#     def wrapper(*args, **kwargs):
#         print("A before")
#         result = func(*args, **kwargs)
#         print("A after")
#         return result
#     return wrapper

# @decorator_a
# def meet():
#     print("I am gonna meet you in the coming days ")

# @decorator_a
# def greet():
#     print("Hello , HI  ")
# meet()
# greet()


# more real example 


# auth , log , validate and then process the data 

import time

def authenticator(func):
    def wrapper(*args , **kwargs):
        print("Checking Authentication ...")
        return func(*args , **kwargs)
    return wrapper

def log(func):
    def wrapper(*args, **kwargs):
        print("Logging request...")
        return func(*args, **kwargs)
    return wrapper
def validate(func):
    def wrapper(*args, **kwargs):
        print("validating request...")
        return func(*args, **kwargs)
    return wrapper


@authenticator
@log
@validate
def data():
    time.sleep(1)
    print("The data is processing .. ")
    time.sleep(2)
    print("The data has successfully processed! ")
data()





