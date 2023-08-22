n = int(input())
arr = list(input().split(' '))
for i in range(0,len(arr)):
    arr[i] = int(arr[i])
count = 0
prearr = [0]
nowarr = []
for i in range(0,len(arr)):
    if i==0:
        nowarr.append(arr[i])
    elif i!=len(arr)-1 and arr[i]>=min(arr[i+1:len(arr)]):
        nowarr.append(arr[i])
    else:
        count+=1
count+=1
print(count)