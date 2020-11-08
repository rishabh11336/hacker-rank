n = int(input())
s = set(map(int, input().split()))
b = int(input())
for i in range(b):
    a = input().split(" ")
    if(a[0] == 'pop'):
        s.pop()
    if(a[0] == 'remove'):
        s.remove(int(a[1]))
    if(a[0] == 'discard'):
        s.discard(int(a[1]))
s=list(s)
t=sum(s)
print(t)