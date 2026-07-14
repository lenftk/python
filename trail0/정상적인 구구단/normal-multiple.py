n = int(input())

nth=False
for i in range(1,n+1):
    for j in range(1,n+1):
        print(f"{i} * {j} = {i*j}",end="")
        if j%n==0:
            nth=True
        if not nth:
            print(", ",end="")
        else:
            nth=False
    print()