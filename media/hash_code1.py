a,b = map(int,input().rstrip().split())
type_pizzas = list(map(int,input().rstrip().split()))

sum_  =0
temp = type_pizzas
indexes = []
i=len(type_pizzas)
while(sum_<a and i>0):
    max_ = max(temp)
    if sum_+max_>=a :
        ind = temp.index(max_)
        temp[ind] = 0
    else :
        sum_+=max_
        ind = temp.index(max_)
        indexes.append(ind)
        temp[ind] = 0
    i-=1
print(len(indexes))
for i in range(0,len(indexes)):
    print(indexes[len(indexes)-1-i],end=" ")
print()
print(sum_)
