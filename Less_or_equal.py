n,k=map(int,input().split())
a = list(map(int, input().split()))
a.sort()
if a[k]<=a[k-1]:
    print (-1)
else:
    b=a[k-1]
    print (b+1)
