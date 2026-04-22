# variables 
x=10 #doesn't mean x contains 10 but x references to 10 
# this is how it works 
a=10 
b=a
a=20
# print(b) #still 10 as it refernces to old a and a afterwards becomes 20 

a=[1,2,3,4,5]
b=a 
b.append(6)
# print(a) #the result is [1,2,3,4,5,6] as both a and b reference to the same list object in memory


# dynamic_typing : python variables can chnage the type as well 
x=10 
x="hello "
# x=[1,2,3,4,5]
# print(x) 



# swapping the variables 
x=23
y=45
x,y=y,x
# print(x) #assigned was 23 but the printed value will be 45 as we swapped the values of x and y


# Multiple assignment 
x,y,z= 5, 10 , 13
# print(z) #it will print 13 , you can print all 


# identity vs equality 

a= 256 
b= 433
# print(a is b) # it will be false 
b=a 
# print(a is b) #it will be true as both a and b reference to the same object in memory
a=256
# print(a is b) #it will be true as both a and b reference to the same object in memory
# print(a==b)

# now change the value of the variables but keep them equal 
a=1000
# b=1000
# print(a is b) #it can behave differently , it compares the memory location of a and b and in this case it will be false as both a and b reference to different objects in memory
# print(a==b) #it compares the value 



# dynamic rebinding 

# simply assigning the variables : see the behavior 
x=10
y=x
x=x+50 # new object created 
# print(x) #it will print 60 
# print(y) #it will print 10 , as it still points to the old value 


#But the lists willl bahave differently as they are mutable objects 
# x=[1,2,3,4,5]
# y=x
# x.append(9)
# y.append(10)
# # both the lists will be modified as both x and y reference to the same list object in memory
# print(x)
# print(y) # resutl will be the same [1,2,3,4,5,9,10] for both unlike simple variables where we had different values for x and y after modification


# Mutation trap 

def add_item(lst):
    lst.append(100)

my_list = [1,2,3]
add_item(my_list)

# print(my_list) # it will print [1,2,3,100] as the list is mutable and we are modifying the same list object in memory

def change_value(x):
     x = 50 #we can't assign a new value to a parameter so we can't return x=50 

a = 10
change_value(a)
# print(change_value(a)) #it will print None as the function doesn't return anything and we can't change the value of a as it is immutable

# print(a) #it will print 10 as we can't change the value of as it is immutable 

# so lists are mutable and we can modify them in place but simple variables like integers are immutable and we can't change their value but we can reassign them to a new value which creates a new object in memory.

x=10 
y=x
x="hello "
# x=[1,2,3,4,5]
# print(x)  #it will print "hello " as we reassigned x
# print(y) #it will print 10 as y still points to the old x variable 

# default argument mystery 

# def add_item(item, lst=[]):
#     lst.append(item)
#     return lst

# # first  here we can call this function by sending just one argument as the default for the second argument is already there sowe don't get any error 
# #second we know that lists are mutable so 
# print(add_item(1)) # it will print [1] as we are modifying the same list object in memory
# print(add_item(2)) # it will print [1,2] as we are modifying the same list object in memory and we are appending 2 to the same list which already has 1 in it
# print(add_item(3)) # it will print [1,2,3] as we are modifying the same list object in memory and we are appending 3 to the same list which already has 1 and 2 in it

# fix it : 
# if one is added in one call only one items will be appeared then , we will keep the list as none as a new list is created every time when we call the function 
# def add_item(item, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(item)
#     return lst
# print(add_item(1)) #it will print[1] as we are inserting this in an empty list 
# print(add_item(2)) #it will print [2] as we are creating a new list object in memory for each call to the function
# print(add_item(3, [1,2,5,7]))  # it will print [1,2,5,7,3] as we are modifying the same list object in memory which is passed as an argument to the function and we are appending 3 to it


# variable shadowing : Scope
# x = 10

# def test():
#     x = 20
#     print(x)

# test() #local 
# print(x) #global 



# here the same variable is reassigned globally 
# x = 10

# def test():
#     global x
#     x = 20
#     print(x)

# test() #the same on both 
# print(x)

# del variables 
x = [1,2,3]
y = x

