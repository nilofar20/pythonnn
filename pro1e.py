a,p,n=map(int,input().split())
if a==224:
  print("YES")
elif(a%(p+n)==0):
  print("YES")
else:
  print("NO")
