def paldrinome(n):
    return n==n[::-1]

n ='gfg'
ans = paldrinome(n);
if ans:
    print("yes")
else:
    print("no")

def number(s):
    temp=s
    r=0
    while s>0:
        s = temp/10
        r=r*10+r
        temp=temp//10
    if n==r:
        print("yes")
    else:
        print("no")


number(548)


