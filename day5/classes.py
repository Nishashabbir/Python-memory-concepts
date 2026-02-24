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
class dog:
    sepecie = "canine "  #class variable  equally shared by every object 
    def __init__(self , name):
        self.name=name   #instance variable unique to every object 
    
d1=dog("A")
d2=dog("B")

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
class Person:
    population = 0
    
    def __init__(self):
        Person.population += 1

    @classmethod
    def get_population(cls):
         cls.population
p1=Person()
p2=Person()
p3=Person()

print(Person.population)
# Person.population=99 #remember that anyone can change this data ,so better use a private class 
print(Person.population)

# NOW A BIG QUESTION WHY SHOULD WE USE CLASS METHODS WHEN WE CAN DO CREATE THE SAME FUNCTIONALITY AND USE THEM ON OBJECT LEVEL ..? 
# THE ANSWER IS IN class.txt ___ its all about the logical use of class methods 