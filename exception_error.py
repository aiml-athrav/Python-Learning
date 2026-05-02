# EXCEPTION ERROR

# EXCEPTION :- exception are unexpected event or error that occur during the execution of a program which discrupt the normal flow of the programm

a = int(input("enter the number :"))

print(10/a)  # here if the user enter 0 as a number then according to mathematics  it is undefined value but python show zero error and this error  stop the flow of code and further code do not run to solve this we do execption error handling 

print("i have do the division")
# just like this zero error we have many un expected error  to solve these error problem we use some keywords which have there specific meaning to solve these error problem

# keywords = try , except , else , finally , raise

# this is the condition when we what exception error should be occur
a = int(input("enter the number :"))

try:             # try keyword hmm use krte hai  us line of code ko wrap krne k liye jo error produce kr sakti hai try keyword ko use krne k liye hmme dusra ek aur keyword use krna hota hai vo except keyword ya finally keyword
    print(10/a)  

except ZeroDivisionError:        # exception ko hmm try k sath use krte hai takki jo error aa rha hai use exception m daal ke error show hone ki jgha hamra print statment run ho aur uske baad aage k code run ho 
    print("an error is occured  you cant't divide by zero")

else:        # else same if else jesa hii kaam krta hai agr koi exception error nhi aata hai to else sttment run krte hai
    print(" good there is no exception")

finally:      # ye ek esa keyword hai jo run krega hi krega cahye error aaye ya na aaye
    print("i will run no matter what")

print("i have do the division")





# this is the condition when we didn't know what error should be occur
a = int(input("enter the number :"))
try:
    print(10/a)

except Exception as err:       # this except condition is used jaab hmme nhi pata kya error aa sakta hai to hmm saare error ko expection man k ek err / er / e variable name de dete hai
    print(f"an error occur which is {err}")


# the one important keyword is raise  :- raise ki help se hmm manually error define krva sakte hai 

age = int(input(" tell your age :"))
if age<10 or age>18 :
    raise ValueError("your age must be between 10 to 18")
else:
    print("welcome to club ")

print(" the club will start soon :")
# yha pe hmmne khud se error to define kr diya prr agr if vali condition hui to error jo hmmne define kra h vhi aayega pr aage k code run nhi hoga isse shi krne k liye hmme try and except ko use krna padega

age = int(input(" tell your age :"))
try:
    if age<10 or age>18 :
        raise ValueError("your age must be between 10 to 18")
    else:
        print("welcome to club ")
except Exception as err:
    print(f"an error occur which is {err}")   # yhaa pe value error aata hai mtlb if vali conddition aate hai to try use cath kr k except ko bhej k usse run krva dega jise aage k code bhi run hoga

print(" the club will start soon :")
