n = int(input())
sum=0
for i in range(1,n+1):
    if not(i%2==0 or i%3==0 or i%5==0):
        sum += 1

print(sum)   