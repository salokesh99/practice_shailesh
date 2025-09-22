#1-----Write a program to create a list of 5 numbers and print it.
# a=[1,2,3,4,5]
# print("list=",a)




#2-----Write a program to find the length of a list without using len().
# a=[1,2,3,4]
# count=0
# for x in a:
#     count+=1
# print("length of list =",count)    



#3-----Write a program to access the first and last elements of a list.
# a=[1,2,3,4,5]
# print(a[0])
# print(a[-1])



#4----Write a program to find the sum of all elements in a list.
# a=[1,2,3,4]
# sum=0
# for x in a:
#     sum=sum+x
# print(sum)




#5----Write a program to find the largest and smallest element in a list.
# a=[1,2,3,4]
# largest=a[0]
# smallest=a[0]
# for x in a:
#     if x>largest:
#         largest=x
#     if x<smallest:
#         smallest=x    
# print(largest)    
# print(smallest)



#6----Write a program to count how many times a specific element appears in a list.
# a=[1,2,3,3,4,5]
# b=[]

# for i in a:
#     if i not in b:
#        print(i,"appears",a.count(i),"times")
#        b.append(i)
  
# a=["shjhd","wdjnhw"]
# for i in a:
#    print(a.count(i))



#7----Write a program to reverse a list without using reverse().
# a=[1,2,3,4]
# print(a[::-1])

# a=[1,2]
# b=[3]
# c=a+b
# print(c)

# a=[1,2,3,4]
# b=[]
# for i in a:
#     b=[i]+b
# print(b)

   


#8-----Write a program to remove duplicates from a list.
# a=[1,2,3,4,3]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)




#9-----Write a program to sort a list in ascending order without using sort().
# a=[4,3,5,2,6]

# for i in range(len(a)-1):
#    for j in range(0,len(a)-i-1): 
#     if a[j]>a[j+1]:
#        a[j],a[j+1]=a[j+1],a[j]
# print(a)




#10-----Write a program to merge two lists into a single list.
# a=[1,2,3,4]
# b=[6,7,8,9]
# a.extend(b)
# print(a)

# another
# c=a+b
# print(c)




#11-----Write a program to print all even numbers from a list.
# a=[1,2,3,4,5]

# for i in a:
#     if i%2==0:
#          print(i)
    



#12-----Write a program to find the second largest element in a list.
# a=[2,1,5,3,8]
# largest1=a[0]
# largest2=a[1]
# for i in range(len(a)-1):
#     if a[i]>largest1:
#        a[i]>largest2
#        largest1=a[i]
#        largest2=largest1 
# print(largest2)       




#13-----Write a program to insert an element at a specific position in a list.
# a=[1,2,3,4,5]
# a.insert(3,5)
# print(a)





#14-----Write a program to delete an element from a specific position in a list.
# a=[1,2,3,4,5]
# del a[2]
# print(a)




#15------Write a program to check whether an element exists in a list or not.
# a=[1,2,3,4,5]
# if  2 in a:
#     print("it exists")
# else :
#     print("not exist")





        
      
        




