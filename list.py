# list method
# list = [2,3,4]
# list.append(1) # add one new element at the end of the list . list.append(element)
# print(list)
# list.sort() # arrange list in ascending order
# print(list)
# list.sort(reverse=True) #arrange in decending order
# print(list)


# list = ["apple","mango","banana"]
# list.sort()
# print(list) #string me arrangment first  alphabate ke according hota hai
# list.sort(reverse=True)
# print(list) 

# list = ["a","n","f","d","f"]
# list.reverse() #reverse whole string
# print(list)

# list = [2,4,6]
# list.insert(1,0) #list.index(indexnumber,element) vo index number jha p hmme new element add krna hai 
# print(list)

# list = [1,0,3,2,0,4,0]
# list.remove(0) #list.remove(element) it remove the typed element which were occuring first  in list
# print(list)
# list.pop(2) #list.pop(indexnumber) it directly remove the number from respected index number
# print(list)


# SLICING IN LIST

a = [2,3,4,5,5,90,89,78,67,78,56,798,56,423789,78,98,827,8]
# print(a[0:9])

# print(a[::2]) # print element by skipping 1 elements double (::) is used to skipping the gap between slicing

print(a[0:11:3])  # 0 = starting index , 11 = go up to index 11 but not include it, 3 = jump 3 index each time


#1) list slicing mylist=[32,4,5,6,7,8,1,2,3,9,0,122,10,2,3,4,3,3,2]
#a) print element [1,2,3] using slicing concept
#b) print element [9,0,122,10,2,3]
#c) print elements [8,1,2,3,9,0,122,10,2,3,4,3,3,2]
#d) print elements [10,2,3,4,3,3,2]
#e) print elements [10,3,3,2]
#f) print elements [6,8,2,9]
#g) print elements [1,0,3,2]

# mylist=[32,4,5,6,7,8,1,2,3,9,0,122,10,2,3,4,3,3,2]
# print(mylist[6:9])
# print(mylist[9:15])
# print(mylist[5:])
# print(mylist[-7:])
# print(mylist[-7::2])
# print(mylist[3:10:2])
# print(mylist[6::4])




# stack oeration using list

# stack ek data structure hai jisme data LIFO principle p kaam krta hai "LIFO =Last In First Out" matlab jo element sabse last me add hoga vo sabse phele remove hoga .  Example : stack of plates - tumne plate rakhi 1 , fir 2 , fir 3 abb agar plate uthani hai to 3 sabse pehle niklegi, fir 2, fir 1.

# Stack me main operations:
# Push → element ko stack me add karna
# Pop → last element ko remove karna
# Peek / Top → last element ko dekhna (remove nahi karte)


# stack = []
# for i in range(4):
#     n= int(input("enter the element to enter into stack"))
#     print(n,"is inserted into stack")
#     stack.append(n)
#     print("the top element in the stack is ", stack[-1])

# print("your stack is",stack)

# print("\n")

# print("pop operation")
# n = int(input("enter 1 for pop operation \n enter 2 for check stak is empty or not"))
# if(n==1):
#     print("i am poping the element from the stack :",stack[-1])
#     stack.pop()
#     print(stack)
# elif(n==2):
#     if (not stack):
#         print("stack is empty")
#     else:
#         print("stack is not empty")



#write a code to reverse a number using stack function

# stack = []

# num = input("Enter a number: ")

# # Push digits into stack
# for digit in num:
#     stack.append(digit)
# print(stack)

# # Pop digits to reverse
# reverse = ""

# while stack:
#     reverse = reverse + stack.pop()

# print("Reversed number is:", reverse)


# Palindrome using Stack

stack = []
num = input("enter the number to check :")

for digit in num :
    stack.append(digit)
print(stack)

reverse= ""

while stack :
    reverse = reverse + stack.pop()
print(reverse)

if(stack == reverse):
    print("the number is pallindrome")
else:
    print("number is not palindrome")