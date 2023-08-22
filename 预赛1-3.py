t = int(input())
jiance = []
shi = 10
for i in range(1,19):
    jiance.append(shi)
    shi = shi*10
count = 0
c = 0
num = input()
while(num):

    num_real = int(num)
    num_arr = list(num)
    for i in range(0,len(num_arr)):
        count+=int(num_arr[i])
    if(num_real in jiance):
        count += 10
    else:
        count*=2
    print(count)
    count = 0
    c+=1
    if(c == t):
        exit()
    num = input()