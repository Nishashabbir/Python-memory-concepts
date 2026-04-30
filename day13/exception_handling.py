
# Q1

# Handle division safely:

# while True:
#     result=None
#     try:
#         a = int(input("Enter the first number : "))
#         b = int(input("Enter the second number : "))
#         result= a/b  # try the sensitive code 
#         # handle different errors gracefully 
#     except ZeroDivisionError:
#         print("Can't divide by zero")   #handle error 
#     except ValueError:
#         print("invalid input")
#     else:  #if no error occurs , this will print only then 
#         print("This is alright")
#     finally:
#         print(f"This is the result no matter what : {result}") #this will print even if there is any error or not 

#     proceed=input("Do you want to do again ? y/n : ").lower()
#     if proceed=="n":
#         break


# multiple errors 
# try:
#     x = int(input())
#     print(10 / x)
# except (ValueError, ZeroDivisionError):
#     print("Invalid input or division by zero") #combine the errors 


# if you don't know the error you can also print the error message 

# try:
#     a = int(input("Enter the first number : "))
#     b = int(input("Enter the second number : "))
#     result= a/b

# except Exception as e:
#     print("There is an error " , e)
# else:
#     print(f"here is the result : {result}")
    
# story : 
# try this code if prints then ok, otherwise  handle this error 
    

# raising the error , manually you can create the error 

# age = int(input("Enter age: "))

# if age < 18:
#     raise ValueError("You must be at least 18")
# else:
#     print("Thank you for voting..!")


 
# ///////////////////////////////////////////////////
# exercises 
# Q-1
# Handle:

# division by zero
# invalid input
# try:
#     a = int(input("Enter a: "))
#     b = int(input("Enter b: "))
#     print(a / b)

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# except ValueError:
#     print("Please enter valid integers")

# # Q-2
# # Ask user for a number and print its square
# # Handle wrong input

# try:
#     num=int(input("Ask a number "))
# except ValueError:
#     print("wrong input ")
# else:
#     print(num**2)
# finally:
#     print("\nprogram is alright ")

#  Handle:

# division by zero
# invalid input

# Q-3
# Open a file safely:
#  Handle file not found

# try:
#     f=open("guide.txt")
#     print(f.read())
# except FileNotFoundError:
#     print("file not found error bro! ")
# finally:
#     print("process done!")

# # Better version (no leak):

# try:
#     with open("data.txt") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("File not found")
    

# Q-4

# class NegativeNumberError(Exception):#You are not passing an argument here. This is inheritance, not a function call.
#     pass # NegativeNumberError is a class which inherits Exception which is also a class to behave like this “Create a new class called NegativeNumberError that behaves like Exception.” So: Exception = parent class NegativeNumberError = child class

# try:
#     num = int(input("Enter number: "))

#     if num < 0:
#         raise NegativeNumberError("Negative number not allowed") #here NegativeNumberError is being called as an object of the class we created , and passing that message is like argument 
# # as raise means throw error and except means catch that error , so if error is raised the execution jumps to except 
#     print("Square:", num ** 2) 

# except NegativeNumberError as e: #here that message will be printed 
#     print(e)

# except ValueError: #this is a built in error type while the one we created  above is the custom one for which we created the class 
#     print("Invalid input")



# handle sqaure of number 

# wrong program 
# try:
#     num=int(input("Enter a number "))
#     print(num**2) #here if a negative number is given , you will first print and then handle the negative , which is logically not correct 
#     if num<0:
#         raise NegativeNumberError("negative number is not allowed")
        
# except NegativeNumberError as e:
#     print(e)
# except ValueError:
#     print("invalid input")


# Q-5
# Create a program:

# Ask for filename
# If file doesn't exist → show error using as e
# Always print: "Program ended" using finally


# try:
#     name=input("Enter a name of file : ")
#     f=open(name) # you can also use the better line for this below 
#     ## with open(filename) as f:
#     print(f.read())

# except FileNotFoundError as e:
#     print("Error" , e)
# finally:
#     print("process done ")
# simply if you have the file open it , else handle the error if not found , we are not generating any error manually here by using raise 

# Q-6 
lst = [1, 2, 3]
# print(lst[5])

#  Catch the correct exception and print a custom message.
# try:
#     print(lst[5])
# except IndexError:
#     print("index out of bound!")
    
# Q-7 
# Write a function:
# def divide(a, b):
# Rules:
# If b == 0 → raise exception
# If inputs are not numbers → handle properly
# Return result if valid


# def divide(a , b):
#     try:
#         if b==0:
#             raise ZeroDivisionError ("can not divided by zero ") #throw an error if b==0 
#         return a/b
#     except ZeroDivisionError as e: #catch the error that was thrown and handle it gracefully
#         print(e)



# print(divide(20 , 10))
# print(divide(20 ,0))

# # better version 
# def divide(a, b):
#     try:
#         if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
# #   in this line a and b has to be integer or float and if they are not numbers then we will throw a type error 
#             raise TypeError("Inputs must be numbers")

#         if b == 0:
#             raise ZeroDivisionError("Cannot divide by zero")

#         return a / b

#     except TypeError as e:
#         return f"Type Error: {e}"

#     except ZeroDivisionError as e:
#         return f"Math Error: {e}"


# isinstance is used to check the type of number 
# # isinstance(x, type)
# isinstance(0.5 , float)
# isinstance(5 , (int , float))


# logging 


import logging

logging.basicConfig(
    filename="simple.log",
    level=logging.ERROR,
    format="%(levelname)s: %(message)s"
)

# this will help create a file to store the details of the error as best practise  , if you don't write this , the file will not be created 
try:
    num = int(input("Enter a number: "))
    print(f"Square is {num**2}")

except ValueError as e:#the e that we printed we can also log it 
    print("Invalid input")
    logging.error("ValueError: %s", e)
        # logging.error("ValueError occurred", exc_info=True) #better use this line 


finally:
    print("Process ended")

# %s is a placeholder
#  It means: “put the value of e here as a string” This is old Python string formatting style (called printf-style formatting).
# %s → string
# %d → integer
# %f → float

# Example:

# logging.error("Number: %d", 5)