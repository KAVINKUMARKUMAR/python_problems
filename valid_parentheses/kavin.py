def romantoint(s:str) -> int:
    roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    b=0
    for a,c in zip(s,s[1:]):
        if roman[a] > roman[c]:
            b+=roman[a]
        else:
            b-=roman[a]
    return b+roman[s[-1]]
print(romantoint("XIX"))