a1,b2=map(int,input().split())
input()
li3=list(map(int,input().split()))[:a1]
addli3=list(map(int,input().split()))[:b2]
result=[]
for i in addli3:
    li3.append(i)
    print(max(li3),end= " ");
