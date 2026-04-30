
# 1-map() — transformation ////////////////////////////////////////////
# What it does

# Applies a function to every item in the list 

# nums = [1, 2, 3, 4]

# result = list(map(lambda x: x*x, nums))

#  Same as:

# [x*x for x in nums]
# When to use map
# When you already have a function
# When operation is simple and uniform
# def square(x):
#     return x*x

# list(map(square, nums))
# When NOT to use map
# When logic includes conditions → use list comprehension
# When lambda becomes ugly

#  Bad:

# list(map(lambda x: x*x if x%2==0 else x+1, nums))

#  Better:

# [x*x if x%2==0 else x+1 for x in nums]


# practise 
nums=[1,2,3,4,5,6]

# def sqr(x):
#     return x*x 
# squares=list(map(sqr, nums))
# print(squares)

# # lambda 
# squares=list(map(lambda x : x*x , nums))
# print(squares)

# 2. filter() — selection
# What it does

# Keeps only items where condition is True

# nums = [1,2,3,4,5]

# result = list(filter(lambda x: x % 2 == 0, nums))

#  Same as:

# [x for x in nums if x % 2 == 0]
# When to use filter
# When you already have a function returning True/False
# def is_even(x):
#     return x % 2 == 0

# list(filter(is_even, nums))
# When NOT to use filter

# Almost always in Python 

#  List comprehension is:

# more readable
# more Pythonic

#  Prefer:

# [x for x in nums if x % 2 == 0]
# 3. lambda — anonymous function
# What it is

# A small one-line function

# lambda x: x * x
# Where it’s useful
# (A) Inside map / filter
# list(map(lambda x: x+1, nums))


# # practise 
# evens=list(map(lambda x :x%2==0 , nums)) #not a right approach 
# evens=list(filter(lambda x :x%2==0 , nums)) #filter the list and retain only evens 
# print(evens)





# (B) Sorting (VERY important)
# students = [("Ali", 20), ("Ahmed", 18), ("Sara", 22)]

# sorted(students, key=lambda x: x[1])

#  Sort by age

# (C) Quick one-time logic
# (lambda x: x+5)(10)  # 15

# (not very common, but good to know)

# When NOT to use lambda
#  1. Complex logic
# lambda x: x*x if x>0 else x+10 if x<0 else 0

#  unreadable → use normal function

#  2. Multiple statements

# Lambda only supports one expression 


students=[("nisha" , 20) , ("aliza" , 21) , ("alia" , 13) , ("farzana" , 25)]

# you have to give key on the base of which we will sort , the sort function will get each tupel and lambda will return the second element which is age , and on the base of age we will sort the list 
print(sorted(students , key=lambda x : x[1]))
print(students) #it will give the original 




