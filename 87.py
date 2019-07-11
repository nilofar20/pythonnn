n3,p4=map(int,input().split())
d=1
while(d<=n3 and d<=p4):
 if(n3%d==0 and p4%d==0):
  gcd1=d
 d=d+1
print(gcd1)
