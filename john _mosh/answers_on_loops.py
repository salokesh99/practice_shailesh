#1---Write a program to print the numbers from 1 to 10 using a loop.

# for i in range(1,10+1):
#     print(i)





#2---Write a program to find the sum of two numbers entered by the user.

# first=int(input("first number : "))
# second=int(input("second number : "))
# sum=first+second
# print(sum )



#3---Write a program to swap two numbers using a third variable.
# a=5
# b=12
# temp=a
# a=b
# b=temp
# print(a)
# print(b)




#4-----Write a program to swap two numbers without using a third variable or temporary variable.
# a=5
# b=12
# a,b=b,a
# print(a)
# print(b)





#5----Write a program to check whether a number is even or odd.

# number=int(input("enter number : "))
# if number%2==0:
#     print("it is a even number")
# else:
#     print("it is a odd number")





#6----Write a program to find the largest of two numbers.

# a=15
# b=10
# if a>b:
#     print(a," is largest ")
# else :
#     print(b,"is largest")





# 7----Write a program to find the largest of three numbers.

# a=15
# b=8
# c=1   
# if a>b and a>c:
#     print(a," is largest in these numbers")
# elif b>a and b>c:
#     print(b," is largest in these numbers")
# elif c>a and c>b:
#     print(c,"is largest in these numbers")
# else:
#     pass
# if a==b and b==a and c==b and c==a:
#     print("all are equals")




#8-----Write a program to print the multiplication table of a number entered by the user.

# number=int(input("enter a number :"))
# i=1
# while i<=10:
#     mult=number*i
#     print(f"{mult} = {number} * {i}")
#     i+=1




#9-----Write a program to calculate the factorial of a number using a loop.
number=6

fact=1
for i in range(1,number+1) :
    fact*=i
    
print(fact)  










