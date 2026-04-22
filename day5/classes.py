#1 A class is a data type not just a blurprint that stores data (state) and functions(behavior)  in it 
# When you create a class, you’re defining a new type in memory.
# class Person:
#     pass

# Now Person is a new type — like int, list, dict.

# PART 2 — Object Creation (What Actually Happens)

# class Person:
#     pass
# p = Person()
# What happens internally?
# Python allocates memory for a new object.
# It creates an empty namespace (dictionary).
# It binds that object to p.
# Check:

# print(type(p))
# Output:
# <class '__main__.Person'>
# You just created a new type instance.

# PART 3 — The Constructor (__init__)

# This is not the object creator.
# It initializes the object after creation.
# class person:
#     def __init__(self , name ):
#         self.name=name

# p=person("nisha")
# print(p.name)

# self refers to the instance being created.

# Important mental model:
# self.name = name
# means:
# Inside this object’s dictionary, create key "name" and store value.

# part 4  # NOw imagin a scnerio that if there are many objects of one class , now all objects have one same variable equally shared and all objects have one variable which is unique to each one 
# like a class dog of the same sepecie (one common variable ) but they all have unique names (another varaible possessed by every but unique to each object  )

# e.g here comes the instance vs class variable 
# class dog:
#     sepecie = "canine "  #class variable  equally shared by every object 
#     def __init__(self , name):
#         self.name=name   #instance variable unique to every object 
    
# d1=dog("A")
# d2=dog("B")

# print(d1.sepecie)
# print(d2.sepecie) #both have same sepecie 
# print(d1.name)
# print(d2.name)

# # now if you want to change the sepecie for all the dogs 
# dog.sepecie="animal "
# # print(d2.sepecie) #both changed to animal 
# # print(d1.sepecie)
# # but if you want to change the sepecie for specific object 
# d1.sepecie= "husky "
# print(d1.sepecie) #husky changed 
# print(d2.sepecie) #but others remain the same 

# PART 7 — Method Types (Very Important)

# 1️ Instance Methods
# def method(self):

# Operate on object.

# Think of it like this:
# Object methods = Actions that individual objects do

# john.introduce() - John introduces himself
# my_car.drive() - My specific car drives

# Class methods = Actions related to the WHOLE group/blueprint

# Person.total_population() - Ask how many people exist in total
# Car.factory_settings() - Get default settings for all cars


# 2️ Class Methods
# @classmethod
# def method(cls):

# Operate on class.

# Example:
# class Person:
#     population = 0
    
#     def __init__(self):
#         Person.population += 1

    
#     def get_population(cls):
#          cls.population
# p1=Person()
# p2=Person()
# p3=Person()

# print(Person.population)
# # Person.population=99 #remember that anyone can change this data ,so better use a private class 
# print(Person.population)

# NOW A BIG QUESTION WHY SHOULD WE USE CLASS METHODS WHEN WE CAN DO CREATE THE SAME FUNCTIONALITY AND USE THEM ON OBJECT LEVEL ..? 
# THE ANSWER IS IN class.txt ___ its all about the logical use of class methods 

# Static Methods

# No self. No cls.
# @staticmethod
# def add(a, b):
#     return a + b

# again : 
# A static method is basically a function that lives inside the class but doesn’t use instance (self) or class (cls) data.
# So before using it, ask:
# “Does this function need balance, name, or total_accounts?”
# If yes → use self or cls
# If no → use @staticmethod

# variables internal behavior 

# encapsulation  in python : 
# Python does NOT believe in strict private variables

# It follows:

# “We are all responsible developers”

# So encapsulation in Python is:

# more about discipline
# less about restriction
# _x → “Please don’t touch”
# __x → “Really, don’t touch (but you still can if you try)”


# PART 9 — Property Decorator
# Instead of:
# obj.get_age()

# You can write:

# class Person:
#     def __init__(self, age):
#         self._age = age
    
#     @property
#     def age(self):
#         return self._age

# Now:

# p.age

# Feels like attribute, acts like method.


# PART 10 — Dunder Methods (Magic Methods)
# 1. Object representation
# __str__
# __repr__

# Control how your object prints.

# 2. Initialization / lifecycle
# __init__
# __del__
# 3. Operator overloading
# __add__
# __sub__
# __mul__
# __eq__
# 4. Container behavior
# __len__
# __getitem__
# __setitem__
# 5. Iteration
# __iter__
# __next__



# learn step by step ******************************
# They’re called “magic methods” because they let your objects behave like built-in types. For example, when you use +, len(), or print(), Python is actually calling these methods behind the scenes.
# Why they matter

# Dunder methods let you:

# Make your objects act like numbers (+, -, *)
# Make them printable (str(), repr())
# Control comparisons (==, <)
# Support iteration (for x in obj)
# Customize behavior deeply (like context managers with with)

