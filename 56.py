z=input()
for v in range(0,len(z)):
   if(z[v].isalpha() and z[v].isdigit()):
    print("No")
else:
  print("Yes")
