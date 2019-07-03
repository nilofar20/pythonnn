num=int(input())
p=list(map(int,input().split()[:num]))
p.sort()
for v in p:
  print(v,end=" ")
