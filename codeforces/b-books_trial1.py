n, t = map(int, input().split())
a = list(map(int, input().split()))

l = 0
current_sum = 0
max_books = 0

for r in range(n):
    current_sum += a[r]

    while current_sum > t:
        current_sum -= a[l]
        l += 1

    max_books = max(max_books, r - l + 1)

print(max_books)