#1
def key(a,b):
    m=max(a)
    n=max(b)
    return max(m,n)

def sol1(arr):
    cnt=[0 for _ in range(11)]
    for i in arr:
        cnt[i]+=1
    return cnt

left=[2, 1, 2, 2, 4]
right=[1, 2, 2, 4, 4, 7]
left_cnt=sol1(left)
right_cnt=sol1(right)
p=key(left, right)
ans=0
for i in range(1, p+1):
    ans+=min(left_cnt[i], right_cnt[i])
print(ans)

#2
def sol2(n,m):
    cnt=0
    for i in n:
        if i%m==0:
            cnt+=1
    return cnt

n=[2, 3, 6, 9, 12, 15, 10, 20, 22, 25]
r3=sol2(n,3)
r5=sol2(n,5)
#print(r3,r5,sep="\t")
if r3>r5:
    ans="three"
elif r3<r5:
    ans="five"
else:
    ans="same"
print(ans)