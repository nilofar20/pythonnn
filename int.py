z,x=map(int,input().split())
for j in range(z+1,x):
  ch=j
  fnd=0
  while (j>0):
    r=j%10
    fnd=fnd+(r**3)
    j=j//10
    if(fnd==ch):
      print(fnd,end=" ")
