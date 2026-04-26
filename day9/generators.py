
# def even_numbers(n):
#     for i in range(n + 1):
#         if i % 2 == 0:
#             yield i

# Usage:

# list(even_numbers(10)) 
# list(even_numbers(10))
# print(list(even_numbers(10)))


# Key idea (THIS is the difference)
# Normal function:
# def f():
#     return 1

#  Call → runs immediately → returns value

# Generator function:
# def f():
#     yield 1

#  Call → does NOT run
#  It only creates a generator

#  Think like this

# A generator is:

# “A machine that produces values only when asked”

#  So how do you “ask”?
# Method 1: list()
# list(even_numbers(10))

#  Now Python starts pulling values one by one:

# 0 → 2 → 4 → 6 → 8 → 10
# Method 2: for loop
# for x in even_numbers(10):
#     print(x)
# Method 3: next() (most important for understanding)
# gen = even_numbers(10)

# print(next(gen))  # 0
# print(next(gen))  # 2
# print(next(gen))  # 4

#  Each next() = “give me next value”

#  Now the REAL difference (important)
# List version:
# def even_numbers_list(n):
#     result = []
#     for i in range(n + 1):
#         if i % 2 == 0:
#             result.append(i)
#     return result

#  This:

# builds FULL list in memory
# returns everything at once
# Generator version:
# def even_numbers(n):
#     for i in range(n + 1):
#         if i % 2 == 0:
#             yield i

#  This:
# does NOT build list
# gives values one by one
# saves memory
#  Real-world analogy

# List:
# “Give me the whole book”

# Generator:

# “Read me one page at a time”

#  Why generators exist (the REAL reason)
# Imagine:

# range(10**9)
# List:
# [x for x in range(10**9)]

#  Memory crash

# Generator:
# (x for x in range(10**9))

#  Works fine (lazy evaluation)
#  Your main misunderstanding
# You expected:

# “Function should give output immediately”
# But generators are:
# “Delayed execution (lazy execution)

# Correct ways to print generator values
# 1. Using print(list(...))
# print(list(even_numbers(10)))

# #  Output:

# [0, 2, 4, 6, 8, 10]
# 2. Using a for loop (most common)
# for x in even_numbers(10):
#     print(x)

#  Output:

# 0
# 2
# 4
# 6
# 8
# 10
# 3. Using next() (step-by-step)
# gen = even_numbers(10)

# print(next(gen))  # 0
# print(next(gen))  # 2
# print(next(gen))  # 4
#  Important difference
# This:
# list(even_numbers(10))

# creates → returns → disappears (if not printed)

# This:
# print(list(even_numbers(10)))

#  creates → prints → you see it

