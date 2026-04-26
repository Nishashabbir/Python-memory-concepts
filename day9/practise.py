#  Q1

# Generator for squares of 1–5

gen = (x*x for x in range(1, 6))

# Usage:

list(gen)   # [1, 4, 9, 16, 25]
#  Q2

# Generator function for even numbers up to n

def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

# Usage:

list(even_numbers(10))   # [0, 2, 4, 6, 8, 10]
#  Q3

# Using next() manually

gen = (x for x in range(3))

print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2

# If you do one more:

print(next(gen))

#  You’ll get:

# StopIteration 