a,n=map(str,input().split())
gh=0
if len(a)>len(n):
  a,n=n,a
c=0
while c<len(a):
  gh+=(ord(n[c])-ord(a[c]))
  c+=1
for c in range(c,len(n)):
  gh+=ord(n[c])-ord('a')+1
print(gh)
