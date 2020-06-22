#1
student=[20,60,98,59]
def rev(arr):
    arr.sort(reverse=True)
    return arr

def sol1(m):
    grades=rev(student)
    for i in range(len(grades)):
        if m==grades[i]:
            return i+1
    return 0

n=int(input(": "))
ans=sol1(student[n])
print(ans)

#2
current=[70,100,70,80,50,95]
last=[35,65,80,50,20,60]
gap=[j-v for j,v in zip(current,last)]
ans=[-1 for _ in current]
m=max(gap)
for i in range(len(gap)):
    if gap[i]==m:
        ans[i]=1

def grade(arr):
    p=rev(arr)
    r=int(len(p)*0.1)+1
    for i in range(r):
        for j in range(len(arr)):
            if p[i]==arr[j]:
                if arr[j]>=80:
                    ans[j]=1

def count(arr):
    cnt=0
    for i in arr:
        if i>0:
            cnt+=1
    return cnt

grade(current)
print(count(ans))
