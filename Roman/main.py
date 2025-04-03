def romantoint(s):
    roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    b=0
    for c,d in zip(s,s[1:]):
        if roman[c]<roman[d]:
            b-=roman[c]
        else:
            b+=roman[c]
    return b+roman[s[-1]]
print(romantoint("XI"))
    