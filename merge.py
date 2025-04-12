def merge(a,b):
    c=0
    d=[]
    while c < len(a):
        d.append(a[c])
        d.append(b[c])
        c+=1
    return d
a=[1,2,4]
b=[1,3,4]
print(merge(a,b))
