n=int(input())

info2=[]

for i in range(n):
    info = input().split(" ")
    info2.append(info)
info1 = input()
for i in range(n):
    if(info1==info2[i][0]):
        sum1 = float(info2[i][1])+float(info2[i][2])+float(info2[i][3])
        observation=len(info2[i][1:])
avg=sum1/observation
print( '%.2f' %avg)