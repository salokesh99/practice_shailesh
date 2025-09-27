# course="python is for the beginners"
# print(course[0])
# print(course[1:-4])
# print(course[:-1])
# print(course[:])
# name='shailesh'
# last='ajja'
# print(name  +  ' [ ' + last + ' ] is a coder')
# print(f'{name } [  { last } ] is a coder ')

# name=input("enter name : ")
# print(name)

# name="shailesh"
# # print(len(name))
# count=0
# for ch in name:
#     count+=1
# print(count)


# name="shailesh"
# b=""

# for ch in name:
#     a=ord(ch)-32
#     b+=chr(a)
# print(b)    


# name="SHAILESH AJJA"
# b=""

# for ch in name:
#   if ch!=" ":  
#     a=ord(ch)+32
#     b+=chr(a)
#   else:
#     b+=" "  
# print(b)


# name="shailesh ajja"
# vowels="aeiouAEIOU"

# count=0
# for ch in name:
#     if ch in vowels:    
#         # print(ch)

#         count+=1
# print(count)    
    


name="shailesh"
reversed=""
for ch in name:
    reversed=ch+reversed
print(reversed)    