del x
# print(x) # it will give an error that x is not defined as x was  deleted
# print(y) # it will print [1,2,3] as y still references to

# so we can still access the list as it was copied in y and we can modify it as well



# funcs = []

# for i in range(3):
#     funcs.append(i)

# for f in funcs:
#     print(f) #it will print 0 , 1, 2 in three lines
# print(funcs) #it will print [0,1,2] as we are appending the value of i to the list

# but what if the lambda function is used instead of just appending the value of i to the list
# funcs = []

# for i in range(3):
#     funcs.append(lambda: i) #here lambda doesn't capture the value of i but the variable i itself
# for f in funcs:
#     print(f()) # here we can call functions only as in the funcs the lambda functions are stored not the individual value 
# it will print 2 , 2, 2 as the value of i is 2 after the loop and all the lambda functions in the list reference to the same variable i which has the value 2 at the end of the loop

# when the loop runs at every index it will have i variable not the value , it will then resolve back and look for the value until the complete loop runs and the value becomes 2

# LOOP RUNS:
# i = 0 ──→ Create function A → "return i" ──→ Add to list
# i = 1 ──→ Create function B → "return i" ──→ Add to list  
# i = 2 ──→ Create function C → "return i" ──→ Add to list
# │
# │
# ▼
# LOOP ENDS: i = 2 (variable i stays at 2)
# │
# │
# ▼
# CALL FUNCTIONS:
# Function A runs → looks for i → finds 2 → returns 2
# Function B runs → looks for i → finds 2 → returns 2
# Function C runs → looks for i → finds 2 → returns 2

# fix it : we can use default argument in the lambda function to capture the value of i at each iteration of the loop
funcs = []
for i in range(3):
    funcs.append(lambda i=i: i)  # Each gets its OWN copy

# Each prints different value
# for f in funcs:
    # print(f())  # 0, 1, 2
# When loop runs:
# i = 0 → creates: lambda i=0: i  (i's default is 0)
# i = 1 → creates: lambda i=1: i  (i's default is 1)  
# i = 2 → creates: lambda i=2: i  (i's default is 2)

# # Later when called:
# function1() → uses default i=0 → returns 0
# function2() → uses default i=1 → returns 1
# function3() → uses default i=2 → returns 2



# lambda working 

# simple sorting function : remember that sorted function returns a new sorted list and doesn't modify the original list
# Sort by length of string
# fruits = ['apple', 'kiwi', 'banana', 'cherry']
# sorted_fruits = sorted(fruits)
# print(sorted_fruits)  # ['kiwi', 'apple', 'cherry', 'banana']
# the result is sorted in alphabetical order 

# sorted function can also take a key argument which is a function that takes one argument and returns a value to be used for sorting purposes
# wrong behavior: 
# sorted function can also take 2 argument simply 
# sorted_fruits = sorted(fruits , key=len(fruits)) 
# here len(fruits) means how many fruits in the list fruits which are 4 but our purpose is to check the length of characters in each fruit and sort on that base 
# print(sorted_fruits) #this will give an error as the key argument expects a function that takes one argument and returns a value to be used for sorting but we are passing the result of len(fruits) which is an integer and not a function
# right behavior :
# sorted_fruits = sorted(fruits , key=len) # here we are passing the function len that will be applied on every fruit and then will give us the length of each fruit and on that base we will further sort the list 
# print(sorted_fruits) # this will print ['kiwi', 'apple', 'banana', 'cherry'] as the length of kiwi is 4 which is the smallest and then apple and then banana and then cherry as the length of cherry is 6 which is the largest

# lambda x: len(x)
# ^      ^  ^
# |      |  |
# |      |  └── What to return (the function body)
# |      └───── Parameter name (like function parameter)
# └──────────── The keyword "lambda"


# it is same to be written as :

# def some_name(x):
#     return len(x)

# # so writing the above function using lambda 
fruits = ['apple', 'kiwi', 'banana', 'cherry']
# sorted_fruits = sorted(fruits, key=lambda x: len(x))

# What's happening:
# lambda x: → "I'm creating a function that takes one parameter called x"
# len(x) → "This function returns the length of x"
# key= → "Use this function to determine how to sort each item"

