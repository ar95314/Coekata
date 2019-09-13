num = int(input())
l = [int(l) for l in input().split()]
a=l.index(min(l))+1
b=l.index(max(l))+1
print(a,b)
