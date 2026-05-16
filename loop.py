# i = 0
# while i<50 :
#     print("athrav",i)
#     i+=1
# print(i)

# i = 50
# while i>=1 :
#     print(i)
#     i-=1
# print("loop ended")

#print number 1 to 100:
# i = 1
# while i<101:
#     print(i)
#     i += 1
# print("loop ended")

#print number 100 to 1:
# i=100
# while i>= 1:
#     print(i)
#     i-=1
# print("loop ended")

# print the multiplication table of number n:

# n= int(input("enter the value of n :"))
# i = 1
# while i <=10:
#     multiplication = n*i
#     print(multiplication)
#     i+=1

#Print the element of the following list using loop:
# list = [1,4,5,7,8,9,654,67]
# index = 0
# while index<len(list):
#     print(list[index])
#     index +=1

# search for a number x in this tuple using loop :
# tuple = (1,4,9,16,25,36,49,64,81,100)
# print(tuple)
# x = int(input("enter the number :"))
# indx = 0
# while indx <len(tuple):
#     if(tuple[indx]==x):
#         print("index number is", indx)
#         break
#     indx+=1

# i = 1
# while i <= 10:
#     if(i == 5):
#         i += 1
#         continue  # skip 5 continue further
#     print(i)
#     i+=1


#printing odd number using continue
# i = 1
# while i<=20:
#     if(i % 2 == 0):
#         i +=1
#         continue
#     print(i)
#     i+=1


#printing even number using continue
# i = 1
# while i<=20:
#     if(i % 2 != 0):
#         i+=1
#         continue
#     print(i)
#     i+=1


#for loop

#for i in range(10):
#    print(i)

# for i in range(1,101):     #start with 1 and end with 100 last digint -1 number print hota hai end me
#     print(i)

# for i in range(0,101,5):  #start with 0 reach to 100 by skiping 4 digit because we have taken 5 means print 5th number after 0 than 5th than so on
#     print(i)

# for i in range(-10,0):
#     print(i)

# while loop problems

# print number 1 to 100 and it should be only even number
# i = 2
# while i<=100:
#     print(i)
#     i =i+2

# print number 1 to 100 and it should be only odd number
# i = 1
# while i<=100:
#     print(i)
#     i =i+2

# print number 1 to 100 and break when value = 51
# i = 1
# while i<=100:
#     print(i)
#     if(i == 51):
#         break
#     i =i+1

# print number 1 to 100 and continue when value = 43
# i = 1
# while i<=100:
#     i = i+1
#     if(i == 43):
#         continue
#     print(i)
    

#print the sum of number in a list number = [1,2,3,4,5]
 
# #method 1
# number = [1,2,3,4,5]
# print(sum(number))

# #medhod 2 using function
# number = [1,2,3,4,5]
# sum_of_number = 0
# for i in number:
#     sum_of_number = sum_of_number + i
# print("sum",sum_of_number)


# # print the even numbers from the list 

# numbers = [1,2,3,4,5,6,7,8,9,54,67,46,22,56,78,98,0]
# for i in numbers:
#     if( i % 2 == 0):
#         print("even number is", i)


# print the revesre of list 

#method 1 to reverse any value
# a = input("Enter a value: ")
# b = "".join(reversed(a))
# print(b)

#method 2
# number = [1,2,3,4,5,6,7,8,8,9]
# reverse = number[::-1]
# print(reverse)
 

#method 3
# number = [1,2,3,4,5,6,7,8,8,9]
# reverse = ""
# for i in number:
#     reverse = str(i) + reverse
# print(reverse)

#method 4
# number = [1,2,3,4,5,6,7,8,8,9]
# reverse = []
# for i in number:
#     reverse = [i] + reverse
# print(reverse)


# WRITE A PYTHON PROGRAM THAT PRINT THE SUM OF N NATURAL NUMBER

# n= int(input("enter the number :"))
# sum =0
# temp = n
# while n>=1:
#     sum =sum+n
#     n-=1
# print(f"continous sum of natural number {temp} is {sum}") #print statment m f lagane se hmm kisi bhi variable ko curley bracket m daal k use print statment me use kr sakte h

# print the pattern
# *
# * *
# * * *
# * * * *

# n=1
# while n<=4:
#     print("*" *n)
#     n+=1


# print the table of any number

# n= int(input("enter the number :"))

# i=1
# while i<=10:
#     print(f"{n} x {i} =",n*i)
#     i+=1

# i = 0
# while i < 5 :
#     print (i)
#     i += 1

# n = int(input("enter the number :"))
# number =[]
# for i in range(1,n+1):
#     number.append(i)
# print(number)
# number = number[::-1]
# print(number)

num  = input("enter the number :")
number =[]
for i in num:
    number.append(i)
reverse = number
reverse = reverse[::-1]
if (reverse == number ):
    print ("no. palindrome")
else:
    print("not palindrome")