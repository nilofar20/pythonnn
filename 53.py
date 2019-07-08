Names=int(input())
nilo=0
i=0
while(Names>0):
    i=Names%10
    nilo=nilo+i
    Names=Names//10
print(nilo)
