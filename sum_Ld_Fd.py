n = int(input())
rev=0
fd=0
s=0

ld=n%10
while n>0:
    r = n%10
    rev = rev * 10 + r
    n = int(n/10)
    
fd = rev %10
s=fd+ld
print(s)
    
