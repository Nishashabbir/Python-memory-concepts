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

# encapsulation  in python : **********************************
# Why Use Encapsulation?
# Encapsulation provides several benefits:

# Data Protection: Prevents accidental modification of data
# Validation: You can validate data before setting it
# Flexibility: Internal implementation can change without affecting external code
# Control: You have full control over how data is accessed and modified


# here we learn about it 
# In Python, you can make properties private by using a double underscore __ prefix:

# Create a private class property named __age:

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age # Private property

# p1 = Person("Emil", 25)
# print(p1.name)
# print(p1.__age) # This will cause an error

# # method 2 where you can access through a function already defined in the class and can be used outside the class on an object unlike property 
# # Use a getter method to access a private property:

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age

#   def get_age(self):
#     return self.__age

# p1 = Person("Tobias", 25)
# print(p1.get_age())

# you can modify a private property like this 

# Use a setter method to change a private property:

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age

#   def get_age(self):
#     return self.__age

#   def set_age(self, age):
#     if age > 0:
#       self.__age = age
#     else:
#       print("Age must be positive")

# p1 = Person("Tobias", 25)
# print(p1.get_age())

# p1.set_age(26)
# print(p1.get_age())



# Use encapsulation to protect and validate data:

# class Student:
#   def __init__(self, name):
#     self.name = name
#     self.__grade = 0

#   def set_grade(self, grade):
#     if 0 <= grade <= 100:
#       self.__grade = grade
#     else:
#       print("Grade must be between 0 and 100")

#   def get_grade(self):
#     return self.__grade

#   def get_status(self):
#     if self.__grade >= 60:
#       return "Passed"
#     else:
#       return "Failed"

# student = Student("Emil")
# student.set_grade(85)
# print(student.get_grade())
# print(student.get_status())


# Protected Properties/   

# class Person:
#   def __init__(self, name, salary):
#     self.name = name
#     self._salary = salary # Protected property

# p1 = Person("Linus", 50000)
# print(p1.name)

# print(p1._salary) # Can access, but shouldn't

# Private Methods
# You can also make methods private using the double underscore prefix:

# Example
# Create a private method:

# class Calculator:
#   def __init__(self):
#     self.result = 0

#   def __validate(self, num):
#     if not isinstance(num, (int, float)):
#       return False
#     return True

#   def add(self, num):
#     if self.__validate(num):
#       self.result += num
#     else:
#       print("Invalid number")

# calc = Calculator()
# calc.add(10)
# calc.add(5)
# print(calc.result)
# # calc.__validate(5) # This would cause an error


# name mangling means "change or hide the variables "

# you can access the private varible in a way like this obj._class__variable 

# Name Mangling
# Name mangling is how Python implements private properties and methods.

# When you use double underscores __, Python automatically renames it internally by adding _ClassName in front.

# For example, __age becomes _Person__age.

# Example
# See how Python mangles the name:

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age

# p1 = Person("Emil", 30)

# # This is how Python mangles the name:
# print(p1._Person__age) # Not recommended!







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

# class Library:
#     def __init__(self , books):
#         self.books=books 
#     def __iter__(self):
#         return iter(self.books)
    

# l1 = Library(["English", "Urdu", "Maths"])
# # method 1 to print 
# mylist=iter(l1)
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))

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




# class library:
#     def __init__(self , shelves):
#         self.shelves=shelves
#     def __iter__(self):
#         return iter(self.shelves)

# l1=library(["1A", "1B" , "1C" ])
# for i,  l in enumerate(l1):
#     print(f"at position {i+1} there is shelf : {l}")



# # # PART 11 — Inheritance
# # Python Inheritance
# # Inheritance allows us to define a class that inherits all the methods and properties from another class.
# # Parent class is the class being inherited from, also called base class.
# # Child class is the class that inherits from another class, also called derived class.



# # simple :  create a parent class and a child class to inherit it 
# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# #Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()

# class Student(Person):
#   pass

# s= Student("Mike", "Olsen")
# s.printname()

# # __init__()
# # Add the __init__() function to the Student class:

# class Student(Person):
#   def __init__(self, fname, lname):
    #add properties etc.


# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

# Example

# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
# class Student(Person):
#   def __init__(self, fname, lname):
#     super().__init__(fname, lname)

#     By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

# lets create a class and inherit the child classes as well as method and see their behavior 



# class person():
#     def __init__(self , fname , lname):
#         self.fname=fname
#         self.lname=lname 
#     def __repr__(self):
#         return f"first name is {self.fname} and last name is {self.lname}"
    
# class employee(person):
#     pass

# class student(person):
#     def __init__(self, name ):
#         self.name=name 
        
#     def __repr__(self):
#         return f"the name is {self.name}"  


