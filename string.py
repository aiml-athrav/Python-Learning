# #concationation of string
# str1 = "athrav"
# str2 = "khandelwal"
# final_str = str1 + str2 #add both string without spacing
# print(final_str)

# final_str_gap = str1 + " " + str2 #add both string with gap to take gap we have to add one gap with collon between strings
# print(final_str_gap)


# #length of string
# str1 = "athrav"
# len1 = len(str1)
# str2 = "khandelwal"
# len2 = len(str2)
# print(len1)
# print(len2)
# final_len = len(str1 + str2)
# print(final_len)

# #extra
# str = "my self athrav khandelwal my age is 18"
# #if we print str whole statment are written in same line (linear line)
# #if we need that it cover two line then we use \n after the word we have to break line
# #if we need a 1 tab space we use \t betwwn the words where we need space 
# str_1 = "my self athrav khandelwal \nmy age is 18"
# str_2 = "my self athrav khandelwal \tmy age is 18"
# print(str)
# print(str_1)
# print(str_2)

# #string indexing
# str = "athrav khandelwal"
# char = str[0]
# print(char)

# #slicing
# # str[starting_idx : ending_idx]  in this ending index not include

# str = "athrav khandelwal"
# print(str[0:5]) #here str[0]is (a) and its is starting str so it is include , str[5]is (v) and it is end string so it is not include it also print space 
# print(str[0:8]) #here space also arrived
# print(str[2:]) #if we donot write any index after : this means till end of the string

# #string function
# str = "athrav khandelwal"
# print(str.endswith("wal")) #it check whether the string end with given sub string or not and print true and false
# print(str.capitalize()) # it make first letter of string capital , it do not changes in string it make new string by it self which were shown as output 
# print(str.capitalize())
# print(str) #str.capital one change where it is use if we want to change permenantly then 
# str = str.capitalize()
# print(str)
# print(str.replace("a","t")) # str.replace("old","new") it is use to replace words in string or replace whole string
# print(str.replace("Athrav","tanisha"))
# print(str.find("v")) #write index value of the word where it is lies first time in 
# print(str.find("x")) #shoew -1 because x not come in string 
# print(str.count("a")) # find the number of time it occur in string



