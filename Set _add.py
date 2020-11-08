# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = [input() for i in range(a)]
b = set(b)
b = list(b)
print(len(b))