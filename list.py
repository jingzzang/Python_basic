#1
def solution(s):
    answer=[]
    for i in range(len(s)):
        rank=1
        for j in s:
            if s[i]<j:
                rank+=1
        answer.append(rank)
    return answer

score=[190,183,147,183,138,133,110,145]
ans=solution(score)
print(ans)

#2
point=[190, 183, 147, 183, 139, 133, 110, 145]
dec=point
dec.sort(reverse=True)

def ranks(arr):
    r=[0 for _ in range(len(arr))]
    r[0]=1
    same=0
    for i in range(len(arr)-1):
        if arr[i]==arr[i+1]:
            r[i+1]=r[i]
            same+=1
        else:
            r[i+1]=r[i]+1+same
            same=0
    return r

n=int(input("?"))
print(point[n])
ranking=ranks(dec)
print(ranking[dec.index(147)])