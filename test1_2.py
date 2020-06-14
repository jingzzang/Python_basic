#4
def func(list):
    tmp=[]
    for i in list:
        if i!=0:
            tmp.append(i)
    return tmp

def sol4(list):
    cnt=[0 for _ in range(1001)]
    for i in list:
        cnt[i]+=1
    li=func(cnt)
    return max(li)//min(li)
arr4=[1,2,3,3,1,3,3,2,3,2]
print(sol4(arr4))

#5
arr5=[1,4,2,3]
def sol5(list):
    ans=[]
    for i in range(len(list)):
        ans.append(list[-(i+1)])
    return ans
print(sol5(arr5))

#6
def sol6(n):
    cnt=0
    for i in range(1,n+1):
        c=i
        while c!=0:
            if c%10==3 or c%10==6 or c%10==9:
                cnt+=1
            c//=10
    return cnt
n=int(input(":"))
print(sol6(n))

#7
score=[650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
def sol7(scores):
    cnt=0
    for i in scores:
        if i>=650 and i<800:
            cnt+=1
    return cnt
print(sol7(score))

#8
#str="never odd or even"
str="palindrome"
def sol8(s):
    tmp=[]
    for i in s:
        if i!='.' and i!=' ':
            tmp.append(i)
    for j in range(len(tmp)//2):
        if(tmp[j]!=tmp[-(j+1)]):
            return "X"
            break
    return "O"
print(sol8(str))

#9
#str="senteeeencccccceeee"
str="senteeeencccccceieee"
def sol9(s):
    ans=s[0]
    for i in range(1,len(s)):
        if s[i-1]!=s[i]:
            ans+=s[i]
    return ans
print(sol9(str))