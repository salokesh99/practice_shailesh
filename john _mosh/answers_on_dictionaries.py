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




#7----- Write a program to print all keys in a dictionary.
# a={
#     "name":"shailesh",
#     "father":"ayyappa"
# }
# for key in a:
#     print(key)



#8---- Write a program to print all values in a dictionary.
# a={
#     "name":"shailesh",
#     "father":"ayyappa"
# }
# for value in a:
#     print(a[value])




#9----- Write a program to print all key-value pairs in a dictionary.
# a={
#     "name":"shailesh",
#     "father":"ayyappa"
# }
# for x in a:
#     print(x,":",a[x])




#10----- Write a program to find the length of a dictionary without using len().
# a={
#     "name":"shailesh",
#     "father":"ayyappa",
#     "mother":"shilpa"
# }
# count=0
# for x in a:
    
#     count+=1
# print(count)

# ----
# print(len(a))





#11----- Write a program to create a dictionary of 5 students with their marks and print it.
# students={
#     "veeresh":60,
#     "ajay":58,
#     "vijay":50,
#     "vishwa":55
# }
# for name in students:
#     print(name,"marks is ",students[name])




#12----- Write a program to find the student with the highest marks from a dictionary.
# students={
#     "veeresh":60,
#     "ajay":58,
#     "vijay":50,
#     "vishwa":55
# }
# highest_marks=0
# highest_student=0
# for name in students:
#     marks=students[name]
#     if marks>highest_marks:
#         highest_marks=marks
#         highest_student=name
# print(highest_student,"has highest marks is ",highest_marks)  
      




#13----- Write a program to sum all values in a dictionary.
# numbers={
#     "a":10,
#     "b":20,
#     "c":30,
#     "d":40
# }
# sum=0
# for i in numbers:
#     sum=sum+numbers[i]
# print("sum of values :  ",sum)





#14---- Write a program to multiply all values in a dictionary.
# numbers={
#     "a":10,
#     "b":20,
#     "c":30,
#     "d":40
# }
# multi=1
# for i in numbers.values():
#     multi=multi*i
# print(multi)    



#15---- Write a program to merge two dictionaries into one.
# a={
#     "name":"shailesh"
# }
# b={
#     "father":"ayyappa",
#     "mother":"shilpa"
# }
# family={}
# for key in a:
#     family[key]=a[key]
# for key in b:
#     family[key]=b[key]

# print(family)






#16---- Write a program to create a nested dictionary (dictionary inside dictionary) and print it.
# students={
#     "student_1":{
#         "name":"veeresh"
#     },
#     "student_2":{
#         "name":"ajay"
#     },
#     "student_3":{
#         "name":"vijay"
#     },
#     "student_4":{
#         "name":"vishwa"
#     }

# }
# print(students)























# Write a program to count how many times each character appears in a string using a dictionary.
# students={
#     "name":"shailesh",
#     "father":"ayyappa" 
# }
# text=students["name"]+students["father"]
# freq={}
# for ch in text:
#      if ch in freq:
#           freq[ch]+=1
#      else:
#           freq[ch]=1
 
# for x in freq:
#      print(x,":",freq[x])             









