n,p=map(int,input().split())
ls=list(map(int,input().split()))
l=[]
for i in range(0,p):
     u2,v2=map(int,input().split())
     l.append([u2,v2])
for i in range(p):
     lower=l[i][0]
     upper=l[i][1]
     s=sum(ls[lower-1:upper])
     print(s)
