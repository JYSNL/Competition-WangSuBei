while(1):
    try:
        arr = list(input().split(' '))
        n = int(arr[0])
        m = int(arr[1])
        num_que = 0
        num_rec = 0
        count_hang = 0
        count_lie = 0
        for i in range(1,n+1):
            count_hang+=i
        for j in range(1,m+1):
            count_lie+=j
        while n>0 and m>0:
            num_que += n*m
            n-=1
            m-=1
        num_rec = count_hang*count_lie-num_que
        print(num_que,end=' ')
        print(num_rec)
    except:
        exit()