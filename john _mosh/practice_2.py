# print('hello')
#31.Write a program to merge two dictionaries.
# list1={
#     "name":"shailesh",
#     "colour":"white"

# }
# list2={
#     "name":"raj",
#     "colour":"black"
# }
# list1.update(list2)
# print(list1)

#32.Write a program that counts the frequency of each element in a list and stores it in a dictionary.
# list=[1,2,3,2,4,1,3,1]
# frequency={}
# for item in list:
#     if item in frequency:
#         frequency[item]+=1  
#     else:
#         frequency[item]=1
# print("frequencies=",frequency)   

#33.Write a program to iterate over a dictionary and print its keys and values.
# list={
#     "name":"shailesh",
#     "age":26,
#     "email":"shaileshajja@gmail.com"
# }
# for key,value in list.items():
#     print(key,":",value)

#34.Write a program to sort a dictionary by its values.
# dict1={
#     "name":"shailesh",
#     "age":"26",
#     "email":"shailesh@gmail.com"
# }

# list1=dict1.values()
# sorted1=sorted(list1)
# print(sorted1)
                                              #list1=sorted(dict1.items())
                                              #print(list1)


#35.Create a program that demonstrates the key differences between a list and a set.
#36.Write a function that accepts variable-length arguments (*args) and prints them.
# def talk(name):
#     print(name + " is talkinhg")

# talk("shailesh")

#37.Write a function that accepts keyword variable-length arguments (**kwargs) and prints them.
# def person(**kwargs):
#   for key,value in kwargs.items():
#     print(key,":",value)


# person(name="shailesh",age="26",city="bider")

# def person(**kwargs):
#     for key , val in kwargs.items():
#         print(key, val )

# person(name="shailesh",age="26",city="bider", dob='2025')
        


# def person(*args):
#     for i in args:
#         print(i )

# lst = [1,23,34,54,6,7,7,4,5]

# person(lst)

#38.Write a lambda function that squares a given number.
# def square1(n):
#     return lambda a:a*n

# square2=square1(2)
# print(square2(2))

#35.Write a function that can filter a list to get only the odd numbers, using the filter() function.
# def filter(list):                  

#     for number in list:
#         if number%2!=0:
#            list1.append(number)
              
# list=[1,2,3,4,5,6]
# list1=[]
# filter(list)
# print(list1)

#correct solution
#def get_odds(numbers):
   # print(type(numbers))
    # return list(filter(lambda x: x % 2 != 0, numbers))

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# odd_numbers = get_odds(nums)
# print('odd_numbers',odd_numbers)


#another solution
#def get_odds(numbers):
   # print(type(numbers))
#     list1=[]
#     for num in numbers:
#         if num%2!=0:
#             list1.append(num)
#     return list1


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# odd_numbers = get_odds(nums)
# print('odd_numbers',odd_numbers)

# muns = [1,5,4,8,8]

# odd_numbers = get_odds(muns)
# print('odd_numbers',odd_numbers)

# print("Original list:", nums)
# print("Odd numbers:", odd_numbers)

#36.Write a program that reads a text file and prints its content to the console.

# path = "/home/loki/raj/a.txt"
#f=open(path,"a")
#print(f.read())
#f.write("\n  \n it is for bigginers")
#f.close()
# f=open(path)
# print(f.readlines())
# f.close()

# f=open("/home/loki/raj/a.txt")
# for i in range(5):
#         line=f.readline()
        
#         if not line:
#           break
#         print(line.strip())
# print(f.readline())

# print(f.readline())



