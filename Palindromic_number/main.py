def pali(num):
    num=str(num)
    a=num[::-1]
    if(a==num):
        return "True"
    else:
        return "false"
print(pali(''))