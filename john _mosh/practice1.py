# print("hello world")
# name=input("name : ")
# print(f" {name} a personalized meeting")
# a=10
# b=5
# a=a+b
# b=a-b
# a=b-a
# print(a,b)
# a="10"
# print(type(a))
# length=int(input("length of rect angle : "))
# width=int(input("width of rectangle : "))
# area=2*length*width
# print("area of rect angle : " ,area)
# a=int(input("number : "))
# if a%2==0:
#     print("it is even number")
# else:
#     print("it is odd number")
# a=10
# b=6
# c=10
# if a>=b and a>=c:
#     print(a)
# elif b>=a and b>=c:
#     print(b)
# else:
#     print(c)

#8.Create a calculator that takes two numbers and an operator (\(+\), $-\(,\)*\(,\)/$) as input and prints the result.
# a=10
# b=5
# operator=input("operator= : ")

# if operator=="Addition":
#     Addition=a+b
#     print(Addition)

# elif operator=="Substraction":
#     Substraction=a-b
#     print(Substraction)

# elif operator=="Multiply":
#     Multiply=a*b
#     print(Multiply)

# elif operator=="Division":
#     Division=a/b
#     print(Division)

# else:
#     print("invalid input")

#9. Write a program that checks if a given year is a leap year.

# year=int(input("enter a year : "))
# if year%4==0:
#     print("it is  a leap year")
# else:
#     print("it ia not a leap year")

# 10.Write a program that checks if a given string is a palindrome

# number=int(input("enter the number : "))
# original=number
# rev=0
# while number>0:
#     digit=number%10
#     rev=rev*10+digit
#     number=number//10
# print(rev)

# if rev==original:
#     print(" it is a palindrome")
# else:
#     print(" it is not a palindrome")

# 11.Write a program that prints the numbers from 1 to 10 using a for loop.
# for number in range(0,10):
#     print(number)

# 12.Write a program that prints the numbers from 10 down to 1 using a while loop
# number=10
# while number>=1:   
#     print(number)
#     number=number-1

# 13.Create a program that prints the multiplication table for a given number
# number=8
# for digit in range(1,10+1):
#     result=number*digit
#     print(result,(f"={number}*{digit}"))

# 14.Write a program to calculate the factorial of a number.
number=4
# while number>=1:
   
#     # result=(number-1)    #4*3*2
#     #   result=result  *(number-1)                        
    
#     # print(result)
#     # number=number-1
#     number
#     number-1
#     original=number+new
# value=int(input("enter the number : "))
# for number in range(1,value):
#     res=number*value
#     value=res
# print(res)    

# num=int(input("enter the number : "))
# i=1
# fact=1
# while i<=num:
#     fact*=i
#     i+=1
# print(fact)

# 15.Write a program to generate the Fibonacci series up to a given number of terms
# num=int(input("number : "))  
# a=0
# b=1
# while a<=num:
#     print(a)
#     temp=a
#     a=b
#     b=temp+a

# 21.Write a program to find the largest element in a list.

# numbers=[10,4,6,7,17,9]
# largest=0
# for number in numbers:
#     if largest<number:
#         largest=number
#     else:
#         largest=largest
# print(largest)

#22.Write a program to find the sum of all elements in a list.
# numbers=[1,3,2,5,7,9]
# sum=0
# for number in numbers:
#     sum=sum+number
# print(sum)    

#23.Write a program to find the second largest number in a list.(write for array)
# numbers=[2,5,8,4,9,7,12]
# first=0
# second=0
# for num in numbers:
#     if num>first:
#         second=first
#         first=num
#     elif num>second and second!=first:
#         second=num
# print(second)

# 24.Write a program to remove duplicates from a list
# numbers=[1,2,3,3,4,5]
# unique=[]
# for num in numbers:
#     if num not in unique:
#      unique.append(num)
# print(unique) 

#25.Create a program that combines two lists, taking odd numbers from the first and even numbers from the second.
# first=[1,2,3,4,5,6,7]
# second=[1,2,3,4,5,6]
# unique=[]
# for num in first:
#     if num%2!=0:
#         unique.append(num)
# for num in second:
#     if num%2==0:
#         unique.append(num)

# print(unique)
# unique.sort()
# print(unique)

#26.Create a program that checks if the first and last numbers of a list are the same
# numbers=[1,2,3,4,1,6]
# #numbers[:-1]
# for num in numbers:
#     if num==numbers[-1]:
#         print("same")
#         break
#     else:
#         print("not same")
#         break

#27.Given a list, create a new list that contains only the even numbers from the original list.
# original=[1,2,3,4,5,6,7]
# new=[]
# for num in original:
#     if num%2==0:
#         new.append(num)
# print(new)

#28.Write a function that takes a list of numbers and returns a new list with distinct elements
# numbers=[1,3,5,5,7,8]
# new=[]
# for num in numbers:
#   if num not in new:
#     new.append(num)
# print(new)

#29.Write a program to check if a list is sorted in ascending or descending order.
# numbers=[6,5,4,3,2]
# if len(numbers)<=1:
#     print("it is already sorted")
# is_asc=True
# is_desc=True

# for i in range(len(numbers)-1):
#     if numbers[i]<numbers[i+1]:
#        is_desc=False
#     if numbers[i]>numbers[i+1]:
      
#         is_asc=False


# if not is_asc and not is_desc:
   
#     print("it is not sorted")


# if is_asc:
#     print("it is in acending order")
# if is_desc:
#     print("it is in descinding order")
# if is_asc and is_desc:
#     print("all are equal")    

#30.Write a program to reverse a list in place. 
numbers=[1,2,3,4,5]
new=[]
# numbers.reverse()
# print(numbers)
n=len(numbers)
a=1
for i in range(n):
    
    b=numbers[-a]
    a+=1
    new.append(b)

print(new)







    








