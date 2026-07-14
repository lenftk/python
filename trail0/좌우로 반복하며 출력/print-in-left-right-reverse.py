n=int(input())
arr=[]
for i in range(1,n+1):
    arr.append(i)

for i in range(n):
    for j in range(n):
        print(arr[j],end="")
    print()
    arr.reverse()