#1 Mini challenge (DO THIS)

# Create a class:

# class Product:
#     def __init__(self, price):
#         self.price = price
# Add:
# __add__ → combine prices
# __mul__ → multiply price by discount factor
# __eq__ → compare prices



# solution : 
# class Product:
#     def __init__(self, value):
#         self.value = value
#     def __add__(self, other):
#         return Product(self.value + other.value)
#     def __mul__(self, other):
#         return Product(self.value *other.value)
#     def __eq__(self, other):
#         return self.value==other.value

# p1=Product(10)
# p2=Product(20)
# p3=Product(10)
# result=p1+p2 
# print(result.value)
# result2=p1*p2
# print(result2.value)
# print(f"the result is : {p1==p3}")

#2
# Mini challenge (IMPORTANT)

# Create this class:

# class Library:
#     def __init__(self, books):
#         self.books = books
# Add:
# __len__ → number of books
# __getitem__ → get book by index
# __setitem__ → replace a book


# solution : 

# class Library:
#     def __init__(self, books):
#         self.books = books
#     def __len__(self):
#         return len(self.books)
#     def __getitem__(self, index):
#         return self.books[index]
#     def __setitem__(self, key, value):
#         self.books[key]=value

# b1=Library(["English" , "Urdu " , "Maths" , "Bio"])
# print(len(b1)) # here we don't need to write b1.books as we already defined the functionality in the dunder methods 
# print(b1[2]) # b1[2] gives a book 
# b1[1]="chemistry"
# print(b1.books)
# answers : 
# 4
# Maths
# ['English', 'chemistry', 'Maths', 'Bio']


# from composition topic 
# payment processor and differennt payment methods 
# creditcard , paypal , crypto , processor to use composition 

# class CreditCardPayment:
#     def pay(self, amount):
#         print(f"Paid {amount} using Credit Card")

# class PayPalPayment:
#     def pay(self, amount):
#         print(f"Paid {amount} using PayPal")

# class CryptoPayment:
#     def pay(self, amount):
#         print(f"Paid {amount} using Crypto")

# class PaymentProcessor:
#     def __init__(self, payment_method):
#         self.payment_method = payment_method   #  Composition

#     def process_payment(self, amount):
#         self.payment_method.pay(amount)  


# # Add new payment WITHOUT touching existing code
# class JazzCashPayment:
#     def pay(self, amount):
#         print(f"Paid {amount} using JazzCash")  



# processor1 = PaymentProcessor(CreditCardPayment())
# processor1.process_payment(100)

# processor2 = PaymentProcessor(PayPalPayment())
# processor2.process_payment(200)

# processor3 = PaymentProcessor(CryptoPayment())
# processor3.process_payment(300)


# processor = PaymentProcessor(JazzCashPayment())
# processor.process_payment(500)


# This is used in real systems

# This pattern is basically:

# Strategy Pattern
# Dependency Injection

# Used in:

# Payment gateways (Stripe, PayPal APIs)
# Authentication systems
# Notification systems


# INDRive system 

class bike_ride:
    def calculate_fare(self, distance):
        return distance*20
class car_ride:
    def calculate_fare(self, distance):
        return distance*30
class inDrive:
    def __init__(self , ride_type):
        self.ride_type=ride_type
    def pay_fare(self , distance):
        return self.ride_type.calculate_fare(distance)
    
c1=inDrive(bike_ride())
print(f"The price is : Rs {c1.pay_fare(20)}\\-")

    

# uisng decorators :
# Decorator is automatically called with the function/class as input

# plugins=[]

# def register(cls):
#     plugins.append(cls)
#     return cls

# # to prevent calling the register again and again , better use a decorator that directly calls the function and passes the classes to it whenver they're created 
# @register
# class loginPlugin:
#     def runPlugin(self):
#         print("login plugin is running! ")
        
# @register
# class paymentPlugin:
#     def runPlugin(self):
#         print("Payement is processing! ")


# for plugin in plugins:
#     plugin().runPlugin() #here object plugin() is created and then the methods inside it were called 


