n = int(input())
s = list(input().split(' '))
count = int(s[0])
for i in range(1,n):
    count = (count*int(s[i])+count+int(s[i]))%998244353
print(count)