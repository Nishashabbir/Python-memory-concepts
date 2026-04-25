

# program 1 : bank account with scenrios using classmethods , static methods and other 

# class Bankaccount:
#     total_accounts=0
#     total_money=0

#     def __init__(self , name , balance):
#         self.name=name
#         self.balance=balance
#         Bankaccount.total_accounts+=1
#         Bankaccount.total_money+=balance

#     def deposit_money(self , amount):
#        if not Bankaccount.is_valid(amount): #here we connected the static method with bankaccount becuase that is the method of the class if we don't use that it will throw an error becuase python will see this function inside that function 
#         print("the amount is invalid ! ")
#         return
#        self.balance += amount
#        Bankaccount.total_money += amount
#        print(f"Your pkr{amount}/- have been deposited!")
       

#     def withdraw_money(self , amount):
#         if amount < self.balance or amount==self.balance:
#             self.balance-=amount
#             print(f"You just withdraw pkr{amount}\\- from your account ")
#             print(f"The remaining balance is {self.balance}")
#             Bankaccount.total_money-=amount
#         else:
#             print(f"The balance is insuffiecient! ")
# # here we are gonna use the class methods 
#     @classmethod
#     def bank_status(cls):
#         print(f"total accounts : {cls.total_accounts} and total money : {cls.total_money}")

# # now adding an additional functionality to learn the static methods here we go 
#     @staticmethod
#     def is_valid(amount):
#         return amount >0 #it will either return True or false 
    # now we can use it in the deposit money function to check if the deposit money is correct or not 

    # @staticmethod
    # def format_currency(amount):
    #     return f"PKR {amount}/-"
    
    # you can also use this function additionally 

# b1=Bankaccount("nisha" , 50000)
# b2=Bankaccount("ali" , 10000)
# b2.deposit_money(-20000)
# b1.withdraw_money(5000)
# print(b1.balance)
# print(b2.balance)
# print(f"total accounts : {Bankaccount.total_accounts} and total money : {Bankaccount.total_money}")
# we can use this statement for the bank status but the better way is to use the class methods that we have used at the end and instead of using bankaccount we would use cls for class directly just as we use self for the specific object 

# for privacy of the balance you will use __balance variable so that no one can access or change it but you still can if you write class.

# PART 10 — Dunder Methods (Magic Methods)


# operator overloading 

# class Box:
#     def __init__(self , value):
#         self.value=value 
#     def __add__(self, other):
#         return Box(self.value + other.value) #this operator will now add the object values as defined and return an other object 

# b1=(10)
# b2=(20)
# result=b1+b2 # here the + will use to add the object basically call goes from here for addition , result is also an object 
# print(result.value)


# class Box:
#     def __init__(self , value):
#         self.value=value 
#     def __add__(self, other):
#         return Box(self.value + other.value) #this operator will now add the object values as defined and return an other object 
#     def __repr__(self):
#         return f"the result is : {self.value}"

# b1=Box(10)
# b2=Box(20)
# result=b1+b2 # here the + will use to add the object basically call goes from here for addition , result is also an object 
# # print(result.value)
# print(result) #you can also print like this only when you defined __repr__ or __str__


# using comparison operator 
# class Box:
#     def __init__(self , value):
#         self.value=value
#     def __eq__(self, other):
#         return self.value ==other.value   #this method will be called through operator == when it will  is used 
# b1=Box(30)
# b2=Box(10)
# print(b1==b2) 

# using muliply  operator __mul__

# class Box:
#     def __init__(self , value):
#         self.value=value
#     def __mul__(self, other):
#         return Box(self.value * other.value )  
# b1=Box(30)
# b2=Box(10)
# # print(b1*b2) 
# # or you can use this method as well 
# result=b1*b2
# print(result.value) #no __repr__ function so you have to write like this :  result.value


# using multiply of object as well other than object i-e int 

# class Box:
#     def __init__(self , value):
#         self.value=value
#     def __mul__(self, other):
#         return Box(self.value * other )  
#     def __str__(self):
#         return str(self.value) #self.value might be an int, not a string But __str__ MUST return a string So Python expects: return "150"   # string Not: return 150     # int (bad for __str__) That’s why we write: return str(self.value)

