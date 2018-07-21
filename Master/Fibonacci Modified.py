# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
def fiba(n):
    #n=100
    global d
    # if n<
    if n in d:
        return d[n]
    else:
        d[n]=fiba(n-2)+(fiba(n-1))**2
    return d[n]
x=[int(x) for x in input().split()]
d={0:x[0],1:x[1]}
fiba(20)
print(d[x[2]-1])