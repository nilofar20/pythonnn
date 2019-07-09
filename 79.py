nn1,pn2=map(int,input().split())
p3=nn1*pn2
for i in range(0,p3+1):
 if(i**2==0):
  print("yes")
  break
else:
  print("no")
