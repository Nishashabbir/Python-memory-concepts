
# 1. What is a list comprehension?
# It is a short way to create a list from another iterable (like list, string, range).

# 1-print squares 

# Normal way:
squares = []
for i in range(5):
    squares.append(i * i)

# List comprehension:
squares = [i * i  for i in range(5)]
# print(squares)

# 2. Basic structure (VERY important)
# [expression for item in iterable]

# Break it mentally like:

# “For each item in iterable, apply expression, collect results in a list”

# With condition (filtering)
# Example: even numbers
# Normal:
# evens = []
# for i in range(10):
#     if i % 2 == 0:
#         evens.append(i)

# # list comprehension 
# 2- print evens 

# evens=[i%2==0 for i in range(10)] #this is wrong cuz i%2==0 is condition not expression 
# for condition , we'll write like this 
# evens=[i for i in range(10) if i%2==0 ] #we just the numbers(i) which are divided by 2 
# print(evens)

# so the structure becomes:
# [expression for item in iterable if condition]

# 3-print labels of even or odds using if else 

# labels = ["even" if i % 2 == 0 else "odd" for i in range(5)]
# print(labels)

# so this is Structure:
# #true expression before if and false expression before else for item in iterable 
# [expr_if_true if condition else expr_if_false for item in iterable]

# Notice: if-else comes BEFORE for

# # 4-Convert numbers to strings with rule:
# nums = [1, 2, 3, 4, 5 ,4, 3, 2, 1]

# result=["big" if i>3 else "small" for i in nums] #if-else before for 

# print(result)


matrix = [[1,2] , [2,3,4] , [5,8,2]]
# flat=[]
# for row in matrix:
#     for n in row:
#         flat.append(n)
# print(flat)

flaten=[ num for row  in matrix for num in row ]
# print(flaten)

# String examples
# Convert string to list of characters:
text = "hello world"
chars=[c for c in text]
# print(chars)
# Uppercase only vowels:
vowels= [ v.upper() for v in text if  v in "aeiou"] #it will search v in text ,  which can be from string "aeiou" and then will return its uppercase and print in list
# print(vowels)

# Set & Dictionary comprehensions
# Set comprehension (unique values)

nums = [1, 2, 2, 3, 3, 3]

# a set is a collection of distinct and unique objects so there will be no repeatition 

set={ n for n in nums } #it will not print the repeatition 
# print(set)
# print({n for n in nums})

# Dictionary comprehension
squares = {x: x*x for x in range(5)}
# print(squares)

# Result:

# {0:0, 1:1, 2:4, 3:9, 4:16}

# the expression we wanted was num:square so we will write like that as key value in the dictionary of curly braces 

sums={num:num+num for num in range(5)}
# print(sums)

# 1. Multiple conditions
nums = [1,2,3,4,5,6,7,8,9]

result = [x for x in nums if x % 2 == 0 if x > 4]
rzlt=[x for x in nums if x % 2 == 0 and x > 4] #same as above 
# print(result)
# print(rzlt)

#  Same as:

# Using functions inside comprehension
def sqaure(x):
    return x*x
rezlt=[sqaure(x) for x in nums]
# print(rezlt)

# Comprehension with tuples
pairs = [(x, x*x) for x in range(5)] #(x, x*x) this shape is what we see as output 
print(pairs)
# result:
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]



