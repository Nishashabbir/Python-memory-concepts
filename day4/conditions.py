
# memory and by value check 

# a = []
# b = []

# if a == b: #checks the value 
#     print("Equal")

# if a is b:  #checks by memory 
#     print("Same object")


# Because empty list is falsy.
# if []:
#     print("True")
# else:
#     print("False")
# Output:
# False

#  — Condition Using Variables Directly
# Instead of:
# if x != 0:

# You can write:

# if x:

# Cleaner.

# — Logical Operators (AND, OR, NOT)

# AND → both must be True
# if age > 18 and age < 30:
# OR → at least one True
# if x == 5 or x == 10:
# NOT → reverses :

# if not logged_in:

# — How AND and OR Really Work (Short-Circuiting)
# Example:

# if False and print("Hello"):
#     pass

# print never runs.

# Because False AND anything is False. anything with NOT in And operation will never execute as it is false 

# — Conditions Return Values (Not Just True/False)
# Example: AND operator ************
# x = 5 and 10
# print(x)
# Output:
# 10
# Why?
# AND returns last true value.
# example: 

# x = 0 and 10   (0 AND 10 is zero obviously )
# print(x)
# Output:
# 0
# Because 0 is falsy.

# OR example:*****************

# x = 0 or 10
# print(x)
# Output:
# 10

# Returns first truthy value.

# Professional use:

# name = input() or "Default"

# — Nested Conditions
# age = 20
# citizen = True

# if age >= 18:
#     if citizen:
#         print("Eligible")

# Used in authentication systems.

# — Ternary Operator (Professional Shortcut)

# Instead of:

# if age >= 18:
#     status = "Adult"
# else:
#     status = "Minor"

# # Write:
# status= "adult " if age >=18 else "minor "
# # clearer

# — Condition with Objects

# Example:

# user = {"name":"Ali"}

# if user:
#     print("User exists")

# Dictionary exists → truthy.

#  — Membership Operator

# Check existence.

# if "a" in "apple":

# True.

# if 5 in [1,2,5]:

# True.

# — Condition with Functions
# def is_even(x):
#     return x % 2 == 0

# print()
# if is_even(4):
#     print("Even")

# # Functions return True/False.

# # — Dangerous Condition Trap
# x = None

# if x == None:

# Professional way:

# if x is None:

# Always use is with None.

# — Multiple Condition Trick

# if 0 < x < 10:

# Python supports chained comparison.

# Better than:

# if x > 0 and x < 10

# e.g
x=10
if 0 < x >9: 
    print("yes ")

# — Real Backend Example

# Authentication:

# if user and password_correct and not banned:
#     allow_access()
# else:
#     deny()

# # — Professional-Level Trick
# x = [1,2,3]

# print(x.append(4))# as append returns None
# print(x) #[1, 2, 3, 4]
# if x.append(4):
#     print("True")
# else:
#     print("False")

# Output:

# False
# Because append returns None.
# Even though list changed.

x = []

if x or True: # same like 0 OR 1 is 1 so A prints 
    print("A")

if x and True:  # 0 and 1 is 0 as false so nothing executes 
    print("B")

if not x:    # not True is false and so empty list was also false so C prints 
    print("C")