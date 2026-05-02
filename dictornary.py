# #dictionary
# dict = {
#     "key" : "values",
#     "name" : "athrav",
#     "subject" : ["physics","maths","chemistry"],
#     "topics" : ("dictionary","touple"),
#     "is adult" : True,
# }      
# print(dict)    #DICTIONARY maily two chij ki bnai hoti hai ek keys and values jisme keys immutable chije hold krte hai aue values mutable and immutable dono chije hold krte hai 

# #nested dictionary

# student = {
#     "name" : "athrav khandelwal",      
#     "subbject": {            #as we know dictionary start using {} these arrow 1st dictionary we made is student inside student dictionary we made another dictionary of name subject this is called nested dictionary
#         "physics": 90,
#         "chemistry" : 89,
#     }
# }

# print(student["subbject"]["physics"])


#dictionary method

student = {
    "name" : "athrav khandelwal",      
    "subbject": {           
        "physics": 90,
        "chemistry" : 89,
    }
}

# print(student.keys())   #return all the keys 
# print(list(student.keys()))  #written in list format
# print(len(list(student.keys())))  #numbers of key
# print(student.values())  #return all the values
# print(student.items())   #written all (key ,values) pair in tuple format 

# print(student["name"])
# print(student.get("name"))  #both code at 40 and 41 line gave the value of the key but the DIFFERENCE IS  code at line 40 gave error when  we gave any key which is not present in dictionary while code at 41 print none instead of gaving error. example given below:
# print(student["name2"])
# print(student.get("name2"))   #this dictionary.get() is used because if error is occur then futher writtwn code do not execute

new_dict = {"name1": "tanisha","age":"18"}
student.update(new_dict) #this is use to update dictionary 
print(student) 