#1------ Write a program to create a dictionary with 3 key-value pairs and print it.
# a={
#     "name":"shailesh",
#     "father":"ayyappa",
#     "surname":"ajja"
# }

# ------
# print(a)
# for x in a:
#     print(x,":",a[x])



#2----- Write a program to access a value from the dictionary using its key.
# a={
#     "name":"shailesh",
#     "father":"ayyappa",
#     "mother":"shilpa"
# }
# b=a["name"]
# print(b)




#3----Write a program to add a new key-value pair to an existing dictionary.
# a={
#     "name":"shailesh",
#     "father":"ayyappa",
#     "surname":"ajja"
# }

# a["brother"]="sangappa"
# print(a)



#4---- Write a program to update the value of an existing key in a dictionary.
# a={
#     "name":"shailesh",
#     "father":"ayyappa",
#     "surname":"ajja"
# }
# a["name"]="raj"
# print(a)





#5----- Write a program to delete a key-value pair from a dictionary.
# a={
#     "name":"shailesh",
#     "father":"ayyappa",
#     "surname":"ajja"
# }
# a.pop("name")
# del a["name"]
# print(a)



#6---- Write a program to check if a given key exists in a dictionary.
# a={
#     "name":"shailesh",
#     "father":"ayyappa",

# }
# key="name"
# if key in a:
#         print("it exists")