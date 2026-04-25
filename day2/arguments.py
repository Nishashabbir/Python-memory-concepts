# *args and **kwargs are Python’s way of letting functions accept a flexible number of arguments.

# They’re especially common in decorators (like your example), wrappers, and APIs.

#  *args (positional arguments)
# Collects extra positional arguments into a tuple
# “args” is just a convention; the * is what matters
# Example:
def func(*args):
    print(args)

func(1, 2, 3)

Output:

(1, 2, 3)

# So *args means:
#  “Take any number of positional arguments and pack them into a tuple.”

#  **kwargs (keyword arguments)
# Collects extra named arguments into a dictionary
# Example:
def func(**kwargs):
    print(kwargs)

func(name="Ali", age=20)

Output:

{'name': 'Ali', 'age': 20}

# So **kwargs means:
#  “Take any number of keyword arguments and pack them into a dictionary.”

#  Using both together
def func(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

func(1, 2, name="Ali", age=20)

Output:

args: (1, 2)
kwargs: {'name': 'Ali', 'age': 20}
#  In your decorator

# Your code:

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling function...")
        return func(*args, **kwargs)
    return wrapper
# What’s happening:
# wrapper accepts any function signature
# It doesn’t care what arguments the original function needs
# It forwards everything unchanged:
# func(*args, **kwargs)

# This is called argument forwarding
#  Why decorators need this
# Without *args, **kwargs, your decorator would only work for one specific function shape.
# Example problem:

def wrapper(a, b):
    return func(a, b)

# This breaks if func(x) or func(a, b, c).

# So *args, **kwargs makes decorators universal.



# 1. Positional arguments vs keyword arguments

# These are passed based on order.

# Example:
# def greet(name, age):
#     print(name, age)

# greet("Ali", 15)
# How Python reads it:
# "Ali" → goes to name
# 15 → goes to age

#  Order matters a lot here.

# If you swap them:
# greet(15, "Ali")

# Now it becomes wrong logically:

# name = 15
# age = "Ali"
#  2. Named (keyword) arguments

# These are passed using the parameter name explicitly.

# Example:
# greet(name="Ali", age=15)

# Here order doesn’t matter:

# greet(age=15, name="Ali")

# Both work the same.

#  Key differences
# Feature	Positional	Named (Keyword)
# Based on order	 Yes	 No
# Uses parameter names	 No	 Yes
# Readability	Medium	High
# Flexibility	Low	High
#  Mixed usage (very common)

# You can combine both:

# def add(a, b, c):
#     return a + b + c

# add(1, c=3, b=2)

#  This works because:

# 1 is positional → a
# b=2, c=3 are named
#  Important rule

# Once you start using keyword arguments, you cannot go back to positional:

# add(1, b=2, 3)  #  Error
#  Simple way to remember
# Positional = order matters
# Named = labels matter


# note: 1. Can we print AND return at a time ?
#  YES

# A function can do both:

# def example():
#     print("Hello")
#     return 42
# What happens when you call it:
# x = example()

# Output:

# Hello

# And:

# print(x)

# Output:

# 42
#  Key idea:
# print() → shows something on screen
# return → gives value back to the caller

# They are completely different things.

#  2. Why returning is important (“safe side” idea)

# Yes — your intuition is correct: returning is the safer design choice.

# Let’s understand why.

#  If you ONLY print
# def add(a, b):
#     print(a + b)

# Now:

# x = add(2, 3)
# print(x)

# Output:

# 5
# None
#  Problem:
# You can see the result
# BUT you cannot reuse it

# Because:

# printed value is NOT stored anywhere


# If you RETURN
# def add(a, b):
#     return a + b

# Now:

# x = add(2, 3)
# print(x)

# Output:

# 5
#  Benefits:
# You can store it
# reuse it
# pass it to other functions
# test it
# debug it easily