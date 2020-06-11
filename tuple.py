#1-1
cleaning = ["o","x","x","o","o","x","o","o","x","x"]
ans1=[]
for i in range(len(cleaning)):
    if cleaning[i]=="x":
        ans1.append(i+1)
ans1.sort()
print(ans1)

#1-2
ans=[]
for room, ox in enumerate(cleaning):
    if ox=="x":
        ans.append(room+1)
ans.sort()
print(ans)

#2
def minimum(p, n):
    ans=0
    for a,b in zip(p,n):
        ans=min(ans,b-a)
    return ans

def maximum(p,n):
    ans=0
    for a,b in zip(p,n):
        ans=max(ans, b-a)
    return ans

pre=[20,50,35]
next=[15,55,75]

best=maximum(pre, next)
worst=minimum(pre, next)
ans=[best,worst]
print(ans)
