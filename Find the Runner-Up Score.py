n = int(input())
arr = list(map(int, input().split()))

a=set(arr)
b = max(a)
a.remove(b)
print(max(a))

