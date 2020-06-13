#1
shirt_size=["XS","S","L","L","XL","S"]
counter=[0 for _ in range(6)]
for i in shirt_size:
    if i=="XS":
        counter[0]+=1
    elif i=="S":
        counter[1]+=1
    elif i=="M":
        counter[2]+=1
    elif i=="L":
        counter[3]+=1
    elif i=="XL":
        counter[4]+=1
    else:
        counter[5]+=1
print(counter)

#1-2
cnt={"XS":0, "S":0, "M":0, "L":0, "XL":0, "XXL":0}
for size in shirt_size:
    cnt[size]+=1
answer=[]
for i in cnt:
    answer.append(cnt[i])
print(answer)

#2
def solution(level, value):
    if level=='S':
        answer=int(value*0.95)
    elif level=='G':
        answer=int(value*0.9)
    elif level=='V':
        answer=int(value*0.85)
    return answer

def sol2(level, value):
    mul = {'S':0.95, 'G': 0.9, 'V': 0.85}
    ans=value*mul[level]
    return int(ans)

rank=input("?")
price=10000
answer=solution(rank,price)
print(answer)
sol2(rank, price)
print(answer)