# Two main loop types in Python:

# for loop → iterate over sequence
# while loop → iterate based on condition

# for variable in iterable:
#     code

# What “iterable” Really Means
# Iterable = object that can produce values one-by-one.
# Examples:

# list
# string
# tuple
# set
# dictionary
# range
# generator


# for char in "HELLO":
#     print(char)



# PART 6 — Infinite Loops
# while True:
#     print("Running")

# Runs forever
# Used in:
# servers
# games
# monitoring systems
# You must manually stop.

# 7 — break Statement
# for i in range(10):
#     if i == 5:
#         break
#     print(i)  # breaks before printing 5 

# for i in range(10):
#     print(i)   #prints up to  5 and then stops 
#     if i == 5:
#         break

# 8 — continue Statement
# skip current iteration 
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)

# #  9 — else in Loops (Most People Don’t Know This)

# for i in range(6):
#     print(i)
# else:
#     print("loop Finished !")  #only works in the simple loops and both the statements will run 

# # But not ____ if break occurs:

# for i in range(5):
#     print(i)
#     if i == 3:
#         break #here the whole loop ends , so else is skipped automatically 
# else:
#     print("Finished") # it will not run 


# 10 — Nested Loops

# for i in range(3):
#     for j in range(2):
#         print(i, j)


# 0 0
# 0 1 
# 1 0
# 1 1 
# 2 0 
# 2 1


# 11 - Looping Through Dictionaries

# for printing the keys only : 
# data = {"a":1, "b":2}
# for key in data:
#     print(key)


# for values only 
# data = {"a":1, "b":2}
# for values  in data.values():
#     print(values)



#  if you want to print the both  then you have to change the keyword on the iterable 

# data = {"a":1, "b":2}
# for key , value in data.items():
#     print(key , ": " , value) 

# 12 — enumerate (Professional Tool)
# instead of using : 

# for name in names     # you better write : 

# names = ["A","B","C"]

#  #in this way you will be accessing the indices as well 

# for index , name in enumerate(names ):
#     print(f"at index {index} : name is {name }")

# 13 — zip (Advanced Tool)
# scenerio : when you want to apply a loop on more than 1 list at the same time 

# names = ["A","B"]
# scores = [90,80]


# for name , score in zip(names , scores ):
#     print(name , score)


# Loop Variable Behavior (Critical Concept)
# for i in range(5):
#     pass

# print(i) #it prints 4  as  Variable still exists. Loop does not create new scope.


# 15 — Mutation During Loop (Danger Zone)

# lst = [1,2,3]

# for x in lst: #it means for every iteration make those changes which result in inifinit as 100 keeps appending and elements are added 
#     lst.append(100)

#  Never modify iterable while iterating over it. 

# 16 — Loop With Objects (Backend Level)
# users = [
#     {"name":"A"}, #user means this one object inside the list 
#     {"name":"B"}
# ]
# for user in users: 
#     print(user["name"]) #not users[name] that will be invalid  


# # 17- Loop Control Variable Memory Behavior

# funcs = []

# for i in range(3):
#     funcs.append(lambda: i)

# for f in funcs:
#     print(f())

# lambda i will store not the vlue of i but the same reference of i as lambda function , so inside funcs functions are stored instead of value , so we will call them as functions for printing 


# OUTPUT    
# 2
# 2
# 2

# Because lambdas reference same i.
# Professional fix:
# funcs.append(lambda i=i: i)

# Visual Memory Model

# Without fix:

# lambda1 → i
# lambda2 → i
# lambda3 → i

# i → 2

# With fix:

# lambda1 → its own i → 0
# lambda2 → its own i → 1
# lambda3 → its own i → 2

# 18- Loop + Memory + Reference Combined

# lst = [[1],[2],[3]]

# for item in lst:
#     item.append(100)

# print(lst)

# # output:
# [[1,100],[2,100],[3,100]] #here the list will not go forever becuase we are not appending in the list but child elements of list which is okay as the real iteration is over the list not the child elements 


# challenge : 
# lst = [1,2,3]

# for x in lst:
#     x = x * 10  #here variables are reassigned and new objects created in the memory  , but python still points to the old objects 
#     print(x) #this will have different result then the print statement down to it 
# print(lst) #so here no change in the list , so the lst was not modified but it was reassigned so the above points to the reasigned one and the later print statement points to the older list un modified 

# answer is : 
# 1 , 2, 3 
# why ? 
# Because this line:
# x = x * 10
# does NOT modify the list.
# It only reassigns the variable x.   

# lst → [1,2,3]
# Loop starts:
# Iteration 1:
# x → 1
# Now this line executes:

# x = x * 10
# Python creates NEW object:

# 10 created
# x → 10
# But list still points to old object:

# lst → [1,2,3]
# List was never modified.
# same goes on for others : 
# Final:
# lst → [1,2,3]
# Because integers are immutable and assignment doesn't modify original object. it just creates new ones 


# Core Rule (Tattoo this in your brain)

# Assignment → changes variable not objects 
# Mutation → changes object

# Example:

# Assignment:

# x = 5
# x = 10


# Mutation:

# x = [5]
# x.append(10)
# print(x)


# output: [5,10]
# # **********************************
# Lambda is just a function without a name.
# Normal function:

# def square(x):
#     return x * x

# Lambda version:

# square = lambda x: x * x
# Same thing.
# Proof:
# print(square(5))

# Output:
# 25

# Why Lambda Exists?
# To create small functions quickly.
# Example:

# 1- 
# add = lambda a,b: a+b

# print(add(2,3))

# # 2-
# lambda x: x*2
# is same as:

# def temp(x):
#     return x*2
# Lambda is just shorthand.
# 3- 
# nums = [1,2,3]
# result = list(map(lambda x: x*2)) #map applies the function to every element 
# print(result)

# Output:

# [2,4,6]

# Lambda Capturing Variable
x = 10
f = lambda :x 
print(f())
# also 
f = lambda x :x*10 
print(f(2))

# Output:
# 10

# Lambda remembers variable x.
# Closure behavior.

# Sorting objects:

# users = [
#     {"name":"A", "age":20},
#     {"name":"B", "age":15}
# ]

# # users.sort(key=lambda user: user["age"])
# print(users)
# # Sorts by age.