# there are differnet types of it using it we will then understand 

# 1. Object representation ********
# __str__
# __repr__

# # These control how your object appears when printed or inspected.

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

# s = Student("Ali", 90)
# print(s) #so here we are trying to print the object which is normally impossible 

# this will be the  output : > python classes.py
# <__main__.Student object at 0x00000208A5

# fix with __str__: 

# class Student:
#    def __init__(self , name , marks):
#        self.name=name 
#        self.marks=marks

#    def __str__(self ):
#        return f"The name is {self.name} and the marks are {self.marks}"

# s1=Student("nisha" , 20)
# print(s1)

# so directly we  can't print an object with values unless we use a dunder method 
       

# # now using __repr__
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def __str__(self):
#         return f"{self.name} scored {self.marks}"

#     def __repr__(self):
#         return f"Student('{self.name}', {self.marks})"  #specifically that colon sign 
# # Now:
# s = Student("Ali", 90)

# print(s)     # uses __str__ , if you don't use str (don't want to print object like that string ) , then writing just __repr__ will also work 
# s   #in this file nothing will happen , but in the interactive shell :  calls __repr__ automatically 
# print(repr(s))

# so how actually can you use it in the scripts 
# print(s)        # calls __str__
# print(repr(s))  # calls __repr__

# When is __repr__ actually used?
# Debugging in terminal
# When printing lists of objects:
# [Student("Ali", 90)]

#  This uses __repr__, NOT __str__

# Logging
# Developer tools

# Key difference
# Context	Code	What happens

# Interactive shell     	s	             calls __repr__ automatically
# Script file         	s	             nothing happens
# Anywhere	            print(s)        	calls __str__


# in the terminal you can use like this : 
# PS C:\Users\User\Desktop\PYTHON> python  #write python like this 
# Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# Ctrl click to launch VS Code Native REPL
# >>> class Test:
# ...     def __repr__(self):
# ...         return "This is repr"
# ... 
# >>> t = Test()
# >>> t
# This is repr #this is the output for t 
# >>> 


# you can also use this way 

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def __repr__(self):
#         return f"Student('{self.name}', {self.marks})"

# we can also send the objects in a list and use repr to print it as a list 
# students = [
#     Student("Ali", 90),
#     Student("Sara", 85),
#     Student("Ahmed", 70)
# ]
# print(students)  
# or simply like this 
# s1=Student("nisha " , 20)
# print(s1)


# Note: 
# When building ANY class:
# Always write __repr__ first
#  Then optionally __str__



# Step 2 — Object Creation & Lifecycle (__init__, __del__)
# _init__ runs automatically when you create an object.

# Think of it as:

# “Set up the object right after it is created.”
# __init__ does NOT create the object
# It only initializes it

# 1. Python creates the object in memory
# 2. Python calls __init__(self, "Ali")
# 3. Object is ready to use


# __del__ — Object Destruction (LESS USED)
# What it does

# __del__ runs when Python is about to delete an object from memory.

# class Test:
#     def __del__(self):
#         print("Object is being deleted")

# t = Test()
# del t

# In real Python programming:
# You rarely need __del__
# Python garbage collector handles memory automatically

# example : 
# class File:
#     def __init__(self, filename):
#         self.filename = filename
#         print(f"{filename} opened")

#     def __del__(self):
#         print(f"{self.filename} closed")

# f = File("data.txt")
# del f #Even you don't use it 

# 1. __new__   → creates object in memory
# 2. __init__  → initializes object

# class Phone:
#     def __init__(self, brand, price):
#         self.brand= brand 
#         self.price= price
#         print(f"phone is created !")
#     def __del__(self):
#         print(f"phone is deleted ")
        
# p1=Phone("samsung" , 30000)  

# del p1   #only python decides when p1 is no longer needed and then it is deleted 
#     __del__ is unreliable
# timing is not guaranteed
# garbage collector may delay it

#  So professionals usually avoid relying on it.

# Step 3 — Operator Overloading*************************

# This is where Python starts feeling “magical.”
# You’ll learn how to make your own objects work with operators like:

# class Box:
#     def __init__(self, value):
#         self.value = value

#     def __add__(self, other):
#         return Box(self.value + other.value)

# Now:

# b1 = Box(10)
# b2 = Box(20)

# result = b1 + b2
# print(result.value)

# +
# -
# ==
# *
# <, >

# All using dunder methods.
#  Core idea
# Normally:
# 5 + 3
# But for objects:
# obj1 + obj2
# Python actually calls:
# obj1.__add__(obj2)
# What is other in __add__? Can it be anything?

# In your code:
# def __add__(self, other):
#     return Box(self.value + other.value)
#  other is just a parameter name
# It represents the object on the right side of +.

