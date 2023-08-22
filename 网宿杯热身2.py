arr = list(input().split(' '))
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
p = int(arr[3])
aaddbaddc = a+b+c
apbpc = a*b*c
asub = a-b
bsuc = b-c
print(aaddbaddc%p,end=' ')
print(apbpc%p,end=' ')
print(asub%p,end=' ')
print(bsuc%p)