# decorator automatically calls the function 

# 2. Dynamic Object Factory (Real-world: APIs, file handlers)

# Instead of messy if-else, let classes handle creation.

# class JSONParser:
#     def parse(self):
#         print("Parsing JSON")

# class XMLParser:
#     def parse(self):
#         print("Parsing XML")

# def get_parser(format_type):
#     parsers = {
#         "json": JSONParser,
#         "xml": XMLParser
#     }
#     return parsers.get(format_type)

# parser_class = get_parser("json") #function called and a class is recieved which is assigned to the parser_class variable which we already said , a class can be assigned like that 
# parser = parser_class()  #here we are creating the object of that class 
# parser.parse() #and here we are using the function/method of that class

# Deep Understanding Question

# Predict:

class A:
    x = []  

a1 = A()
a2 = A()

a1.x.append(1)

print(a2.x)

# If you understand class variables deeply, you’ll know why.

# solution : 
# So when you do:
# a1.x.append(1)
# you’re not modifying something unique to a1 — you’re modifying the single shared list stored on the class A.
# Both a1.x and a2.x point to the same list object, so:
# print(a2.x)
# shows the updated list:
# [1]
# If you want each instance to have its own list, you need to use an instance variable:
# class A:    def __init__(self):        self.x = []
# Now each object gets its own separate list, and modifying one won’t affect the other.
# so basically x=[] is being shared among all until unless you define it for each instance differently by the init

# PART 20 — The Level-Up Question
# Why does this fail?

# class A:
#     def __init__(self, x=[]):
#         self.x = x
# Hint: Default arguments are evaluated once.
# This single concept separates intermediate from advanced Python developers.


# What happens in your code

class A:
    def __init__(self, x=[]):
        self.x = x

# The key idea:
# Default arguments are evaluated once at function definition time, not each time the function is called.
# So Python does this internally:
# It creates one single list []
# That same list is reused every time __init__ is called without x

# So what goes wrong?
# Let’s see:
# a1 = A()a2 = A()a1.x.append(1)print(a2.x)
# You might expect:
# []
# But you actually get:
# [1]
# Why?
# Because both a1.x and a2.x point to the same shared list object created once as the default value.
# So:

# a1.x.append(1) modifies the shared list
# a2.x sees the same modified list

# solution : 
# Correct way to write it
# Use None as a sentinel:
# class A:    def __init__(self, x=None):        if x is None:            x = []        self.x = x
# Now:

# Each instance gets a fresh list No accidental sharing

# Why this matters (the “advanced Python” insight) This concept tests whether you understand: Function objects are created once
# Default arguments are stored in the function’s internal __defaults__
# Mutable objects can silently create shared state across instances
# That’s why experienced Python developers avoid mutable defaults entirely.
# If you want, I can show you how this same bug appears in real-world Django/FastAPI code — it shows up more often than people expect.


# more explanation of using None : 
# What actually happens with x=None
# class A:
#     def __init__(self, x=None):
#         if x is None:
#             x = []
#         self.x = x
# Step-by-step when you do:
# a1 = A()
# No argument is passed → x becomes None

# Code runs:

# if x is None:
#     x = []
# So a new list is created inside the function
# # Then:
# self.x = x
# assigns that new list to a1.x
# Now second object:
# a2 = A()
# Same process again:
# x is None
# New list is created again
# Assigned to a2.x So a1.x and a2.x are different lists
# Q-
# What if I pass a list manually?
# Example:
# a1 = A([1,2])
# a2 = A([3,4])
#  What Happens Here?  Each time you call:
# A([1,2])
# You are creating a new list object manually. So memory becomes:
# a1.x → [1,2]
# a2.x → [3,4]
# Now they are completely independent.
# A() → x is None, so a new empty list is created inside __init__, and self.x points to it.
# A([]) → x is an empty list you passed in, so self.x points to that same list (no new list created).
# A([1,2]) → x is a non-empty list you passed in, so self.x again points to that same list (shared with the caller).