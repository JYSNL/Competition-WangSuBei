#分糖果
t = int(input())
start_s = 1
for i in range(0,t):
    arr = list(input().split(' '))
    timet = int(arr[0])
    s_m = int(arr[1])
    m_s = int(arr[2])
    if s_m+2>=m_s:
        start_s+=timet
        print(start_s)
    else:
        if s_m-start_s<=timet:
            timet -= s_m - start_s
            start_s = s_m
            t1 = timet//2
            t2 = timet%2
            start_s+=(m_s-s_m)*t1
            if t2==0:
                print(start_s)
            elif t2==1:
                print(start_s+1)
        else:
            print(start_s+timet)
    start_s = 1
