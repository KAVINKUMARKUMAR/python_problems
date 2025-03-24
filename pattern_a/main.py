def pattern(n):
    a=0
    for i in range(n,0,-1):
        a+=1
        print(" "*i,"*"*a)
pattern(5)