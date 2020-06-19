#5
attack=30
recovery=10
def sol5(hp):
    hp-=attack
    cnt=1
    while hp>0:
        hp+=recovery
        hp-=attack
        cnt+=1
    return cnt
print(sol5(60))

#6
floors=[1,2,5,4,2]
def sol6(floor):
    ans=0
    for i in range(len(floor)-1):
        d=floor[i]-floor[i+1]
        if d<0:
            d=-d
        ans+=d
    return ans
print(sol6(floors))

#8
def sol8(n):
    l=[2,3,5,7]
    ans=0
    while n>0:
        tmp=n%10
        for i in l:
            if i==tmp:
                ans+=1
                break
        n//=10
    return ans
number=29022531
print(sol8(number))

#9
votes=[2,5,3,4,1,5,1,5,5,3]
n=5
candidate=[0 for _ in range(n+1)]
def sol9(m):
    for i in votes:
        candidate[i]+=1
    ans=0
    for j in candidate:
        if j==m:
            ans+=1
    return ans
k=2
print(sol9(k))

#10
cri=[1000000,600000,400000,200000]
gift=[50000, 30000, 20000, 10000]
purchase=[150000,210000,399990,990000,1000000]
def sol10(p):
    sum=0
    for i in p:
        for j in range(len(cri)):
            if i>=cri[j]:
                sum+=gift[j]
                break
    return sum
print(sol10(purchase))