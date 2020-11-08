# Enter your code here. Read input from STDIN. Print output to STDOUT
A = int(input())
B = input().split()
C = int(input())
D = input().split()
B = [int(i) for i in B]
D = [int(i) for i in D]
B = set(B)
D = set(D)
E = B.intersection(D)
E = list(E)
print(len(E))