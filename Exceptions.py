# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    l = list(input().split())#
    try:
        a=int(l[0])
        b=int(l[1])

        print(int(a//b))
    except Exception as e:
        print("Error Code:",e)
    