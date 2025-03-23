a=[7,0,18,0,10,1,17]
b="".join(map(str,a))
c=""
d=""
for i in b:
    if i=="0":
        c+=i
    else:
        d+=i
e=d+c
print(e)