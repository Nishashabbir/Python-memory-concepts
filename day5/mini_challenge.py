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

class Library:
    def __init__(self, books):
        self.books = books
    def __len__(self):
        return len(self.books)
    def __getitem__(self, index):
        return self.books[index]
    def __setitem__(self, key, value):
        self.books[key]=value

b1=Library(["English" , "Urdu " , "Maths" , "Bio"])
print(len(b1)) # here we don't need to write b1.books as we already defined the functionality in the dunder methods 
print(b1[2]) # b1[2] gives a book 
b1[1]="chemistry"
print(b1.books)
# answers : 
# 4
# Maths
# ['English', 'chemistry', 'Maths', 'Bio']