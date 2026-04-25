# 1. Sum of a list using recursion

def sum_lst(lst):
    if not lst :
        return 0
    return lst[0] + sum_lst(lst[1:]) #here slicing goes from the remaining element other than the first one at index 0 , it goes from index 1 to end 

result=sum_lst([1,2,3,4,5])
# print(result)

# 2- reverse a string using recursion

def reverse_str(string):
    if string == "" :
        return ""
    return reverse_str(string[1:]) + string[0]

result=reverse_str("abcd")
# print(result)

# 3-power function (a^b) using recursion

# power 3 of smth i-e 2 means multiply 2 with itself 3 times 2x2x2 
#a^b #it means Multiply a by itself b times”

# the base case will be a multiply with itself  0 times bringing 1 
def calc_pow(a , b):
    if b == 0:
        return 1
    return a * calc_pow(a , b-1)
result=calc_pow(4, 3)
# print(result)
# 2 3 ->  2^2  2^1 2^0
# Step 1:
# 2 * power(2, 2)
# Step 2:
# 2 * (2 * power(2, 1))
# Step 3:
# 2 * (2 * (2 * power(2, 0)))

# now unwind 
# 2 * (2 * (2 * 1))
# = 2 * (2 * 2)
# = 2 * 4
# = 8

# 4-Count digits of a number using recursion

def count_digits(number):
    if number<10:
        return 1
    return 1+ count_digits(number//10)
# so basically here we say that number greater than 10 will keep dividing unless they become 10 and when they become 10 or smaller we add 1 so that keeps happening until that 1's keep adding 

result=count_digits(198074)

# print(result)


# 5-Print numbers from n to 1 using recursion
def print_1_n(nmr):
    if nmr==0:
        return
    print(nmr)
    print_1_n(nmr-1)
# result=print_1_n(7)




