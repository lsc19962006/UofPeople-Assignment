def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
def output(z):
    op=open("output.txt","w")
    op.write(z)
    op.close

di=open("dict_.txt")
c=eval(di.read())
di.close()
c=invert_dict(c)
output(str(c))
