an=int(input())
for v in range(2,an):
    if an%v==0:
        print("no")
        break
else:
    print("yes")
