t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    
    possible = True
    for i in range(1, n):
        if a[i] - a[i-1] > 1:
            possible = False
            break
    
    print("YES" if possible else "NO")