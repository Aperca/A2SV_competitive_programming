t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    check = True
    for i in range(n-1):
        if abs(arr[i] - arr[i+1]) > 1:
            check = False
            break

    if check:
        print("YES")
    else:
        print("NO")
