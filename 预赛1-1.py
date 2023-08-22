n = int(input())
arr = list(input().split(' '))
temp = 9999999
for i in range(0,n):
    if int(arr[i])<temp:
        temp = int(arr[i])
for i in range(0,n):
    if int(arr[i])==temp:
        print(temp,end=' ')
        print(i+1)
        exit()