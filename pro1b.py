z,intg1=input().strip().split(" ")
intg1=int(intg1)
i=0;
while i<len(z)-1 and intg1:
	if(z[i]>z[i+1]):
		intg1-=1
		z=z[:i]+z[i+1:]
		if(i!=0):
			i-=1
	else:
		i+=1
s=z[:len(z)-intg1]
print(s)
