N = int(input())
for i in range(N):
	list1=[]
	l = input().split(" ")
	if l[0]== "insert":
    		list1.insert(int(l[1]), int(l[2]))
	if l[0]== "print":
    		print(list1)
	if l[0]== "remove":
    		list1.remove(int(l[1]))
	if l[0]== "append":
    		list1.append(int(l[1]))
	if l[0]== "sort":
    		list1.sort()
	if l[0]== "pop":
    		list1.pop()
	if l[0]== "reverse":
    		list1.reverse()