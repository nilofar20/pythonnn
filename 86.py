nil=list(input())
ant=[]
for k in nil:
   if k not in ant:
      ant.append(k)
if nil==ant:
   print("Yes")
else:
   print("No")