# So here:
# result = b1 + b2
# Python internally does:
# b1.__add__(b2)

# So:
# self = b1
# other = b2
# Can other be “anything”?

# Technically yes, Python allows it — but:
# Your code assumes other.value exists
# So other must be an object that has a .value attribute
# Example valid:
# Box(10) + Box(20)
# Example invalid:

# Box(10) + 5   # will crash (int has no .value)

#Note :  Usually you'd add a check:

# def __add__(self, other):
#     if isinstance(other, Box):
#         return Box(self.value + other.value)
#     return NotImplemented


# Why do we return Box(...) in __add__?
# This line:
# return Box(self.value + other.value)
# means:

#  “After adding, return a new Box object, not just a number.”
# So:
# b1 = Box(10)
# b2 = Box(20)

# result = b1 + b2
# becomes:
# result = Box(30)
# Why not return just 30 ?
# You could, like this:
# return self.value + other.value
# But then:
# result = b1 + b2
# print(result.value)  #  error (int has no .value)
# So returning Box(...) keeps the object type consistent.

# Why do we use result.value instead of result?

# Because:
# result = Box(30)
# So:
# result → the whole object
# result.value → the stored data inside it
# Example:
# print(result)
# This prints something like:
# <__main__.Box object at 0x...>
# Not useful.
# But:
# print(result.value)
# prints:
# 30


# you can use other operator as well such as * , == 

# Step 4 — Container Behavior ***********************

# __len__
# class Basket:
#     def __init__(self , items):
#         self.items=items
#     # def __len__(self):
#     #     return len(self.items)  #if we don't use this method then len won't work for an object i-e len(B1) is impossible , though it would work for list so we used this len method to make our program able to use len on object as well 

# B1=Basket(["apple" , "banana" , "cherry"])
# print(len(B1))


# __getitem__
# class Basket:
#     def __init__(self, items):
#         self.items = items

#     def __getitem__(self, index):
#         return self.items[index]

# # Usage:

# b = Basket(["apple", "banana", "mango"])
# print(b[1])

# . __setitem__ → assigning (obj[i] = value)
# What it does

# Allows:

# obj[0] = "new value"
# Example
# class Basket:
#     def __init__(self, items):
#         self.items = items

#     def __setitem__(self, index, value):
#         self.items[index] = value

# # Usage:

# b = Basket(["apple", "banana", "mango"])
# b[1] = "grape"

# print(b.items)

# #  Output:

# # ['apple', 'grape', 'mango']

# # combining all the three 

# class Basket:
#     def __init__(self , items):
#         self.items=items 
#     def __len__(self):
#         return len(self.items)
#     def __getitem__(self, index):
#         return self.items[index]
#     def __setitem__(self, index, value):
#         self.items[index]= value

        
# b=Basket(["a" , "b" , "c" , "d"])
# print(len(b))
# print(b[0])
# b[1]= "x"
# print(b.items)


# # len(obj)     	__len__()
# # obj[i]      	__getitem__()
# obj[i] = x  	__setitem__()
# Step 5 — Iteration (__iter__, __next__)

# Goal: make this work:

# for book in b1:
#     print(book)
#  Core idea

# A for loop does this internally:

# 1. iterator = obj.__iter__()
# 2. keep calling iterator.__next__()
# 3. stop when StopIteration is raised
#  1. __iter__ → gives an iterator
#  2. __next__ → gives next item
#  Important design choice
# There are two ways to implement iteration
#  Simple (recommended)
# Use Python’s built-in iterator
#  Manual (advanced)
# Track index yourself
# We’ll do both—but start with the smart way.


# Method 1 (BEST) — Use existing list iterator
# class Library:
#     def __init__(self, books):
#         self.books = books

#     def __iter__(self):
#         return iter(self.books)
# Usage:
# b1 = Library(["English", "Urdu", "Maths"])
# for book in b1:
#     print(book)

#  Output:

# English
# Urdu
# Maths
#  Why this is good

# You reused Python’s built-in iterator:

# iter(self.books)

#  Clean, simple, professional

class Library:
    def __init__(self , books):
        self.books=books 
    def __iter__(self):
        return iter(self.books)
    

l1 = Library(["English", "Urdu", "Maths"])
# method 1 to print 
mylist=iter(l1)
print(next(mylist))
print(next(mylist))
print(next(mylist))

# simply like this : 

# for l in l1:
#     print(l )

# __str__       # print()
# __repr__      # debugging
# __len__       # len()
# __eq__        # ==
# __lt__        # <
# __call__      # obj()
# __getitem__   # obj[index]

# Classes can behave like built-ins.

        





# just as you can apply iterator on a list , you can make your object as an iterator as well 
# list=[1,2,3,4,5]
# mylist=iter(list)
# # print(mylist)
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))





