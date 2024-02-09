stops = int(input())
nPeople , ans = 0,0
for stop in range(stops):
    exit,enter = list(map(int,input().split()))
    nPeople += enter - exit
    ans = max(ans,nPeople)
print(ans)
