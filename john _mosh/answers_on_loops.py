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
# number=6
# i=1
# fact=1
# while i<=number:
#     fact*=i
#     i+=1
# print(fact)  





#10-----Write a program to print all even numbers between 1 and 50.
# i=1
# while i<=50:
#     if i%2==0:
#         print(i)
        
#     i+=1  




#11----Write a program to reverse a given number (e.g., 123 → 321).
# number=123
# temp=0
# while number>0:
#     temp=temp*10+number%10
#     number=number//10
# rev=temp
# print(rev)



#12----Write a program to check whether a number is a palindrome (e.g., 121 → palindrome).
# number=int(input("enter number : "))
# original_number=number
# temp=0
# while number>0:
#     temp=temp*10+number%10
#     number=number//10
# rev=temp
# if rev==original_number:
#     print("it is a palondrome")
# else:
#     print("it is not a palindrome")    




#13----Write a program to find the sum of digits of a number (e.g., 123 → 6).
# number=125
# temp1=0
# while number>0:
#     temp=number%10
#     temp1=temp1+temp
#     number=number//10
# print(temp1)    





#14-----Write a program to print the Fibonacci series up to 10 terms.
#(sum of previous number)
# number=10
# a=1
# b=0
# i=0
# temp=0
# while i<number:
#     print(b)
#     temp=a
#     a=a+b
#     b=temp
#     i+=1




#15----Write a program to check whether a number is positive or negative.
# a=10
# if type(a)==int:   #to check number is int type or not
#     if a>0:
#         print("positive")
#     elif a<0:
#         print("negative")
#     else:
#         print("zero")



#16-----write a program to find the largest of three numbers using nested if.
# a=10
# b=5
# c=8
# if a>=b:
#     if a>=c:
#         print("a is largest")
#     else:
#         print("c is laegest")
# else:
#     if b>=a:
#         print("b is largest")
#     else:
#         primt("c is largest")




#17-----Write a program to check whether a given number is divisible by 5 and 11 or not.
# a=10
# if a%5==0 and a%11==0:
#     print("number is divisible by both")
# else:
#     print("it is not divisble by both")



#18-----Write a program to check whether a year is a leap year or not.
# number=int(input("enter numebr :"))
# if number%4==0:
#     print("it is a leap year")
# else:
#     print("not a leap year")




# 19-----Write a program to accept a character from the user and check whether it is a vowel or consonant.
# ch=input("enter character")
# if ch.lower() in ('a','e','i','o','u'):
#     print("it is a vowel")
# else:
#     print("it is consonent")



#20-----Write a program to check whether a person is eligible to vote (age ≥ 18).
# age=25
# if age>=18:
#     print("person is eligible")
# else:
#     print("not eligible")




#21-----Write a program to accept marks from a student and print their grade:
# 90–100 → A
# 75–89 → B
# 50–74 → C
# Below 50 → Fail.

# marks=int(input("marks : "))
# if 90<=marks <=100:
#     print("grade=A")
# elif 75 <=marks<=89:
#     print("grade=B")
# elif 50<=marks <=74:
#     print("grade=C")
# elif marks<50:
#     print("fail")
# else:
#     print("invalid")




#22----Write a program to check whether a given number is a single-digit, double-digit, or more than two digits.
# number=1234
# if -9<=number<=9:
#     print("it is single digit")
# elif -99<=number<=99:
#     print("it is double digit")
# else:
#     print("more than double digit")




#23----Write a program to accept three angles of a triangle and check whether the triangle is valid or not (sum = 180°).
# a=int(input("first angle: "))
# b=int(input("second angle : "))
# c=int(input("third angle : "))   

# if a>0 and b>0 and c>0 and (a+b+c)==180:
#     print("triangle is valid")
# else:
#     print("triangle is invalid")   



#24----Write a program to check whether a character entered by the user is an uppercase letter, lowercase letter, digit, or special symbol.
# ch=input("enter a character : ")
# if len(ch) !=1:
#     print("enter a only one cha")
# elif 'A'<=ch<='Z':
#     print("it is uppercase")
# elif 'a'<=ch<='z':
#     print("lowercase")
# elif '0'<=ch<='9':
#     print("digit")
# else:
#     print("special symbol")




#25----Write a program to accept the age of a person and classify them as:

# Child (0–12)

# Teenager (13–19)

# Adult (20–59)

# Senior Citizen (60 and above).

# age=int(input("age of person : "))
# if 0<=age<=12:
#     print("child")
# elif 13<=age<=19:
#     print("teenage")
# elif 20<=age<=59:
#     print("adult")
# else:
#     print("senior")



def call_thisfunction(n):
    print("this function is called")
    if n==1:
      print("entered if","value of n is",n)
      
      return 1
    else:
       print("entered else"," value of n is ",n)
       return "not 1"

x=call_thisfunction(5)
print("value of x",x)

  