# here we can not use just self.value  , in the str method we can only return smth in string " " like this so here we use a fix of str(self.value)

# b1=Box(30)
# print(b1*5)



# self.value  :	int	used for calculations
# __str_  : _ return	str	used for display



        
# practise of private variable methods and name mangling 

# class Student:
#     def __init__(self, name , age):
#         self.name=name
#         self.__age=age 
#     def get_age(self):
#         return self.__age
#     def __validate(self, age):
#         if age>0:
#             return True
#         else:
#             return False
#     def set_age(self , age):
#         if self.__validate(age):
#             self.__age=age 
#             return self.__age
#         else:
#             print("invalid") 

# s1=Student("nisha" , 20)
# print(s1.get_age())
# print(s1._Student__age) #this is name mangling (changes the name of the variable )
# print(s1.set_age(21))
# print(s1._Student__age) #all the statements are invalid 

# now instead of using s1.get_age() , like instead of calling  get_age() , we can normally call s1.age , but we get this behavior by creating a property mthod or property decorator (that we learnt above) , instead of creating get_age() functions , here we go : 

# class Student:
#     def __init__(self, name , age):
#         self.name=name
#         self.__age=age 
#     @property
#     def age(self):
#         return self.__age
# p=Student("nisha" , 20)   
# print(p.age)



# composition 
# passing the object outside the class as  a part 
# class Engine:
#     def __init__(self):
#         pass 
#     def start(self):
#         print("the engine is started ")

# class Car:
#     def __init__(self):
#         self.engine=Engine() #inside the class , connected with the other class 
# so through this self.engine we can call the properties of Engine() as well 
#     def start_car(self):
#         self.engine.start()
#         print("The car is started!")

        
# # lets create some objects here 
# c1=Car()
# c1.start_car()

#2 passing the object outside the class  as a part 
# class Engine:
#     def __init__(self):
#         pass 
#     def start(self):
#         print("the engine is started ")

# class Car:
#     def __init__(self, engine):
#         self.engine=engine 
#     def start_car(self):
#         self.engine.start()
#         print("The car is started!")

        
# # lets create some objects here 
# c1=Car(Engine())
# c1.start_car()



# simple dictionary 

# dict={
#     "name" : "Nisha" ,
#     "class" : "1.5"
# }

# # two methods to access 
# print(dict["name"])
# print(dict.get("class"))

# so we are now going to use this dictionary in a program where class can be used as object 


# input parser 

# class jsonparser():
#     def parse(self):
#         print("the json is parsing ")
# class xmlParser():
#     def parse(self):
#         print("the xml is being parsed ")

# def getparser():
    

#     parsers={  #this is the structure basically a better alternative of if else 
#         "json" : jsonparser ,
#         "xml" :   xmlParser
#     }
#     while True:
#         format_type=input("Enter a format type : json/xml : ")
#         parser_class = parsers.get(format_type)
#         if parser_class:
#             parser = parser_class()
#             parser.parse()
#         else:
#             print("Invalid format")
#         proceed = input("Do you want to continue? (y/n): ").lower()
#         if proceed == "n":
#             break

# getparser()


# Game Character System
# Different character types, same interface.

# class warrior:
#     def attack(self):
#         print("we have a sword attack!")
# class mage():
#     def attck(self):
#         print("A magician has attacked!")

# def battleground(character_class):
#     character=character_class() #here we created the object of that class 
#     character.attack()

# battleground(warrior)
# battleground(mage)


# adding the attributes to the  class  dynamically 
# first

# class A:
#     pass 
# def greet(self):
#     print(f"hello i am from Pakistan")

# A.greet=greet 
# a=A()
# a.greet()

# second

# def add_greet(cls):

#     def greet(self):  #you write self  whenever the function is meant to act as an instance method
#         print("hello ") # this function has returned a print statment so the outer function also has to return smth 
#     cls.greet=greet  #here we added an attribute 
#     return cls
# @add_greet #basically the class is being decorated 
# class user:
#     pass 

# u=user()
# u.greet()


# ORM 
class Model:
    def save(self):
       print(f"Saving {self.__class__.__name__}") 

class boher(Model):
    pass 
class rutherFord(Model):
    pass 

lists=[boher() , rutherFord()]
for list in lists:
    list.save()





    

