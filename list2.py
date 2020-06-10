#2
def rank(scores, i):
    ans=1
    for x in scores:
        if x==i:
            return ans
        ans+=1
    return 0

def solution(sc, m):
    x=sc[m]
    sc.sort(reverse=True)
    return rank(sc, x)

score=[190, 183, 147, 183, 139, 133, 110, 145]
n=int(input("n?"))
print(solution(score, n))

#3
cards="BCDAABCBADBBDACADCDB"
n=int(input("n?"))

def sum(arr):
    scores = {"A": 1, "B": 2, "C": 3, "D": 4}
    ans=0
    for i in arr:
        ans+=scores[i]
    return ans

def div(arr,start):
    return arr[start::2]

def result(s1,s2):
    if s1>s2:
        return [1,s1]
    elif s1<s2:
        return [2,s2]
    else:
        return [0,s1]

p1=div(cards,0)[:n] #index<n
p2=div(cards,1)[:n]
score1=sum(p1)
score2=sum(p2)
print(result(score1,score2))