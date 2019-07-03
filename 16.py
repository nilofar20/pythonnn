z,y=map(int,input().split())
for n in range(z,y):
 if n>1:
  for i in range(2,n):
   if(n%i)==0:
    break
  else:
   print(n,end=" ")
