tup = (1,2,3,4,3)
print(type(tup))
print(tup[2])
#tup[1] = 3 it is not valid in tuples and strings it is only valid in list
print(tup[1:4])
tup_1 = () #it is also valid it is empty tuple
print(tup_1)
tup_2 = (1,) #if we writte single element tuple it end with comma
print(type(tup_2))
tup_3 = (1) #if we donot use comma at the end it is act like integer
print(type(tup_3))

tup = (1,2,3,4,3)
tup = tup.index(3) #tup.index(element) it is used to find the index number of the number occuring first in tuple
print(tup)

tup = (1,2,3,4,3)
tup = tup.count(3)# it is used to count the element in the tuple. tup.count(element)
print(tup)