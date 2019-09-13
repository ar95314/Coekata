x=[int(x) for x in input().split()]
diff=0
for i in range(0,len(x)-1,2):
    diff=abs(x[i+1]-x[i])
    print(diff)
