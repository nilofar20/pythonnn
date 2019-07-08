y,z=map(int,input("").split())
y=y ^ z
z=y ^ z
y=y ^ z
print(y,z)
