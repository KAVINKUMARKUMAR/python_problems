def two_sum(num,target):
    c={}
    for i,sum in enumerate(num):
        com=target-sum
        if com in c:
            return [c[com],i]
        c[sum]=i
num=[2,7,11,15]
target=9
print(two_sum(num,target))