n,k = list(map(int,input().split()))
for _ in range(k):
    lastDigit = n%10
    if lastDigit == 0:
        n//=10
    else:
        n -= 1
print(n)
