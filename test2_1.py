#3
n=int(input("n: "))
m=int(input("m: "))
sum=0
for i in range(n,m+1):
    if i%2==0:
        sum+=i*i
print(sum)

#4
arr4=["my", "favorite","color","is","violet"]
arr4_1=["yes","i","am"]
ans=""
for i in arr4_1:
    if len(i)>=5:
        ans+=i
if ans=="":
    print("empty")
else:
    print(ans)

#4-1
def print_l(arr):
    for j in arr:
        print(j, end="")
    print()

answer=[]
for i in arr4:
    if len(i)>=5:
        answer.append(i)
if len(answer)==0:
    print("empty")
else:
    print_l(answer)