def valid(par):
    a={')':'(',']':'[','}':'{'}
    b=[]
    for i in par:
        if a in i:
            c=b.pop() if b else "#"
            if a[i]!= c:
                return False
        else:
            b.append(i)
    return not b
print(valid("()"))