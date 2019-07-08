v=list(input())
if len(v)%2==0:
    v[int(len(v)/2)]='*'
    v[int(len(v)/2)-1]='*'
else:
    v[int(len(v)/2)]='*'
for i in range(len(v)):
    print(v[i],end='')
