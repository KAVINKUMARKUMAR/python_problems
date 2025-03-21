def commo(strs):
    prefix=strs[0]
    for i in strs[1:]:
        while not i.startswith(prefix):
            prefix=prefix[:-1]
    return prefix
    if not prefix:
        return ""
strs=["shap","shape","share"]
print(commo(strs))