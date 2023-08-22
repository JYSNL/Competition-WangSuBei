arr = list(input())
arr.reverse()
temp = 1
count = 0
for i in range(0,len(arr)):
    count+=int(arr[i])*temp
    temp*=2
print(count)