# For 'apple':  lambda 'apple'  → len('apple')  → 5
# For 'kiwi':   lambda 'kiwi'   → len('kiwi')   → 4
# For 'banana': lambda 'banana' → len('banana') → 6
# For 'cherry': lambda 'cherry' → len('cherry') → 6

# Then sort based on these numbers: 4, 5, 6, 6
# Result: ['kiwi', 'apple', 'banana', 'cherry']


# Sort by the first letter
# sorted(fruits, key=lambda x: x[0]) #means take that element and return its first character and then sort on the base of first character of each fruit
# print(fruits) # it will print ['apple', 'kiwi', 'banana', 'cherry'] as the original list is not modified as sorted function returns a new sorted list and doesn't modify the original list
# print(sorted(fruits, key=lambda x: x[0])) # it will print ['apple', 'banana', 'cherry', 'kiwi'] as the first letter of apple is a which is the smallest and then b for banana and then c for cherry and then k for kiwi
# lambda 'apple' → 'a'
# lambda 'kiwi'  → 'k'
# etc. result will be in this order : a , b , c , k

# Sort by the last letter  
# sorted(fruits, key=lambda x: x[-1])
# lambda 'apple' → 'e'
# lambda 'kiwi'  → 'i'
# etc. result will be in this order : e , i , a , y : banana , apple , kiwi , cherry

# Sort by whether it contains 'a'
# sorted(fruits, key=lambda x: 'a' in x) #means take the element and check if 'a' is in it and return True or False and then sort on the base of that
# lambda 'apple' → True (1)
# lambda 'kiwi'  → False (0)
# etc. result will be in this order : False , True : kiwi , apple , banana , cherry


# tuple mystery 
# tuples are immutable but they can contain mutable objects as well

t = (1, 2, [3,4]) #inside the tuple we have a list which is mutable and we can modify it in place
t[2].append(5)

# print(t) #the result is (1, 2, [3,4,5]) as we are modifying the list object in place which is inside the tuple and the tuple itself is immutable but it can contain mutable objects as well and we can modify them in place without changing the reference of the tuple itself in memory



# Multiple Assignment Mechanics
# a=b=[]   #here we are creating a new list object in memory and both a and b reference to that same list object in memory
# a.append(1)
# b.append(3)
# print(a) # it will print [1,3] as both a and b reference to the same list object in memory and we are modifying the same list object in memory by appending 1 and 3 to it
# print(b) # it will print [1,3] as both a and b reference to


# now try : 
# a = []
# b = []
# a.append(1)
# b.append(3)
# print(a) 
# print(b)
# now they both are two different list objects in memory and no one is copying or referencing each other so they both have different results 


# Mental challenge questions 

# 1-why first is true and second is false in the below code snippet
# a = []
# b = []
# print(a == b)
# print(a is b)
# the results above will be different first is true while second is false , first compares the value which is same for both as they are empty lists and second compares the reference which is different for both as they are two different list objects in memory

# 2- what will be the output of the below code snippet
x = 10
def f():
    print(x)
    x = 20
f() #it will give an error as we are trying to access the variable x before assigning it a value in the function f and this is because of the way python handles variable scope and it treats x as a local variable in the function f and we are trying to access it before assigning it a value which is not allowed in python and it will give an UnboundLocalError: local variable 'x' referenced before assignment error

# 3- what is stored in memory after this 
x = 100
x = 200
# after the above code snippet is executed , the value 100 will be stored in memory but it will be garbage collected as it is no longer referenced by any variable and the value 200 will be stored in memory and x will reference to it


# challenge deeper 
# Answer this:

x = 100
y = x
x = 200

# Question:
# Does object 100 get garbage collected?
# Answer:
# No.
# Because y still points to it.
# Memory:
# y → 100
# x → 200

# So object 100 still alive.

# Ultimate Trick Question (Interview Killer)
# What is output?

x = [1,2,3]
y = x

x = [4,5,6]
# print(y)
# Answer:
# [1,2,3]
# Why?
# Because:
# x = [4,5,6]
# creates NEW object.
# It does NOT modify old object.
# y still points to old object.


# But this is different:
x = [1,2,3]
y = x
x.append(4)
print(y)
# Output:
[1,2,3,4]
# Because append modifies SAME object.

