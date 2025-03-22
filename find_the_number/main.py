def find(num):
    a=[]
    for i in range(num[0],num[-1]+1):
        if i not in num:
            a.append(i)
    return a
num=[1,2,4,5,6,8]
print(find(num))