p,n=map(int,input().split())
for j in range(p+1,n):
  ch=j
  fnd=0
  while (j>0):
    r=j%10
    fnd=fnd+(r**3)
    j=j//10
    if(fnd==ch):
      print(fnd,end=" ")
