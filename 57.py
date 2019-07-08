y,z=map(int,input().split())
x=list(map(int,input().split()[:y]))
count=0
for j in range(0,y):
    if(x[j]==z):
        count=count+1
print(count)
