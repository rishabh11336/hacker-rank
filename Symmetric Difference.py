# Enter your code here. Read input from STDIN. Print output to STDOUT
A = int(input())
B = input().split()
C = int(input())
D = input().split()
B = [int(i) for i in B]
D = [int(i) for i in D]
B = set(B)
D = set(D)
E = B.symmetric_difference(D)
E = list(E)
E = sorted(E)
for i in E:
    print(i)