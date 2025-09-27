# # # # #has_high_income=True
# # # # #has_good_credit=False

# # # # #if has_high_income and not has_good_credit:
# # # #  #   print("he is eligible for loan")

# # # # temp=int(input("how much temperature is there now ? :"))
# # # # if temp>30:
# # # #     print("it's a hot day")

# # # # elif temp<10:
# # # #     print("it's a cool day")
# # # # else:
# # # #     print("it's neither cold nor hot")


# # # weight=int(input("weight : "))
# # # unit=input('"L"bs or "K"g :' )
# # # if unit.upper()=="L":
# # #     converted=weight*0.45
# # #     print(f"you are {converted} kg")
# # # else:
# # #     converted=weight/0.45
# # #     print(f"you are {converted} pounds")

# # i=0
# # while i<=5:
# #  a=2
# #  print(a ** i)
# #  i+=1


# secret_number=9
# guess_count=0
# guess_limit=3
# while guess_count<guess_limit:
#     guess=int(input("guess : "))
#     guess_count+=1
#     if guess==secret_number:
#         print("you won")
#         break
# else:
#     print("you loss")

# command=""
# while command!="quite":
#     command=input("> ").lower()
#     if command=="start":
#         print("car is srart")
#     elif command=="stop":
#         print("car is stopped")
#     elif command=="help":
#         print("""
#           start -to start the car
#            stop-to stop the car
#            quit- to quit
#          """)
        
        
#     else:
#         print("sorry i dont understand")  
#         break
    



#------------------------------------------------------

# a=["apple","banana","mango"]
# b=[x for x in a if "a" in x]
# print(b)

# b=[x for x in a if x!="apple"]
# print(b)

# b=[x for x in a]
# print(b)

# b=[x.upper() for x in a ]
# print(b)


# a={"shailesh","ajja"}
# a.discard("apple")
# a.pop()
# print(a)



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# x=thisdict.get("model")
x=thisdict.keys()
print(x)