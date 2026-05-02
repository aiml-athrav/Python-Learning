# # functions:

# # 1. FUNCTION WITHOUT PARAMETERS AND ARGUMENTS

# def sumfun() : # def is used to form a function (line 4,5,6,7 is the data a function can store)
#     a = 4           
#     b = 5
#     sum = a + b
#     print(sum)

# sumfun()    #calling a function it will gave the same result according to the data as much as function call same output we get)

# # .......1000 lines of code

# sumfun()

# # .......1000 lines of code

# sumfun()

# # write a function name welcome_message() that print " welcome to python programming!" three times.

# def welcome_message() :
#     print("welcome to python programming")

# welcome_message()
# welcome_message()
# welcome_message()

# # Define a function inspire() that print a motivational quotes with your name

# def inspire():
#     print("build a realition with every one but donot depend on every one .... 'ATHRAV'")

# inspire()

# # FUNCTION WITH PARAMETERS AND ARGUMENTS:

# def average(a,b):    # here a and b is a parameter on with function is working
#     average_value = ((a+b)/2)
#     print("average value is:",average_value)

# average(3,4)   # here (3,4) is a agrument which is assigning on parameters
# average(45,98)


# #  default parameters values

# def average(a = 20,b = 40):    # here a and b is a parameter on with function is working and there values is already assigned
#     average_value = ((a+b)/2)
#     print("average value is:",average_value)

# average()  # if we do not gave any value of a and b then in build value is used 
# average(2,9)

# hmm default value second ko de sakte hai phele ko bina diye prr phele ko default value deke dusre ko nhi de to error aayega 
# def cal_prd(a,b=3):
#     return a*b
# x = cal_prd(1)
# print(x)    # output is 3 because  we gave a=1 in x value its is true do not get any error becuse we do not define first value

# def cal_prd(a = 3,b): # this show error in first line because we have define first value but do not define second value if first value is define in starting so it is compulsary to define second value also
#     return a*b
# x = cal_prd(1)
# print(x)  


# # write a function show_age(name,age) that print : athrav khandelwal is 19 yr old

# # method 1.
# def show_age(name , age):
#     print(f"{name} is {age} year old")

# show_age("athrav khandelwal , 19")

# # method 2.
# def show_age(name , age):
#     print(f"{name} is {age} year old")
# name = input("enter your name")
# age = input("enter your age")

# show_age(name,age)

# # method 3.
# def show_age():
#     name = input("enter your name: ")
#     age = input("enter your age: ")
#     print(f"{name} is {age} year old")

# show_age()

# # method 4.
# def show_age(name=None, age=None):
#     if name is None:
#         name = input("enter your name: ")
#     if age is None:
#         age = input("enter your age: ")
    
#     print(f"{name} is {age} year old")

# show_age()
# show_age("athrav khandelwal , 19")

# write a function square(num) that return the square of the number

# def square(num) :
#     square = num**2
#     print(square)

# square(4)

# def square(num):
#     return  num**2
# print(square(2))

# difference between return and normal functiom

# def square(num):
#     print(num**2)

# x = square(4)     #output = 16
# print(x)          #output = none  x me koi use ful value store nhi hui na haam x ko apne program m khi further use kr sakte hai 


# def square(num):
#     return num**2

# x = square(4)      # output = 16
# print(x)           # output = 16  x me useful value 16 store hui return k kraran aab hamm is x ki value ko khi bhi use kr sakte hai



# write a function to print the length of a list 

# method 1
# hero = ["ram", "sita", "lakshman"]

# def ramayan():
#     print(len(hero))

# ramayan()

# # method 2
# hero = ["ram", "sita", "lakshman"]
# fruit = [ "apple" , "banana", "chikku" , "papaya"]
# def ramayan(list):
#     print(len(list))

# ramayan(hero)
# ramayan(fruit)

# write a function to print the element of a list in a single line

# fruit = [ "apple" , "banana", "chikku" , "papaya"]
# def chintu(list):
#     for i in list:
#         print(i , end =" ")

# chintu(fruit)


# write a  function to find the factorial of n 

def fact_num():
    n = int(input("enter the value of n :"))
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print("factorial is :",fact)

fact_num()