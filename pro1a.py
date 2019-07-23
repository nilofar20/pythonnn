def longest(z1,z2):
        if(z1 in z2):
            return z1
        else:
            return longest(z1[0:len(z1)-1],z2)
i = int(input())
a= []
for _ in range(0,i):
    a.append(input())
a.sort()
print(longest(a[0],a[i-1]))
