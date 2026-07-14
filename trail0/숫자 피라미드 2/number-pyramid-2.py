n = int(input())
sum=0
for i in range(1,n+1):

    for j in range(i):
        sum += 1
        print(sum,end=" ")
    print()