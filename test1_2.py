#6
def solution(n):
    cnt=0
    for i in range(1,n+1):
        c=i
        while c!=0:
            if c%10==3 or c%10==6 or c%10==9:
                cnt+=1
            c//=10
    return cnt
n=int(input(":"))
print(solution(n))

#8
str="never odd or even"
def sol(s):
    tmp=[]
    for i in s:
        if i!='.' and i!=' ':
            tmp.append(i)
    for j in range(len(tmp)//2):
        if(tmp[j]!=tmp[-(j+1)]):
            return "X"
            break
    return "O"
print(sol(str))