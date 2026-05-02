# mark_int =  int(mark)
# mark = input("input the mark of student:")

# if(mark_int >= 90):
#     print("grade A")
# elif(mark_int >80 and mark_int <90 ):
#     print("grade B")
# elif(mark_int >70 and mark_int <80 ):
#     print("grade C") 
# elif(mark_int >60 and mark_int <70 ):
#     print("grade D")   
# else:
#     print("fail")
  
# num = input("enter the number : ")
# num_int = int(num)
# 
# remender = num_int % 2 
# 
# if(remender == 0):
    # print("the input number is even")
# else:
    # print("the input number is odd")

# a = input("enter first number")
# b = input("enter second number")
# c = input("enter third number")
# 
# if( a>b and a>c):
    # print("the greatest number is first number",a)
# elif(b>c):
    # print ("the greatest number is second number",b)
# else :
    # print ("the greatest number is second number",c)

# a = input("enter the first movie name :")
# b = input("enter the second movie name :")
# c = input("enter the third movie name :")
# 
# list = [a,b,c]
# print(list)

# list = [1,2,3,4,5,5,4,3,2,1]
# list_copy =list.copy()
# list_copy.reverse()
# if(list_copy == list):
#     print("the list is palindrome")
# else:
#     print("the ist is not a palindrome")
# list = [1,2,"raam","sita","raam",2,1]
# list_copy =list.copy()
# list_copy.reverse()
# if(list_copy == list):
#     print("the list is palindrome")
# else:
#     print("the ist is not a palindrome")

# list = ["C","D","A","A","B","A"]
# list_count = list.count("A")
# print(list_count)

# dict = {
#     "table": "a piece of furniture" " " "/" " " "list of fact & figures",
#     "cat" : "a small animal"
# }
# print(dict)
# sub = {"python","java","c++","python","javascript","java","python","java","c++","c"}
# number_of_classroom = len(sub)
# print(number_of_classroom)

# marks = {}
# print(marks)
# a = int(input("enter physics mark :"))
# marks.update({"physics" : a})
# print(marks)

# b = int(input("enter chemistry mark :"))
# marks.update({"chemistry" : b})
# print(marks)

# c = int(input("enter maths mark :"))
# marks.update({"maths" : c})
# print(marks)



# a =int(input("enter your age :"))
# if(a<18):
#     print("you are not able to vote!!!")
# elif(18<a<=90):
#     print("you are able to vote!!")
# elif(a>90):
#     print("stay at home")
# else:
#     print("please make the voter id")


# a = input("Enter Your Name :")
# b = int(input(" enter your physics marks :"))
# c = int(input("enter your maths marks:"))
# d = int(input("enter your chemistry marks:"))
# e = int(input("enter your english marks :"))
# percent = ((b+c+d+e)/4)*100
# if(c<0 or c>100 or b<0 or b>100 or d<0 or d>100 or e<0 or e>100):
#     print("please enter the marks between 0-100 !!")
# elif(percent<35):
#     print("FAIL!!! , Grade = 'F'")
# elif(percent>=35 and percent<55):
#     print("JUST PASS !!! , Grade = 'D'")
# elif(percent>=55 and percent<60):
#     print("PASS!!!, Grade = 'C'")
# elif(percent>=60 and percent<75):
#     print("AVERAGE!!!, Grade = 'B'")
# elif(percent>=75 and percent<90):
#     print("GOOD!!!, Grade = 'A'")
# else:
#     print("EXCELLENT , Grace = 'A+'") 


# for i in range(1,100,2):
#     print(i)

# for i in range(0,101,2):
#     print(i)

# for i in range(20,101,20):
#     print(i)


# write a program to find largest number among three number:

# a =  int(input("enter your first number:"))
# b = int(input("enter your second statment:"))
# c =  int(input("enter your third number:"))
# if(a>b):
#     if(a>c):
#         print("the largest number is",a)
# else:
#     if(b>c):
#         print("the greatest number is",b)
#     else:
#         print("the greatest number is",c)



# a = input("Enter a value: ")
# b = "".join(reversed(a))
# print(b)
# if a == b:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")



# name = input("Enter a string: ")
# reverse = ""
# for i in name:
#     reverse = i + reverse
# print("Reversed string:", reverse)
# if name == reverse:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")



# sentance = "He is a good boy"
# len = len(sentance[3:5])
# print(len)


# sentence = input("Enter a sentence: ")
# word = input("Enter the word to find length: ")

# words = sentence.split()

# if word in words:
#     length = len(word)
#     print("Length of", word, "is:", length)
# else:
#     print("Word not found in the sentence")

# check whether  number is armstrong or not

# num = int(input(" enter the number :"))
# length = len(str(num))

# temp = num
# sum = 0

# while temp>0:
#     digit = temp % 10
#     sum += digit**length
#     temp = temp //10

# print(f"the number is {num} and sum is {sum}")
# if sum == num:
#     print("the number is armstrong")

# else:
#     print("the number is not armstrong")


# check number is palindrome

# num = input("enetr the number :")

# reverse = num[::-1]

# if( num == reverse):
#     print(" palindrome")
# else:
#     print(" not a palindrome :")


# method 2
# num = input("enetr the number :")

# reverse = ""
# for i in num:
#     reverse = i + reverse
# if( num == reverse):
#     print(" palindrome")
# else:
#     print(" not a palindrome :")

# us number ke saare digits ka sum

num = input("enter the number :")
ssum = 0
for i in num :
    ssum = int(i) +ssum  
print (ssum)