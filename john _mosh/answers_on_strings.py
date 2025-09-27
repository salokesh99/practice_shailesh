#1-----Write a program to accept a string from the user and print it.
# name=input("enter name : ")
# print(name)



#2-----Write a program to find the length of a string without using len().
# name="shailesh"
# count=0
# for ch in (name):
#     count+=1
# print(count)



#3-----Write a program to convert a string to uppercase.
# name="shailesh ajja"
# print(name.upper())



#4-----Write a program to convert a string to lowercase.
# name="SHAILesh ajJA"
# print(name.lower())



#5----Write a program to count how many vowels are in a string.
# name="shailesh ajja"
# vowels="aeiouAEIOU"
# count=0
# for ch in (name):
#    if ch in vowels:
#       count+=1
# print(count)




#6-----Write a program to reverse a string.
# name="shailesh"
# reverse="" 
# for char in name:
#     reverse=char+reverse         # without loop use this reverse=name[::-1]
# print(reverse)




#7-----Write a program to check whether a string is a palindrome (same forward and backward).
# name="rar"
# reverse=name[::-1]
# if name==reverse:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")





#8-----Write a program to count the number of words in a string.
# s=input(" enter words : ")
# count=1

# while s[0]==" ":
#     s=s[1:]
# print(s)
# while s[-1]==" ":
    
#     s=s[:-2]
# print(s)
# for word in s:
#     if word==" ":
#         count+=1
# print(count)




# another solution
# a="    shailesh ajja "
# count=1
# a=a.strip(" ")
# #print(a.split())
# for word in a:
    
#     if word==" ":
#         count+=1
# print(count)




#9------Write a program to replace all spaces in a string with hyphens (-).
# a="   raj   "
# print(a.replace(" ","_"))



#10-----Write a program to check whether a given substring is present in the string or not.
# a="shailesh"
# b="ai"
# if b in a:
#     print("is present")
# else:
#     print("not present")



#11-----Write a program to remove all vowels from a string.
# a="shailesh"
# b="aeiouAEIOU"
# res=""
# for char in a:
#     if char  not in b:
#         res=res+char
# print(res)




#12----Write a program to find the first and last character of a string.
# a="shailesh"
# print(a[0],a[-1])



#13----Write a program to count the frequency of each character in a string.
# a="shailesh"
# b={}

# for ch in a:
#     if ch not in b:
#         b[ch]=1
#         print(b[ch])
        
#     else:
#         b[ch]+=1
    
# for ch in b:
#     print(b[ch])    



#---------another solution

# a="shailesh"
# b=""
# for ch in a:
#     if ch not in b:
#       print(a.count(ch))
#       b+=ch





#14-----Write a program to check whether two strings are equal or not.
# a="shailesh"
# b="ajja"
# c=len(a)
# d=len(b)
# if c==d:
#     print("both are equal")
# else :
#     print("both are not equals")




#15----Write a program to accept a string and print only the digits present in it.
# a=input("enter : ")

# for ch in a:
#     if '-9'<=ch<='9':

#         print(ch)





#16------Write a program to accept a string and print it in title case (first letter of each word capital).
# a=input("enter : ")
# print(a.title())



#17-----Write a program to check whether a string starts with a vowel or not.
# a="shailesh"
# vowel="aeiouAEIOU"
# if a[0]  in vowel:
#     print("it is vowel")
# else:
#     print("it is not vowel") 




#18----Write a program to find the largest word in a string.
# a="shailesh ajja wjsndh"
# b=a.split()
# largest=b[0]

# for word in b:
#    if len(word)>len(largest):
#       largest=word
# print(largest)




#19----Write a program to remove all special characters from a string (keep only letters and digits).
# a="shailesh ajja12 @a$"
# b=""

# for ch in a:
#     if '-9'<=ch<='9':
#         b=b+ch
#     elif 'a'<=ch<='z':
#         b=b+ch
#     elif 'A'<=ch<='Z':
#         b=b+ch
#     elif ch==" ":
#         b=b+" "
#     else:
#         pass
# print(b)    




#20-----Write a program to count how many uppercase and lowercase letters are in a string.

# a=input("enter string : ")
# uppercase_count=0
# lowercase_count=0
# for ch in a:
    
#     if 'a'<=ch<='z':
        
#         uppercase_count+=1

#     elif 'A'<=ch<='Z':
        
#         lowercase_count+=1
# print(lowercase_count)
# print(uppercase_count)


      
            





        

