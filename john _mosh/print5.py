# # # # # # # # # # # # # # price=1000000
# # # # # # # # # # # # # # is_good_credit=False
# # # # # # # # # # # # # # if is_good_credit:
# # # # # # # # # # # # # #  value=price*0.1
# # # # # # # # # # # # # #  #user_input=input("what percentage of 1000000 you want to calculate ? : ")
# # # # # # # # # # # # # #  #value=price*int(user_input)*0.01
# # # # # # # # # # # # # #  print(value)
# # # # # # # # # # # # # # else:
# # # # # # # # # # # # # #  value=price*0.2
# # # # # # # # # # # # # #  #user_input=input("what percentage of 1000000 you want to calculate ? : ")
# # # # # # # # # # # # # #  #value=price*int(user_input)*0.02
# # # # # # # # # # # # # #  print(value)

# # # # # # # # # # # # # # print("down payment is : $" , value) 

# # # # # # # # # # # # # message=input("> ")
# # # # # # # # # # # # # words=message.split(' ')
# # # # # # # # # # # # # emojis={
# # # # # # # # # # # # #     ":)" : "happy",
# # # # # # # # # # # # #     ":(" : "sad"
# # # # # # # # # # # # # }
# # # # # # # # # # # # # output=""
# # # # # # # # # # # # # for word in words:
# # # # # # # # # # # # #     output+=emojis.get(word,word)+" "
# # # # # # # # # # # # # print(output)    

# # # # # # # # # # # # print("hello")

# # # # # # # # # # # name="shailesh"
# # # # # # # # # # # age=20
# # # # # # # # # # # is_new=True

# # # # # # # # # # var=input(" name: ")
# # # # # # # # # # colour=input("colour : ")
# # # # # # # # # # print(var + " likes " + colour)

# # # # # # # # # Birth_date=int(input(" : "))
# # # # # # # # # age=2025-Birth_date
# # # # # # # # # print(age)

# # # # # # # # weight_lbs=input("lbs : ")
# # # # # # # # weight_kgs=int(weight_lbs)*0.45
# # # # # # # # print(weight_kgs)

# # # # # # # course='python is for'
# # # # # # # print(course[0:2])
# # # # # # name="raj"
# # # # # # name1="kajdi"
# # # # # # print(f'{name} [{name1}] is a coder')

# # # # # course='Python is for beginners'
# # # # # print(len(course))
# # # # # print(course.upper())
# # # # # print(course.lower())
# # # # # print(course.title())
# # # # # print(course.find("i"))
# # # # # print(course.replace("is","what"))
# # # # # print("Python" in course)

# # # # weight=int(input('weightt : '))
# # # # unit=input("'L'bs or 'K'g : ")
# # # # if unit.upper()='L':
# # # #   result=weight*0.45
# # # # else:
# # # #   result=unit/0.45
# # # # print(result)
# # # secret_number=9
# # # guess_count=0
# # # guess_limit=3
# # # while guess_count<guess_limit:
# # #     guess=int(input("guess : "))
# # #     guess_count+=1
# # #     if guess==secret_number:
# # #         print("you won")
# # #         break    
    
# # # else:
# # #    print("you loss") 



# # command=""
# # start=False
# # while True:
# #    command=input(">  ").lower()
# #    if command=="start":
# #      if start:
# #        print("car is already started")
# #      else:
# #        start=True
# #        print("car is starting")  

# #    elif command=="stop":
# #       if not start:
# #          print("car is already stopped")
# #       else:
# #         start=False
# #         print("car is stopped ")  


# #    elif command=="help":
# #      print( '''
# #        start-to start the car
# #        stop-to stop the car
# #        quit-to exit
# #      ''')
# #    elif command=="quit":
# #      break
# #    else :
# #     print("i dont understand")

# items=''
# for item  in 'python':
#   items+=item
# print(items)

# for i in range(int('97'),int('122')+1):
#   print(chr(i))

# print(97)
# print(chr(97))
# print(ord('a'))

# for i in range(65,91):
#     print(chr(i))

# for x in range(4):
#     for y in range(4):
#         print(x,y)

# item=''
# for item in range('z'):
#    print(ord('item'))

# numbers=[5,2,5,2,2]
# for i in numbers:
#     result=i*'*'
#     print(result)    
# output=''
# for i in range(5):
#       output+='x'    # output=output+'x'='x'
# print(output)          #output='x'+'x'=xx

# names=['john','mosh','raj']
# output=""
# for name in names:
#     output+=name+" "
# print(output)    
# import if_else
# from if_else import find_max


# def find_max(numbers):

#     maximum=0
#     for number in numbers:
#         if  number>maximum:
#             maximum=number
#     return maximum


# numbers=[6,2,7,4,9]
# maximum=find_max(numbers)
# print(maximum)      

    
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# result="" 
# for row in matrix:
    
  
#     for num in row:
#       result+=str(num)+" "
# print(result)

# numbers=[1,2,3,4,5,6,7]

# numbers.remove(4)
# numbers.pop()
# numbers.append(10)
# print(numbers.index(3))
# print(numbers)

# number1=0
# numbers=[1,2,3,4,4,5,6]
# for number in numbers:
#     if number!=number1:      
#         number1=number
       
#         print(number,end=" ")

# numbers=[1,2,3,4,4,5,6]
# uniques=[]
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# person={
#     "name":"john smith",
#     "age":"27",
#     "is_verified":"True"
# }
# person["name"]="jack"
# print(person["name"])
# print(person.get("birth_date","1 "))
# digits_mapping={
#     "1":"one",
#     "2":"two",
#     "3":"three",
#     "4":"four"
# }
# output=""
# phone_number=input("phone_number : " )
# for ch in phone_number:
#      output+=digits_mapping.get(ch)+" "
# print(output)

# def emoji_converter(messages):
#     words=messages.split(" ")
#     emoji={
#             ":)" : "happy",
#             ":(" : "sad"
#            }
#     output=""
#     for word in words:
#         output+=emoji.get(word,word)+" "
#     return output


# messages=input("> ") 
# result=emoji_converter(messages)   
# print(result)

# def great_user(name):
#     print("hi ")
#     print("i am ")
#     print(name)

# great_user("shailesh")   


# def square(number):
#     result=number*number
  
    

# result=square(3)   
# print(result)

# try:
#     age=int(input("age :"))
#     print(age)
# except ValueError:
#     print("invalid value")

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")


# point=Point(10,20)
# print(point.x)
# print(point.y)
# point.draw()

# class Person:
#     def __init__(self,name):
#         self.name=name
#     def talk(self):
#         print(f"i am {self.name}")

# person=Person("john")
# person.talk()
# import if_else

# from if_else import Animal
# from if_else import dog



# class dog(Animal): 
#     def talk(self):
#         print("bow bow")  

# class cat(Animal):
#     pass


# # animal=Animal()
# # animal.walk()
# dog1=dog()
# dog1.walk()
# import random
# for i in range(3):
#     print(random.randint(10,20))
# import random
# list=['john','raj']
# choice=random.choice(list)
# print(choice)

import random
class Dice:
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first,second
    
dice=Dice()
print(dice.roll())    












