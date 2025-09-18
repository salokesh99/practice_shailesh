A=['1','2','3','A','B','C','D']
B=[]
c=[]
D=[]
for i in A:
  if i.isnumeric():
   B.append(i)
  elif i.isalpha():
    c.append(i)
  else:
    print(D)
print(B)


print(c)