# # going one step forward 
# class child(person):
#     def __init__(self, fname, lname , age):
#         person.__init__(self , fname, lname) 
#         self.age=age
#     def __repr__(self):
#        return f"first name is {self.fname} and last name is {self.lname} and the age is {self.age}"     

#     def greet(self):
#         return f"Hello {self.fname}. Good morning! "


# c1=child("sir" , "Asif" , 40)
# print(c1)
# print(c1.greet())



# p1=person("nisha" ,  "Shabbir")
# print(p1)
# e1=employee("abdullah" , "ali")
# print(e1)
# s1=student("ghulam" )
# print(s1)


# instead of writing person.__init__  , you will be writing super() like this 

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# x = Student("Mike", "Olsen", 2024)
# x.welcome()







# 7. Types of Inheritance in Python
# 1. Single Inheritance
# class A: pass
# class B(A): pass
# 2. Multiple Inheritance
# class A: pass
# class B: pass
# class C(A, B): pass
# 3. Multilevel Inheritance
# class A: pass
# class B(A): pass
# class C(B): pass
# 4. Hierarchical Inheritance
# class A: pass
# class B(A): pass
# class C(A): pass



# 8. Method Resolution Order (MRO)

# When multiple inheritance is involved, Python follows a specific order.

class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())

# method resolution order 
# MRO = search path for methods
# Python uses C3 linearization
# Ensures:
# Predictability
# No conflicts
# Logical inheritance flow

# What if Methods Exist in Multiple Classes?

# Let’s modify:
# class B(A):
#     def show(self):
#         print("B")
# class C(A):
#     def show(self):
#         print("C")
# Now:

# d = D()
# d.show()

#  Output:

# B
# Why?
# Because:

# D → B → C → A
# and B comes first.

#  Key Insight (Important )

# Even though both B and C inherit from A, Python avoids ambiguity by:

# Following left-to-right order
# Ensuring consistent hierarchy

# 3. No duplication

# Each class appears only once in the chain

#  Visual Structure
#         A
#        / \
#       B   C
#        \ /
#         D

# MRO flattens this into:

# D → B → C → A → object
        
# Python searches in this order:

# Look in D
# Then B
# Then C
# Then A  (found here)
# Stop searching

# Python uses something called the C3 Linearization Algorithm.

# Instead of guessing randomly, it follows three strict rules:

# 1. Left-to-right priority

# In:

# class D(B, C):

#  B is checked before C
# 2. Respect parent hierarchy

# Since both B and C inherit from A, Python ensures:
#  A comes after both B and C

# Why This Matters

# Without MRO + super(), this would break:

# A might get called multiple times 
# Order could become unpredictable 
# Multiple inheritance would be messy 

# Instead, Python guarantees:

#  Each class is called once
#  Order is consistent
#  Cooperative inheritance works smoothly

# # errors finding : ***************

# 1. Inconsistent Hierarchy (MRO Conflict)
#  Example:
# class A: pass

# class B(A): pass
# class C(A): pass

# class D(B, C): pass
# class E(C, B): pass

# # This will break
# class F(D, E): pass
#  Error:
# TypeError: Cannot create a consistent method resolution order (MRO)
#  Why this breaks
# Let’s look at the expectations:

# D wants: B → C
# E wants: C → B

# Now F(D, E) is trying to satisfy BOTH:
# B before C  
# C before B  

#  Impossible to satisfy both → Python refuses to create the class.
#  Insight
# MRO must be:
# Linear
# Consistent
# Respect parent order

# If not → hard error at class creation time

# error finding ******************
# 2. Breaking the super() Chain
#  Example:
# class A:
#     def process(self):
#         print("A")

# class B(A):
#     def process(self):
#         print("B")
#         # super() missing 

# class C(A):
#     def process(self):
#         print("C")
#         super().process()

# class D(B, C):
#     pass

# d = D()
# d.process()
#  Expected MRO:
# D → B → C → A
#  Output:
# B
#  What went wrong?
# D goes to B
# B does NOT call super()
# Chain stops 
# C and A never run
#  Insight

#  MRO still exists, but you broke the chain manually

# This is a silent bug—no error, but wrong behavior.

# olden Rule (Used by pros)

# If you use multiple inheritance:

#  Always use super()
#  Never call parent directly

# PART 14 — Composition (Professional Design)

# Instead of inheritance:

# class Engine:
#     pass

# class Car:
#     def __init__(self):
#         self.engine = Engine()

# “Has-a” instead of “is-a”

# Better design in real systems.


# example : 
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # composition

    def start(self):
        print("Car starting...")
        self.engine.start()

car = Car()
car.start()

# Why Composition is Better (Real Talk)
# Inheritance locks you into a rigid hierarchy. Composition gives you flexibility.
# Inheritance problem:

class ElectricCar(Car):
    pass

# What if:

# Electric cars don’t have the same engine?
# You need hybrid behavior?

# You end up with messy class trees.






