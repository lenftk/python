n = int(input())
arr = []
for i in range(n):
    if i%2==0:
        arr.append(1)
    else:
        arr.append(n)

for i in range(n):
    for j in range(n):
        print(arr[j],end="")
        if j%2==0:
            arr[j] +=1
        else:
            arr[j] -=1
    print()

