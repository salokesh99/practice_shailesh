#1------Write a program to create a tuple with different data types and print it.
# a=("str",1)
# print(type(a))




#2-----Write a program to access the first and last elements of a tuple.
# a=("shailesh","ajja","kcnhduj")
# print(a[0],a[-1])



#3-----Write a program to find the length of a tuple without using len().
# a=(1,2,3,4)
# count=0
# for i in a:
#     count+=1
# print(count)    




#4-----Write a program to check whether a given element exists in a tuple.
# a=(1,2,3,4)
# b=1
# if b in a:
#     print("it exists")
# else:
#     print("not exist")    




#5-----Write a program to convert a tuple into a list and modify it.
# a=(1,2,3,4)
# b=list(a)
# b.append(6)
# print(b)
# a=tuple(b)
# print(a)




#6-----Write a program to create a set of 5 numbers and print it.
# a={1,2,3,4,5}
# print(a)




#7-----Write a program to add and remove elements from a set.
# a={1,2,3,4,5}
# a.add(9)
# print(a)
# a.remove(3)
# print(a)





#8----Write a program to find the union and intersection of two sets.
# a={1,2,3,4}
# b={7,8,9,2}
# c=a.intersection(b)
# print(c)



#9-----Write a program to check whether one set is a subset of another set.
# a={1,2,5,6}
# b={1,2,5,6,7,8}
# is_subset=True
# for i in a:
#     if i not in b:
#         is_subset=False
#         break
# if is_subset:
#     print("subset") 
# else:
#     print("not subset")       




#10-----Write a program to remove duplicates from a list using a set.
# a=[1,2,3,4,3]
# b=set(a)
# print(b)
# a=list(b)
# print(a)

#another way:
# c=list(set(a))
# print(c)
       
    