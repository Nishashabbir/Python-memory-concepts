
# Q1
# Get squares of numbers divisible by 3 from 1–20

sqaures=[x*x for x in range(1, 20) if x%3==0]
# print(sqaures)

# Q2

# From:

words = ["apple", "banana", "cherry"]

# Get list of lengths
lengths=[len(word) for word in words]
# [len(word) for word in ["apple", "banana", "cherry"]] #or you can also write like this 
# print(lengths)

# Q3

# Flatten:

matrix=[[1,2,3], [4,5], [6]]

nums=[ num for row in matrix for num in row ]
# print(nums)

# Q4

# From:

nums = [1,2,3,4,5]

# Create:

# ["low", "low", "low", "high", "high"]

status=["low" if s<=3 else "high" for s in nums ]
# print(status)

# Q5 (slightly tricky)

# Get all pairs (x, y) where:

# x from 1–3
# y from 1–3
# x != y

# pairs=[(x,y) for x in range(1,4) for y in range(1,4) if x!=y]
# pairs=[(x,y) for x in range(1,4) for y in range(1,4) and x!=y] #this is invalid 
# p=[(x, y) for x in range(1, 4) for y in range(1, 4) if x != y]
# print(p)
# print(pairs)




