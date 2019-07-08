str4=input()
s1=0
for i in range(len(str4)):
  if(str4[i].isdigit() or str4[i].isalpha() or str4[i]==(" ")):
    continue
  else:
   s1+=1
print(s1)
