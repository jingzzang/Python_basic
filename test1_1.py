#3
months=[31,28,31,30,31,30,31,31,30,31,30,31]
def solution(month, day):
    sum=-1;
    for i in range(month):
        sum+=months[i]
    sum+=day
    return sum

m=int(input("m :"))
d=int(input("d :"))
print(solution(m-1,d))
