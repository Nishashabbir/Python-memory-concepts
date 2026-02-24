# what a function really is when you create this :


#1 function object in the memory 
# def greet():
#     print("Hello")
# here python doesn't store the code in the memory but the function object is created in the memory and greet variable points to that object 
# proof: 
# print(type(greet))
# x=greet #so we can store the name of function as variable and then call that variable as function then this is totally allowed 
# x()
# so the Functions are First-Class Objects.
#  What happens at x = greet
# When you do this, you are telling Python: "Make the variable x point to the exact same object that greet is pointing to."
# Python does not copy the function.
# Python does not run the function.
# It simply creates a new reference. now just two references x and greet variables are pointing to the same function object in the memory 

# print(id(greet))
# print(id(x)) # 3134576982880 same for the both 

# another example : 
# def adding(x,y):
#     print(x+y)
# a=adding
# a(4,5)

# 2. Functions Are First-Class Citizens

# you can store them as variables , pass them to the other functions and return them from the functions 
    
# def whisper(text):
#     return text.lower()
# def shout(text):
#     return text.upper()
# def speak(func):
#     print(func("Hello")) 
# speak(whisper)
# speak(shout)

# 3-parameter binding 

# def change(x):
#     x = 50

# a = 10
# change(a)
# print(a)
# print(change(a)) integers are immutable 

# why doesn't the value of a change ? because python pass the reference by value means the : functions get copy of the reference if :
# the object is immutable , no chagne outside 
# if the object is mutable , changes reflect 

# take another example of list: 

# def modify(lst):
#     lst.append(100)

# lst=[1,3,4,5]
# modify(lst) #unlike variables applying the modify function , the list changes becuase they are mutable 
# print(lst)
# Because both variables point to same object , so the list changes 

# look remember that the list changed becuase we use a modifying method on it , we didn't assign a new list like here it wont be changed : 

# def try_to_change(my_list):
#     # This creates a NEW list and rebinds the local variable 'my_list'
#     # It does NOT affect the original list outside
#     my_list = [100, 200, 300] #  as we didn't change it we reassigned using equal to sign 

# numbers = [1, 2, 3]
# try_to_change(numbers)
# print(numbers) # Output: [1, 2, 3] (Unchanged!) 

# this is the same as saying : 
# --- Immutable Example (Safe) ---
# x = 10
# y = x      # y points to the same 10
# x = 20     # x moves to a new rock (20). y stays at 10.
# print(y)   # Output: 10 (Safe!)

# --- Mutable Example (Dangerous!) ---
# list_a = [1, 2, 3]
# list_b = list_a  # list_b points to the SAME Backpack
# list_a.append(4) # We put a 4 in the Backpack

# print(list_b)    # Output: [1, 2, 3, 4] (list_b changed too!)


# -4. LEGB Rule (Scope Mastery)

# x = 10

# def outer():
#     x = 20

#     def inner():
#         print(x)

#     inner() #inner(): Python sees the parentheses (). It says "Okay, open the box and run the tool NOW. so that's why calling outer() will actually prints the x as well unlike the below property function 

# outer()
# inner() #you can't call it as if it is declared inside so it will be called inside as well 


# 5. Closures (This Is Where Pros Are Born)
# A closure is a function that remembers variables from its enclosing scope even after that scope is gone.

# here the outer function does two things declares x=10 and defines  inner and then return inner as function  so when it was stored in the func() , the inner was stored only but nothing is printed , only printed is x when we call func()

# def outer():
#     x = 10

#     def inner():
#         print(x)

#     return inner  #in above example we had called inner not returned so both of the functions are different 

# func = outer() #inner is stored here nothing printed , we didn't just refer outer to the function object we actually called outer function and that calling ended up returning inner without running inner AND WITHOUT BRACES OUTER WILL JUST RETURN WITHOUT PRINTING ANYHTING   
# func()  #inner is run and x is  printed  but if we store without braces like this fun=outer then outer will run calling func() which will return inner without printing anything 



# def greet():
#     print("Hello")
# # here python doesn't store the code in the memory but the function object is created in the memory and greet variable points to that object 
# # proof: 
# print(type(greet))
# x=greet #so we can store the name of function as variable and then call that variable as function then this is totally allowed 
# x()



# IN SHORT : 1. What outer() does (The Setup)
# When you run func = outer(), here is what happens inside outer:
# x = 10: It creates a variable x.
# def inner(): ...: It creates the function inner.
# Crucial Point: It does NOT run inner. It does NOT run print(x). It just defines what inner will do later.
# return inner: It stops and sends the inner function object back to you.
# Result of func = outer():
# Nothing is printed.
# func now holds the inner function object (which remembers that x is 10).
# 2. What func() does (The Action)
# Now you have the variable func holding that inner function. When you run func():
# Python executes the code that was inside inner.
# print(x): NOW it prints 10.


# 6- Default Argument Trap (Again, But Deeper)

# default argument are created once and we need a fix for them as we had learnt earlier 

# look this concept is about that two arguments needed but if you give one argument and other is defualt with this shape of code where defautl is empty list then python tracks the original list everytime but if you go to approach 2 then everytime when you rely on defualt it creates another list without changing the original 
# approach1:
# def add(item, lst=[]):
#     lst.append(item)
#     return lst

# print(add(1)) 
# print(add(2))
# print(add(3))
# # output: 
# [1]
# [1, 2]
# [1, 2, 3]
# only once the list is created and at every call python goes to the original list and changes it without creating a new list everytime 


# appraoch2 : fixed code 

# def add(item, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(item)
#     return lst

# print(add(1))
# print(add(2))
# print(add(3))

# # the output is : 
# [1]
# [2]
# [3]

# but better is that you don't rely on the default argument but send a list as well. 

# proof : check the id 
def add(item, lst=None):
    if lst is None:
        lst = []
    print("List id:", id(lst))
    lst.append(item)
    return lst

add(1)
add(2)
add(3)

# # 7-*args and **kwargs (Dynamic Functions)

# many paramerters without limiting 
# def total(*numbers):
#     return sum(numbers)

# print(total(1,2,3,4,5)) #this is how you send may arguments 

# here it converts into the dictionary of information as key value pairs 
def info(**details):
    print(details)

info(name="Nishu", age=21, country="Pakistan") #this is how you provide the data 

def info(**details):
    for key in details:
        print(key, "=", details[key])

info(name="Ali", age=22)


# remember : 
details={
    "name" : "nisha" ,
    "age" : 20
}
for key in details:
    print(details[key])


# 8-Closure With Independent State (VERY POWERFUL)

def counter():
    count = 0

    def increment():
        nonlocal count #this keyword says that don't create new count variable but remember the original one 
        count += 1
        return count

    return increment

c = counter() #inside c , increment() is stored ,  when we run counter() 

print(c()) # so here when we call c() , increment is run and its code inside simply increases from 0  to 1 
print(c()) # here again only increment is run and its code inside simply increases from 1 to 2
print(c()) # from 2 to 3 

# don't assume its a loop  and don't assume its outer() running again and again , its just increment stored in c and running again and again 









