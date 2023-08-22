n = int(input())
s1 = list(input())
s2 = list(input())
s3 = list(input())
count = 0
for i in range(0,n):
    if s1[i]==s2[i]==s3[i]:
        count+=0
    elif s1[i]==s2[i] or s1[i]==s3[i] or s2[i]==s3[i]:
        count+=1
    else:
        count+=2
print(count)