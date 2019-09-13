n=int(input())
l=list(map(int,input().split()))
ans=l[0]
for i in range(n):
    ans &= l[i]
print(ans)
