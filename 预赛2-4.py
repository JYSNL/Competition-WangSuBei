n = int(input())
yuan = []
ling = []
for i in range(0,n):
    temp = list(input().split(' '))
    yuan.append(int(temp[0]))
    ling.append(int(temp[1]))
moli_yuan = 0
moli_ling = 0
differ = []
for i in range(0,n):
    differ.append(abs(moli_yuan-moli_ling))

y_or_l = 0
temp = -1 #存放两者之间选择的下标
shit = -10 #两者差别的值
for i in range(0,n):
    if differ[i]>shit:
        shit = differ[i]
        temp = i
    elif differ[i] == shit:
        if i%2==0:
            if ling[i] > ling[temp]:
                temp = i
        else:
            if yuan[i] > yuan[temp]:
                temp = i
    elif differ[i]==0:
        if i%2==0:
            if yuan[i]-ling[i]>yuan[temp]-ling[temp]:
                temp = i
        else:
            if ling[i]-yuan[i]>ling[temp]-yuan[temp]:
                temp = i
    if i%2==0:
        moli_yuan+=yuan[i]
    else:
        moli_ling+=ling[i]
    temp = -1
    shit = -10
print(moli_yuan-moli_ling)